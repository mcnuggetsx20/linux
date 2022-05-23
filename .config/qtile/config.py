#figlet
#                                             _            ____   ___  
# _ __ ___   ___ _ __  _   _  __ _  __ _  ___| |_ _____  _|___ \ / _ \ 
#| '_ ` _ \ / __| '_ \| | | |/ _` |/ _` |/ _ \ __/ __\ \/ / __) | | | |
#| | | | | | (__| | | | |_| | (_| | (_| |  __/ |_\__ \>  < / __/| |_| |
#|_| |_| |_|\___|_| |_|\__,_|\__, |\__, |\___|\__|___/_/\_\_____|\___/ 
#                            |___/ |___/                               

from typing import List  # noqa: F401
from libqtile import bar, layout, widget, qtile, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.command import lazy
from libqtile.command.client import InteractiveCommandClient
from funx import *
from lib import *
from subprocess import call 
import os

orange = '#F0Af16'
ored   = '#F77B53'
black  = '#000000'
swamp  = '#335D03'  
lime   = '#32CD32'
green  = '#A9DC76'
violet = '#C76BFA'
dviolet= '#7A05BE'
dblue  = '#3A69F0'
white  = '#FFFFFF'
dgray  = '#312D2D'
gray   = '#D0D0D0'
red    = '#C61717'
dred   = '#6b1015'
solar  = '#fdf6e3'
transp = '#000000.00'

################### Hooks #########################
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    call([home + '/.config/qtile/autostart.sh'])

@hook.subscribe.client_new
def func(new_window):
    if new_window.name=='QPanel':
        new_window.cmd_static(screen=1) #The number of the xscreen you want to put QPanel on goes here
    #elif new_window.name=='QNetwork':
    #    new_window.cmd_focus()
    elif new_window.name=='QLauncher':
        new_window.cmd_static(screen=0, x = 0, y = 0)


#################### Variables #########################
mod = "mod1"
sup = "mod4"
terminal = "alacritty -e nvim -c term -c 'set ma' -c startinsert"
bar_indent=7
this_dir = '/home/mcnuggetsx20/.config/qtile/'

def qnetwork(qtile):
    screen = qtile.current_screen.index
    x = 1250 
    y = 910

    x += 1920 * int(not bool(screen))
    Popen('qnetwork ' + str(x) + ' ' + str(y), shell=True)

def screenshot(qtile):
    screen=qtile.current_screen.index
    screen = int(not bool(screen))
    screen += 1
    Popen('screenshot -m ' + str(screen),shell=True)


################### Keybinds #########################

keys = [
    #My stuff
    Key([sup], 'b', lazy.spawn('brave')),
    Key([mod], 'p', lazy.spawn("dmenu_run -sb '" + green + "' -nf '" + violet + "' -sf '" + black + "'")),
    Key([sup], 'f', lazy.spawn('pcmanfm')),
    Key([sup], 'm', lazy.spawn(terminal + ' -e htop')),
    Key([mod], 'e', lazy.to_screen(0)),
    Key([mod], 'w', lazy.to_screen(1)),
    Key([sup], 'p', lazy.spawn('feh /mnt/hdd/zdjecia/plan_lekcji.png')),
    Key([sup], 'q', lazy.spawn('sh power_menu')),
    Key([],    'XF86MonBrightnessDown', lazy.function(brightness_toggle())),

    #Volume Control
    Key([],    'XF86AudioRaiseVolume', lazy.function(volumechange(True))),
    Key([],    'XF86AudioLowerVolume', lazy.function(volumechange(False))),
    Key([],    'XF86AudioMute', lazy.spawn('pulsemixer --toggle-mute')),

    Key([sup], 'XF86AudioRaiseVolume', lazy.function(mic_vol_change(True))),
    Key([sup], 'XF86AudioLowerVolume', lazy.function(mic_vol_change(False))),
    Key([sup], 'XF86AudioMute', lazy.spawn('pulsemixer --toggle-mute')),
    Key([sup],  'v', lazy.spawn('pavucontrol')),


    Key([mod], 'F1', lazy.function(fanSpeed(False))),
    Key([mod], 'F2', lazy.function(fanSpeed(True))),

    Key([sup], 'bracketleft', lazy.spawn('sh qpanel -c /home/mcnuggetsx20/.config/qpanel/qnetwork/qnetwork.py')),
    Key([sup], 't', lazy.spawn('sh qpanel')),
    Key([sup], 'k', lazy.spawn('pkill -f qpanel')),

    Key([sup], 'a', lazy.function(ChangeAudioDevice(False))),
    Key([mod, 'shift'], 's', lazy.spawn('sh screenshot -s')),
    Key([], 'Print', lazy.function(screenshot)),
    Key([],    'XF86HomePage', lazy.spawn('brave')),
    Key([mod], 't', lazy.window.toggle_floating()),
    Key([sup], 'j', lazy.window.toggle_minimize()),
    Key([mod], 'Tab', lazy.spawn('rofi -show window')),

    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),
    Key([mod], "s", lazy.group.prev_window()),
    Key([mod], "d", lazy.group.next_window()),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], 'i', lazy.layout.grow()),
    Key([mod], 'm', lazy.layout.shrink()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([sup], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "space", lazy.next_layout(), desc="Toggle between layouts"),
    Key([sup], "BackSpace", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
]

################### Layouts #########################

all_layouts = [
    layout.MonadTall(
        border_focus=green, 
        border_width=2, 
        single_border_width=2, 
        margin=6, 
        new_client_position='before_current', 
        change_ratio=0.025,
        min_ratio=0,
    ),
    layout.Max(border_width=0, border_focus='#000000'),
]
floating_layout = layout.Floating(
        border_width=2,
        border_focus=green,
        float_rules=[
            # Run the utility of `xprop` to see the wm class and name of an X client.
            *layout.Floating.default_float_rules,
            Match(wm_class='confirmreset'),  # gitk
            Match(wm_class='makebranch'),  # gitk
            Match(wm_class='maketag'),  # gitk
            Match(wm_class='ssh-askpass'),  # ssh-askpass
            Match(wm_class='polo'),  # ssh-askpass
            Match(title='branchdialog'),  # gitk
            Match(title='pinentry'),  # GPG key password entry
            Match(wm_class='feh'),
            Match(wm_class='pavucontrol'),
            Match(title='QNetwork'),
            Match(title='QLauncher'),
        ]
)

################### Groups #########################

groups = [
    Group(
        name='', 
        position=1, 
        layouts=all_layouts
    ),

    Group(
        name='', 
        position=2, 
        layouts=all_layouts
    ),

    Group(
        name='',
        position=3, 
        layouts=all_layouts
    ),

    Group(
        name='',
        position=4, 
        layouts=all_layouts, 
        matches = [
            Match(wm_class='discord')
        ]
    ),
        
    Group(
        name='', 
        position=5, 
        layouts=all_layouts, 
        matches = [
            Match(wm_class='teams')
        ]
    ),

    Group(
        name='', 
        position=6, 
        layouts=[floating_layout], 
        matches = [
            Match(wm_class='Steam'), 
            Match(wm_class='csgo_linux64'),
            Match(wm_class='hl2_linux'),
        ]
    ),
]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], str(i.position), lazy.group[i.name].toscreen()),
        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], str(i.position), lazy.window.togroup(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])


################### Screens, widgets and their support functions #########################

widget_defaults = dict(
    font='IBM Plex Mono Medium',
    fontsize=13,
    padding=0,
    inactive='#FFFFFF',
)
extension_defaults = widget_defaults.copy()

bar_color=solar+'.60'
bar_color2 = solar+'.80'
#bar_color = '#575458.90'

def network_current():
    st = check_output("nmcli -t connection show --active | awk -F ':' '{print $1 " + '"\\n"' + " $(NF-1)}'", shell=True, encoding='utf-8').split('\n')[:-1]
    st.append('None')
    st.append('None')

    current_net_dev = network_devices[st[1].split('-')[-1]]
    qtile.widgets_map['network_device1'].update(current_net_dev + ' ')
    qtile.widgets_map['network_name1'].update(' ' + st[0])
    qtile.widgets_map['network_device2'].update(current_net_dev + ' ')
    qtile.widgets_map['network_name2'].update(' ' + st[0])
    return ''

def wttr_wojn():
    wtt = check_output("curl -s wttr.in/Wojnów?format=4", shell=True, encoding='utf-8').split()
    return ' '.join(wtt) 

def wttr_pion():
    wtt = check_output("curl -s wttr.in/Pionki?format=4", shell=True, encoding='utf-8').split()
    return ' '.join(wtt) 


screens = [
    Screen(
        wallpaper='/mnt/hdd/zdjecia/wallpaper/cool.jpg',
        wallpaper_mode='fill',

        #TOP1
        top=bar.Bar(
            margin=[0, 0, 0, 0], #[N, E, S, W]
            background = '#000000.00',
            widgets=[
                widget.TextBox(
                    text = 'A',
                    font='Bartek',
                    fontsize = 25,
                    foreground=bar_color,
                    background='#000000.00',
                    padding= -2,
                ),
                widget.GroupBox(
                    font='SauceCodePro NF', 
                    fontsize=14,
                    highlight_method='line', 
                    this_current_screen_border=violet, 
                    this_screen_border=violet,
                    block_highlight_text_color=green,
                    inactive=dgray,
                    active=dgray,
                    disable_drag=True,
                    use_mouse_wheel=False,
                    background = bar_color,
                ),

                widget.TextBox(
                    text = 'B',
                    font='Bartek',
                    fontsize = 25,
                    foreground=bar_color,
                    background='#000000.00',
                    padding= -2,
                ),
                
                widget.Spacer(
                    length = 10,
                    background='#000000.00',
                ),

                widget.TaskList(
                    parse_text=lambda text: ' ', 
                    borderwidth=0, 
                    margin_x=0, 
                    margin_y=0, 
                    icon_size=18, 
                    txt_floating='',
                    background=transp,
                ),

                widget.Spacer(
                    length = 15,
                    background='#000000.00',
                ),

                widget.TextBox(
                    text = 'A',
                    font='Bartek',
                    fontsize = 25,
                    foreground=bar_color,
                    background='#000000.00',
                    padding= -2,
                ),

                widget.GenPollText(
                    name = 'weather1',
                    func = wttr_wojn,
                    foreground = dgray,
                    background = bar_color,
                    update_interval=600,
                ),
                widget.TextBox(
                    text = 'B',
                    font='Bartek',
                    fontsize = 25,
                    foreground=bar_color,
                    background='#000000.00',
                    padding= -2,
                ),

                widget.Spacer(
                    length = bar.STRETCH,
                    background='#000000.00',
                ),

                widget.StatusNotifier(
                    highlight_colour=dviolet,
                    menu_foreground = gray,
                    #menu_background = dgray,
                    menu_font = widget_defaults['font'],
                    menu_fontsize = widget_defaults['fontsize'],
                    menu_row_height = 11,
                    icon_size=18,
                    padding=5,
                ),

                widget.TextBox(
                    text = 'A',
                    font='Bartek',
                    fontsize = 25,
                    foreground=dviolet,
                    background='#000000.00',
                    padding= -2,
                ),

                widget.TextBox(
                    name='network_device1',
                    background=dviolet,
                    foreground=black,
                    font='Font Awesome 6 Free Solid',
                    fontsize=12,
                ),

                widget.TextBox(
                    text='Searching...',
                    name='network_name1',
                    foreground=dgray,
                    background=bar_color2,
                ),

                widget.TextBox(
                    text = 'B',
                    font='Bartek',
                    fontsize = 25,
                    foreground=bar_color2,
                    background='#000000.00',
                    padding= -2,
                ),
                
                widget.Spacer(
                    length = 10,
                    background='#000000.00',
                ),

                widget.TextBox(
                    text = 'A',
                    font='Bartek',
                    fontsize = 25,
                    foreground=green,
                    background='#000000.00',
                    padding= -2,
                ),
                widget.TextBox(
                    text=' ',
                    font='mononoki',
                    fontsize=14,
                    foreground=black,
                    background=green,
                ),

                widget.Clock(
                    foreground=dgray, 
                    background=bar_color2,
                    padding=0,
                    format=" %H:%M:%S",
                ),
                widget.TextBox(
                    text = 'B',
                    font='Bartek',
                    fontsize = 25,
                    foreground=bar_color2,
                    background='#000000.00',
                    padding= -2,
                ),

            ], 
            size=18
        ),

        #BOTTOM1
        bottom=bar.Bar(
            #margin=[0, 0, 0, 0], #[N, E, S, W]
            #background='#1b1919.90',
            background='#000000.00',
            widgets= [
                widget.Spacer(
                    length=bar_indent,
                ),

                widget.TextBox(
                    text = 'C',
                    font='Bartek',
                    fontsize=30,
                    foreground=black,
                    background=dviolet,
                ),

                widget.TextBox(
                    text = ' ' + check_output('uname -r', shell=True, encoding='utf-8').split()[0] + ' ',
                    foreground=gray,
                    background=dgray,
                ),

                widget.Spacer(
                   length=12,
                ),
                widget.TextBox(
                    text='  ',
                    font='mononoki',
                    background=dviolet,
                    foreground=black,
                ),

                widget.CPU(
                    foreground=gray, 
                    background=dgray,
                    format=' {load_percent}% ', 
                    update_interval=1.0,
                ),

                widget.Spacer(
                   length=12,
                ),

                widget.TextBox(
                    text='  ',
                    font='mononoki',
                    background=dviolet,
                    foreground=black,
                ),

                widget.NvidiaSensors(
                    foreground=gray, 
                    background=dgray,
                    format=' {temp}°C {fan_speed} ',
                    update_interval = 1,
                    threshold=70,
                ),

                widget.Spacer(
                    length = 12,
                ),
                widget.TextBox(
                    text = '  ',
                    foreground = black,
                    background = dviolet,
                    font = 'Font Awesome 6 Free Regular',
                ),

                widget.Memory(
                    name = 'memory',
                    foreground=gray, 
                    background=dgray,
                    format=' {MemUsed:.0f} MB ',
                    update_interval = 1,
                    font='IBM Plex Mono Medium',
                ),

                widget.Spacer(
                    length=12,
                ),

                widget.TextBox(
                    text = '   ',
                    foreground = black,
                    background = dviolet,
                ),

                widget.GenPollText(
                    name= 'disk space',
                    func = DiskSpace,
                    background = dgray,
                    foreground = gray,
                ),
                
                widget.Spacer(
                    length=bar.STRETCH,
                ),

                widget.Systray(),

                widget.TextBox(
                    text='   ' ,
                    background = dviolet,
                    foreground = black,
                    padding=-2,
                ),

                widget.Net(
                    format=' {down}↓ {up}↑ ',
                    background=dgray,
                    foreground=gray,
                    prefix='M'
                ),

                widget.Spacer(
                    length=12,
                ),

                widget.TextBox(
                    text = '  ',
                    name = 'MicIcon1',
                    background=dviolet,
                    foreground=black,
                    font = 'mononoki',
                ),

                widget.TextBox(
                    name = 'mic_level1',
                    text=' ' + vol1(device='mic')[0],
                    background=dgray,
                    foreground=green,
                    font = 'Ubuntu Bold',
                    fontsize=12,
                ),

                widget.TextBox(
                    name = 'mic_rest1',
                    text=vol1(device='mic')[1],
                    font = 'Ubuntu Bold',
                    fontsize=12,
                    foreground=black,
                    background=dgray,
                ),

                widget.TextBox(
                    text='(',
                    foreground=green,
                    background=dgray,
                ),

                widget.TextBox(
                    name='mic_number1',
                    text = vol1(device='mic')[2]+'%',
                    foreground=violet,
                    background=dgray,
                ),

                widget.TextBox(
                    text=') ',
                    foreground=green,
                    background=dgray,
                ),

                widget.Spacer(
                   length=12,
                ),

                widget.TextBox(
                    text = ' ' + ChangeAudioDevice(True) + ' ',
                    name = 'AudioDeviceIndicator1',
                    background=dviolet,
                    foreground=black,
                    font = 'mononoki',
                ),

                widget.TextBox(
                    name = 'vol_level1',
                    text=' ' + vol1(device='else')[0],
                    background=dgray,
                    foreground=green,
                    font = 'Ubuntu Bold',
                    fontsize=12,
                ),

                widget.TextBox(
                    name = 'vol_rest1',
                    text=vol1(device='else')[1],
                    font = 'Ubuntu Bold',
                    fontsize=12,
                    foreground=black,
                    background=dgray,
                ),

                widget.TextBox(
                    text='(',
                    foreground=green,
                    background=dgray,
                ),

                widget.TextBox(
                    name='vol_number1',
                    text = vol1(device='else')[2]+'%',
                    foreground=violet,
                    background=dgray,
                ),

                widget.TextBox(
                    text=') ',
                    foreground=green,
                    background=dgray,
                ),

                widget.Spacer(
                   length=12,
                ),

                widget.TextBox(
                    text='  ',
                    font='mononoki',
                    fontsize=14,
                    background=dviolet,
                    foreground=black,
                ),

                widget.Clock(
                    foreground=green, 
                    background=dgray,
                    padding=0,
                    format=" %d.%m.'%y %a ",
                ),
                widget.Spacer(
                    length=bar_indent,
                ),

                widget.GenPollText(
                    func=network_current,
                    update_interval=2,
                ),
            ],    
            size=18)
    ),
    Screen(
        wallpaper='/mnt/hdd/zdjecia/wallpaper/cool.jpg',
        wallpaper_mode='fill',

        #TOP2
        top=bar.Bar(
            margin=[0, 0, 0, 0], #[N, E, S, W]
            background = '#000000.00',
            widgets=[

                widget.TextBox(
                    text = 'A',
                    font='Bartek',
                    fontsize = 25,
                    foreground=green,
                    background='#000000.00',
                    padding= -2,
                ),
                widget.TextBox(
                    text=' ',
                    font='mononoki',
                    fontsize=14,
                    foreground=black,
                    background=green,
                ),

                widget.Clock(
                    foreground=dgray, 
                    background=bar_color2,
                    padding=0,
                    format=" %H:%M:%S",
                ),
                widget.TextBox(
                    text = 'B',
                    font='Bartek',
                    fontsize = 25,
                    foreground=bar_color2,
                    background='#000000.00',
                    padding= -2,
                ),

                widget.Spacer(
                    length = 10,
                    background='#000000.00',
                ),

                widget.TextBox(
                    text = 'A',
                    font='Bartek',
                    fontsize = 25,
                    foreground=dviolet,
                    background='#000000.00',
                    padding= -2,
                ),

                widget.TextBox(
                    name='network_device2',
                    background=dviolet,
                    foreground=black,
                    font='Font Awesome 6 Free Solid',
                    fontsize=12,
                ),

                widget.TextBox(
                    text='Searching...',
                    name='network_name2',
                    foreground=dgray,
                    background=bar_color2,
                ),

                widget.TextBox(
                    text = 'B',
                    font='Bartek',
                    fontsize = 25,
                    foreground=bar_color2,
                    background='#000000.00',
                    padding= -2,
                ),
                
                widget.Spacer(
                    length = 10,
                    background='#000000.00',
                ),

                widget.TaskList(
                    parse_text=lambda text: ' ', 
                    borderwidth=0, 
                    margin_x=0, 
                    margin_y=0, 
                    icon_size=18, 
                    txt_floating='',
                    background=transp,
                ),

                widget.Spacer(
                    length = 15,
                    background='#000000.00',
                ),

                widget.TextBox(
                    text = 'A',
                    font='Bartek',
                    fontsize = 25,
                    foreground=bar_color,
                    background='#000000.00',
                    padding= -2,
                ),

                widget.GenPollText(
                    name = 'weather2',
                    func = wttr_pion,
                    foreground = dgray,
                    background = bar_color,
                    update_interval=600,
                ),
                widget.TextBox(
                    text = 'B',
                    font='Bartek',
                    fontsize = 25,
                    foreground=bar_color,
                    background='#000000.00',
                    padding= -2,
                ),

                widget.Spacer(
                    length = bar.STRETCH,
                    background='#000000.00',
                ),
                

                widget.TextBox(
                    text = 'A',
                    font='Bartek',
                    fontsize = 25,
                    foreground=bar_color,
                    background='#000000.00',
                    padding= -2,
                ),
                widget.GroupBox(
                    font='SauceCodePro NF', 
                    fontsize=14,
                    highlight_method='line', 
                    this_current_screen_border=violet, 
                    this_screen_border=violet,
                    block_highlight_text_color=green,
                    inactive=dgray,
                    active=dgray,
                    disable_drag=True,
                    use_mouse_wheel=False,
                    background = bar_color,
                ),

                widget.TextBox(
                    text = 'B',
                    font='Bartek',
                    fontsize = 25,
                    foreground=bar_color,
                    background='#000000.00',
                    padding= -2,
                ),

            ], 
            size=18
        ),

        #BOTTOM2
        bottom=bar.Bar(
            #margin=[0, 0, 0, 0], #[N, E, S, W]
            #background='#1b1919.90',
            background=transp,
            widgets=[
                widget.Spacer(
                    length=bar_indent,
                ),

                widget.TextBox(
                    text = 'C',
                    font='Bartek',
                    fontsize=30,
                    foreground=black,
                    background=dviolet,
                ),

                widget.TextBox(
                    text = ' ' + check_output('uname -r', shell=True, encoding='utf-8').split()[0] + ' ',
                    foreground=gray,
                    background=dgray,
                ),

                widget.Spacer(
                   length=12,
                ),

                widget.TextBox(
                    text='  ',
                    font='mononoki',
                    background=green,
                    foreground=black,
                ),

                widget.NvidiaSensors(
                    foreground=gray, 
                    background=dgray,
                    format=' {temp}°C {fan_speed} ',
                    update_interval = 1,
                    threshold=70,
                ),

                widget.Spacer(
                    length=bar.STRETCH,
                ),

                widget.TextBox(
                    text = '  ',
                    name = 'MicIcon2',
                    background=dviolet,
                    foreground=black,
                    font = 'mononoki',
                ),

                widget.TextBox(
                    name = 'mic_level2',
                    text=' ' + vol1(device='mic')[0],
                    background=dgray,
                    foreground=green,
                    font = 'Ubuntu Bold',
                    fontsize=12,
                ),

                widget.TextBox(
                    name = 'mic_rest2',
                    text=vol1(device='mic')[1],
                    font = 'Ubuntu Bold',
                    fontsize=12,
                    foreground=black,
                    background=dgray,
                ),

                widget.TextBox(
                    text='(',
                    foreground=green,
                    background=dgray,
                ),

                widget.TextBox(
                    name='mic_number2',
                    text = vol1(device='mic')[2]+'%',
                    foreground=violet,
                    background=dgray,
                ),

                widget.TextBox(
                    text=') ',
                    foreground=green,
                    background=dgray,
                ),

                widget.Spacer(
                   length=12,
                ),

                widget.TextBox(
                    text = ' ' + ChangeAudioDevice(True) + ' ',
                    name = 'AudioDeviceIndicator2',
                    background=dviolet,
                    foreground=black,
                    font='mononoki',
                ),

                widget.TextBox(
                    name = 'vol_level2',
                    text=' ' + vol1(device='else')[0],
                    background=dgray,
                    foreground=green,
                    font = 'Ubuntu Bold',
                    fontsize=12,
                ),

                widget.TextBox(
                    name = 'vol_rest2',
                    text=vol1(device='else')[1],
                    font = 'Ubuntu Bold',
                    fontsize=12,
                    foreground=black,
                    background=dgray,
                ),

                widget.TextBox(
                    text='(',
                    foreground=green,
                    background=dgray,
                ),

                widget.TextBox(
                    name='vol_number2',
                    text = vol1(device='else')[2]+'%',
                    foreground=violet,
                    background=dgray,
                ),

                widget.TextBox(
                    text=') ',
                    foreground=green,
                    background=dgray,
                ),

                widget.Spacer(
                   length=12,
                ),

                widget.TextBox(
                    text='  ',
                    font='mononoki',
                    fontsize=14,
                    background=dviolet,
                    foreground=black,
                ),

                widget.Clock(
                    foreground=green, 
                    background=dgray,
                    padding=0,
                    format=" %d.%m.'%y %a ",
                ),

                widget.Spacer(
                    length=bar_indent,
                ),

                widget.GenPollText(
                    func=network_current,
                    update_interval=2,
                ),
            ],    
            size=18)
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = True
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = False

wmname = "QTile"
