from subprocess import check_output, run, Popen, CalledProcessError
from lib import *
from re import split as sp
from libqtile import qtile

cmd_output = lambda command: check_output(command, shell=True, encoding='utf-8').split()[0]

def dbg(text):
    call('echo ' + text + ' >> /home/mcnuggetsx20/.config/qtile/debug', shell=True)

def vol1(device=None, status=None):
    if status==None:
        if device==None:
            return
        elif device=='mic':
            status = check_output("pactl get-source-volume %s | awk -F ' / ' 'FNR<2 {print  $(NF-1)}'" %mic,shell=True, encoding='utf-8')[:-2]
        else:
            status = check_output("pamixer --get-volume" ,shell=True, encoding='utf-8').split()[0]
    try:
        status = int(status)
    except:
        status = 0

    #   =====|----
    seg1 = status // 15 * 'I'
    seg2 = ((10 - len(seg1)) * 'I')[:-1]
    return [seg1, seg2, str(status)]


def volumechange(ok):
    def a(qtile):
        if ok:
            val = 5
        else:
            val = -5

        status = int(check_output('pamixer --get-volume', shell=True, encoding='utf-8').split()[0]) + val
        run(f'pamixer --set-volume {status}', shell=True) #change

        #a = vol1(status=status)

        #qtile.widgets_map['vol_level1'].update(' ' + a[0])
        #qtile.widgets_map['vol_rest1'].update(a[1])
        #qtile.widgets_map['vol_number1'].update(a[2]+'%')

        #qtile.widgets_map['vol_level2'].update(' ' + a[0])
        #qtile.widgets_map['vol_rest2'].update(a[1])
        #qtile.widgets_map['vol_number2'].update(a[2]+'%')
    return a


def mic_vol_change(ok):
    def a(qtile):
        val = -5 + 10 * int(ok)

        com = "pactl get-source-volume %s | awk -F ' / ' 'FNR<2 {print  $(NF-1)}'" %mic
        status = check_output(com ,shell=True,encoding='utf-8')[:-2]

        com = "pactl set-source-volume %(dev)s +%(level)i%(perc)s" % {'dev': mic, 'level': val, 'perc':'%'}
        run(com ,shell=True)

        a = vol1(status=int(status)+val)

        qtile.widgets_map['mic_level1'].update(' ' + a[0])
        qtile.widgets_map['mic_rest1'].update(a[1])
        qtile.widgets_map['mic_number1'].update(a[2]+'%')

        #qtile.widgets_map['mic_level2'].update(' ' + a[0])
        #qtile.widgets_map['mic_rest2'].update(a[1])
        #qtile.widgets_map['mic_number2'].update(a[2]+'%')
    return a


def ChangeAudioDevice(init=False):
    global sinks, device_indicators, cmd_output


    def a(qtile):
        #curr = check_output('pacmd list | grep "active port: <analog-output"', shell=True, encoding='utf-8')
        #curr = sp('\t|\n', curr)[1]

        #desired = 'headphones' not in curr

        #run('pactl set-sink-port ' + devices[0] +' ' + ports[ int(desired) ], shell=True)

        #desired = device_indicators[ int( 'headphones' not in curr) ]

        current = cmd_output('pactl get-default-sink')
        ind = not sinks.index(current)

        run(f'pactl set-default-sink {sinks[ind]}', shell=True)

        qtile.widgets_map['AudioDeviceIndicator1'].update(' '+ device_indicators[ind] +' ')
        #qtile.widgets_map['AudioDeviceIndicator2'].update(' ' + desired + ' ')

    if not init:
        return a

    else:
        try:
            curr = check_output('pacmd list | grep "active port: <analog-output"', shell=True, encoding='utf-8')
            curr = sp('\t|\n', curr)[1]
            return device_indicators[ int( 'headphones' in curr) ]
        except CalledProcessError:
            return device_indicators[0]


def fanSpeed(ok):
    def a(qtile):
        val = -5 + 10 *int(ok)
        curr = int(check_output('nvidia-smi --query-gpu=fan.speed --format=csv,noheader,nounits',shell=True,encoding='utf-8')[:-1])
        curr = str(curr+val)
        Popen('nvidia-settings -a "[fan:0]/GPUTargetFanSpeed="' + curr, shell=True)
    return a


def DiskSpace():
    return ' ' + check_output('df -h --output=source,used,size | grep "nvme0n1p1\|nvme0n1p4\|sda1" | awk \'{printf $2 "/" $3 " "}\'', shell=True, encoding='utf-8')[:-1] + ' '


def brightness_toggle(n):
    #status = check_output("xrandr --current --verbose | grep Gamma", shell=True, encoding='utf-8').split(':')[2]
    run("xrandr --output DP-4 --gamma %(new)f" % {'new': n}, shell=True, encoding='utf-8')
    return

        
def screenshot(qtile):
    screen=int(qtile.current_screen.index)
    monitor_list = check_output("xrandr --query | grep ' connected '",shell=True, encoding='utf-8').split('\n')

    desired_res = None

    for i in monitor_list:
        if 'None' in i: continue
        if not screen and 'primary' in i:
           # print(i.split()[3])
            desired_res = i.split()[3]
        elif screen and 'primary' not in i:
            #print(i.split()[2])
            desired_res = i.split()[2]

    monitors=[
            '+0+0',
            '+3440+1440',
    ]

    resolutions=[
            '3440x1440',
            '1080x1920',
    ]

    Popen(f'maim -g {desired_res} ~/Pictures/shot.png; xclip -selection clipboard -t image/png -i ~/Pictures/shot.png', shell=True)


def network_current():
    st = check_output("nmcli -t connection show --active | awk -F ':' '{print $1 " + '"\\n"' + " $(NF-1)}'", shell=True, encoding='utf-8').split('\n')[:-1]
    st.append('None')
    st.append('None')

    current_net_dev = network_devices[st[1].split('-')[-1]]
    qtile.widgets_map['network_device1'].update(current_net_dev + ' ')
    qtile.widgets_map['network_name1'].update(' ' + st[0])

    #qtile.widgets_map['network_device2'].update(' ' + current_net_dev)
    #qtile.widgets_map['network_name2'].update(' ' + st[0])
    return ''


def wttr(loc):
    def a():
        wtt = check_output("curl -s wttr.in/"+loc+"?format=4", shell=True, encoding='utf-8').split()
        return ' '.join(wtt) 
    return a

def compswitch(qtile):
    global comp
    command = 'killall ' * comp + 'picom'
    #command = 'killall ' * int(comp) + 'picom'
    Popen(command, shell=True)
    comp = not comp
    #qtile.widgets_map['debug'].update(str(comp))

def walpSwitch(qtile):
    global walp, glx

    toSet = WALLPAPER
    if walp:
        toSet = '/mnt/hdd/zdjecia/wallpaper/black.png'
    qtile.screens[0].cmd_set_wallpaper(toSet, 'stretch')
    walp = not walp

def gammaGaming(name):
    global gamma_rules, curr_gamma
    if name in gamma_rules:
        #qtile.widgets_map['debug'].update('jest')
        brightness_toggle(gamma_rules[name])
        curr_gamma = gamma_rules[name]

    elif curr_gamma != 1:
        brightness_toggle(1)
        curr_gamma = 1

def groupSwitch(group):
    def a(qtile):
        global bars
        qtile.groups_map[group.name].cmd_toscreen()
        #if group.position == 5 or not bars:
        #    qtile.cmd_hide_show_bar()
        #    bars = not bars
        #    walpSwitch(qtile)
        #    compswitch(qtile)

    return a

def resSwitch(qtile):
    global RES
    offset = [0,0]
    config = config_class()

    with open('/home/mcnuggetsx20/.config/qtile/res_config') as f:
        for i in f.read().split('\n')[:-1]:
            temp = i.split('=')
            setattr(config, temp[0], temp[1])

    if RES: 
        if config.SCALE_TO != config.RES_DEFAULT:
            res_list_custom = list(map(int, config.SCALE_TO.split('x')))
            res_list_default = list(map(int, config.RES_DEFAULT.split('x')))
            offset[0] = (res_list_default[0] - res_list_custom[0]) // 2
            offset[1] = (res_list_default[1] - res_list_custom[1]) // 2

        command = f'nvidia-settings -a CurrentMetaMode="DP-4: 3440x1440_100 @{config.RES_CUSTOM} +0+0 {{ViewPortIn={config.RES_CUSTOM}, ViewPortOut={config.SCALE_TO}+{offset[0]}+{offset[1]}, ForceCompositionPipeline=Off, ForceFullCompositionPipeline=Off}}"'
    else: command = 'nvidia-settings -a CurrentMetaMode="DP-4: 3440x1440_100 @3440x1440 +0+0 {ViewPortIn=3440x1440, ViewPortOut=3440x1440+0+0, ForceCompositionPipeline=On, ForceFullCompositionPipeline=On}"'

    RES = not RES

    run(command, shell=True)
    run(RES_SECONDARY, shell=True)
    run(DPI_COMMAND, shell=True)

    qtile.widgets_map['current_resolution'].update(command[55:67])

