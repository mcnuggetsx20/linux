from subprocess import check_output, run, Popen
from lib import *

def vol1():
    com = check_output('pamixer --get-volume', shell=True, encoding='utf-8').split()
    #   =====|----
    seg1 = (int(com[0]) // 15) * 'I'
    return [seg1, com[0]]

def vol2():
    return ((10 - len(vol1()[0])) * 'I')[:-1]

def volumechange(ok):
    def a(qtile):
        if ok:
            val = 5
        else:
            val = -5

        run('pulsemixer --change-volume ' + str(val), shell=True) #change

        a = vol1()
        b = vol2()

        qtile.widgets_map['vol_level1'].update(a[0])
        qtile.widgets_map['vol_rest1'].update(b)
        qtile.widgets_map['vol_number1'].update(a[1]+'%')

        qtile.widgets_map['vol_level2'].update(a[0])
        qtile.widgets_map['vol_rest2'].update(b)
        qtile.widgets_map['vol_number2'].update(a[1]+'%')
    return a

def mic_vol_change(ok):
    def a(qtile):
        val = -5 + 10 * int(ok)
        curr = check_output("pactl get-source-volume alsa_input.usb-C-Media_Electronics_Inc._USB_PnP_Sound_Device-00.mono-fallback | awk -F ' / ' 'FNR<2 {print  $(NF-1)}'",shell=True,encoding='utf-8')[:-1]
        run('pactl set-source-volume alsa_input.usb-C-Media_Electronics_Inc._USB_PnP_Sound_Device-00.mono-fallback ' + curr,shell=True)

        #qtile.widgets_map('mic_vol1').update(

def ChangeAudioDevice(init=False):
    global devices, device_indicators


    def a(qtile):
        curr = ''.join(check_output('pactl get-default-sink', shell=True, encoding='utf-8').split())
        desired = devices[(devices.index(curr) + 1) * int(devices.index(curr) != len(devices)-1)]

        run('pactl set-default-sink ' + desired, shell=True)

        a = vol1()
        b= vol2()

        qtile.widgets_map['vol_level1'].update(' ' +a[0])
        qtile.widgets_map['vol_rest1'].update(b)
        qtile.widgets_map['vol_number1'].update(a[1]+'%')
        qtile.widgets_map['AudioDeviceIndicator1'].update(' '+device_indicators[devices.index(desired)]+' ')

        qtile.widgets_map['vol_level2'].update(' ' +a[0])
        qtile.widgets_map['vol_rest2'].update(b)
        qtile.widgets_map['vol_number2'].update(a[1]+'%')
        qtile.widgets_map['AudioDeviceIndicator2'].update(' ' + device_indicators[devices.index(desired)] + ' ')

    if not init:
        return a

    else:
        curr = ''.join(check_output('pactl get-default-sink', shell=True, encoding='utf-8').split())
        return str(device_indicators[devices.index(curr)])

def fanSpeed(ok):
    def a(qtile):
        val = -5 + 10 *int(ok)
        curr = int(check_output('nvidia-smi --query-gpu=fan.speed --format=csv,noheader,nounits',shell=True,encoding='utf-8')[:-1])
        curr = str(curr+val)
        Popen('nvidia-settings -a "[fan:0]/GPUTargetFanSpeed="' + curr, shell=True)
    return a

        
