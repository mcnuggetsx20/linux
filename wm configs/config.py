#figlet
#                                             _            ____   ___  
# _ __ ___   ___ _ __  _   _  __ _  __ _  ___| |_ _____  _|___ \ / _ \ 
#| '_ ` _ \ / __| '_ \| | | |/ _` |/ _` |/ _ \ __/ __\ \/ / __) | | | |
#| | | | | | (__| | | | |_| | (_| | (_| |  __/ |_\__ \>  < / __/| |_| |
#|_| |_| |_|\___|_| |_|\__,_|\__, |\__, |\___|\__|___/_/\_\_____|\___/ 
#                            |___/ |___/                               

from typing import List  # noqa: F401
from libqtile import bar, layout, widget, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.command import lazy
import funx
from lib import *
import subprocess

mod = "mod1"
sup = "mod4"
terminal = "urxvt -lsp 4"

def vol1():
    com = subprocess.check_output('pamixer --get-volume', shell=True, encoding='utf-8').split()
    #   =====|----
    seg1 = (int(com[0]) // 15 -1) * '='
    return [seg1, com[0]]

def vol2():
    return (10 - len(vol1()[0]) - 1) * '-'

def volumechange(ok):
    def a(qtile):
        if ok:
            val = 5
        else:
            val = -5

        subprocess.run('pulsemixer --change-volume ' + str(val), shell=True) #change

        a = vol1()
        b = vol2()

        qtile.widgets_map['volumebox1'].update(a[0])
        qtile.widgets_map['volumebox2'].update(b)
        qtile.widgets_map['volumebox3'].update(a[1])

        qtile.widgets_map['volumebox12'].update(a[0])
        qtile.widgets_map['volumebox22'].update(b)
        qtile.widgets_map['volumebox32'].update(a[1])
    return a

def ChangeAudioDevice(init = False):
    global devices, device_indicators

    curr = ''.join(subprocess.check_output('pactl get-default-sink', shell=True, encoding='utf-8').split())

    if init:
        desired = devices[(devices.index(curr) + 1) * int(devices.index(curr) != len(devices)-1)]

        subprocess.run('pactl set-default-sink ' + desired, shell=True)

        a = vol1()
        b=vol2()

        qtile.widgets_map['volumebox1'].update(a[0])
        qtile.widgets_map['volumebox2'].update(b)
        qtile.widgets_map['AudioDeviceIndicator'].update(device_indicators[devices.index(desired)])

        qtile.widgets_map['volumebox12'].update(a[0])
        qtile.widgets_map['volumebox22'].update(b)
        qtile.widgets_map['AudioDeviceIndicator2'].update(device_indicators[devices.index(desired)])

    else:
        return str(device_indicators[devices.index(curr)])


keys = [
    #My stuff
    Key([sup], 'b', lazy.spawn('brave')),
    Key([mod], 'p', lazy.spawn('dmenu_run')),
    Key([sup], 'f', lazy.spawn('pcmanfm')),
    Key([sup], 'm', lazy.spawn('urxvt -e htop')),
    Key([mod], 'e', lazy.to_screen(0)),
    Key([mod], 'w', lazy.to_screen(1)),
    Key([sup], 'p', lazy.spawn('feh /mnt/hdd/zdjecia/plan_lekcji.png')),
    Key([sup], 'q', lazy.spawn('sh power_menu')),
    Key([sup], 'a', lazy.function(ChangeAudioDevice)),
    #Key([sup], 'y', lazy.function(test)),
    Key([mod, 'shift'], 's', lazy.spawn('sh /usr/bin/screenshot')),
    Key([sup],  'v', lazy.spawn('pavucontrol')),
    Key([],    'XF86AudioRaiseVolume', lazy.function(volumechange(True))),
    Key([],    'XF86AudioLowerVolume', lazy.function(volumechange(False))),
    Key([],    'XF86AudioMute', lazy.spawn('pulsemixer --toggle-mute')),
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

all_layouts = [
    layout.MonadTall(border_focus=colors['swamp'], border_width=2, single_border_width=0, margin=5, new_client_position='before_current'),
    layout.Columns(border_focus=colors['swamp'], border_normal='#000000',  border_width=2, margin=3, grow_amount=5, fair=True),
    layout.Matrix(border_focus='#F0AF16', border_width = 2, margin=5),
    layout.Max(border_width=0, border_focus='#000000'),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=6),
    # layout.Bsp(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(border_focus='#F0AF16'),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]
floating_layout = layout.Floating(border_width=0,float_rules=[
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
    Match(wm_class='Alacritty'),
])

groups = [
        Group(name='', position=1, layouts=all_layouts),
        Group(name='', position=2, layouts=all_layouts),
        Group(name='', position=3, layouts=all_layouts),
        Group(name='', position=4, layouts=all_layouts),
        Group(name='', position=5, layouts=all_layouts),
        Group(name='', position=6, layouts=[floating_layout], matches = [Match(wm_class='Steam'), Match(wm_class='csgo_linux64')]),
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

widget_defaults = dict(
    font='Ubuntu',
    fontsize=14,
    padding=1,
    inactive='#FFFFFF',
)
extension_defaults = widget_defaults.copy()

janek = [('system shutdown', 'shutdown now', 'calkiem niezle')]

screens = [
    Screen(
        bottom=bar.Bar(
            widgets=[
                widget.LaunchBar(
                    default_icon = '/home/mcnuggetsx20/.config/qtile/arch_icon_orange.png', 
                    progs=janek,
                ),

                widget.Spacer(
                    length=3,
                ),

                widget.GroupBox(
                    font='Font Awesome 5 Brand Bold', 
                    highlight_method='line', 
                    this_current_screen_border='#F0AF16', 
                    this_screen_border='#F0AF16',
                ),

                widget.TextBox(' | '),
                widget.TaskList(
                    parse_text=funx.remtext, 
                    borderwidth=0, 
                    margin_x=0, 
                    margin_y=0, 
                    icon_size=18, 
                    txt_floating='',
                ),

                widget.Spacer(
                    length=bar.STRETCH,
                ),

                widget.Systray(),
                widget.TextBox(' | '),
                widget.CPU(
                    background=colors['black'], 
                    foreground=colors['orange'], 
                    font='SauceCodePro NF Bold', 
                    format='CPU {load_percent}%', 
                    update_interval=1.0,
                ),

                widget.TextBox(
                    text = ' | ',
                    #foreground=colors['orange'],
                    ),

                widget.NvidiaSensors(
                    background=colors['black'], 
                    foreground=colors['orange'], 
                    font='SauceCodePro NF Bold', 
                    format='GPU {temp}°C',
                    update_interval = 4,
                ),

                widget.TextBox(
                    text = ' | ',
                    #foreground=colors['orange'],
                    ),

                widget.CurrentLayout(
                    background=colors['black'], 
                    foreground=colors['orange'], 
                    font='SauceCodePro NF Bold',
                ),

                widget.TextBox(
                        text = ' | ',
                ),

                widget.TextBox(
                        text = ChangeAudioDevice(False),
                        name = 'AudioDeviceIndicator',
                        foreground = colors['ored'],
                ),

                widget.TextBox(
                        name = 'volumebox1',
                        text=vol1()[0],
                        foreground=colors['swamp'],
                        font = 'mononoki',
                ),

                widget.TextBox(
                        foreground=colors['ored'],
                        font = 'mononoki',
                        text = '|',
                ),

                widget.TextBox(
                        name = 'volumebox2',
                        text=vol2(),
                        font = 'mononoki',
                        func = funx.vol2,
                ),

                widget.TextBox(
                        text='(',
                        foreground=colors['swamp'],
                        font='SauceCodePro NF Bold',
                ),

                widget.TextBox(
                        name='volumebox3',
                        text = vol1()[1],
                        font = 'SauceCodePro NF Bold',
                        foreground=colors['ored'],
                ),

                widget.TextBox(
                        text='%',
                        foreground=colors['ored'],
                        font='SauceCodePro NF Bold',
                ),

                widget.TextBox(
                        text=')',
                        foreground=colors['swamp'],
                        font='SauceCodePro NF Bold',
                ),


                widget.TextBox(
                        text = ' | ',
                ),

                widget.Clock(
                    BACKGround=colors['black'], 
                    foreground=colors['orange'], 
                    font='SauceCodePro NF Bold', 
                    padding=0,
                    format="%d.%m.'%y %a %H:%M:%S",
                ),
            ],    
            size=19)
    ),
    Screen(
        bottom=bar.Bar(
            widgets=[

                widget.LaunchBar(
                    default_icon = '/home/mcnuggetsx20/.config/qtile/arch_icon_orange.png', 
                    progs=janek,
                ),

                widget.Spacer(
                    length=3,
                ),

                widget.GroupBox(
                    font='Font Awesome 5 Brand Bold', 
                    highlight_method='line', 
                    this_current_screen_border='#F0AF16', 
                    this_screen_border='#F0AF16',
                ),

                widget.TextBox(' | '),
                widget.TaskList(
                    parse_text=funx.remtext, 
                    borderwidth=0, 
                    margin_x=0, 
                    margin_y=0, 
                    icon_size=18, 
                    txt_floating='',
                ),

                widget.Spacer(
                    length=bar.STRETCH,
                ),

                widget.NvidiaSensors(
                    background=colors['black'], 
                    foreground=colors['orange'], 
                    font='SauceCodePro NF Bold', 
                    format='GPU {temp}°C',
                    update_interval = 4,
                ),

                widget.TextBox(
                    text = ' | ',
                    #foreground=colors['orange'],
                    ),

                widget.CurrentLayout(
                    background=colors['black'], 
                    foreground=colors['orange'], 
                    font='SauceCodePro NF Bold',
                ),


                widget.TextBox(
                        text = ' | ',
                ),

                widget.TextBox(
                        text = ChangeAudioDevice(False),
                        name = 'AudioDeviceIndicator2',
                        foreground = colors['ored'],
                ),

                widget.TextBox(
                        name = 'volumebox12',
                        text=vol1()[0],
                        foreground=colors['swamp'],
                        font = 'mononoki',
                ),

                widget.TextBox(
                        foreground=colors['ored'],
                        font = 'mononoki',
                        text = '|',
                ),

                widget.TextBox(
                        name = 'volumebox22',
                        text=vol2(),
                        font = 'mononoki',
                        func = funx.vol2,
                ),

                widget.TextBox(
                        text='(',
                        foreground=colors['swamp'],
                        font='SauceCodePro NF Bold',
                ),

                widget.TextBox(
                        name='volumebox32',
                        text = vol1()[1],
                        font = 'SauceCodePro NF Bold',
                        foreground=colors['ored'],
                ),

                widget.TextBox(
                        text='%',
                        foreground=colors['ored'],
                        font='SauceCodePro NF Bold',
                ),

                widget.TextBox(
                        text=')',
                        foreground=colors['swamp'],
                        font='SauceCodePro NF Bold',
                ),


                widget.TextBox(
                        text = ' | ',
                ),

                widget.Clock(
                    background=colors['black'], 
                    foreground=colors['orange'], 
                    font='SauceCodePro NF Bold', 
                    format="%d.%m.'%y %a %H:%M:%S",
                ),
            ],    
            size = 19),

            #top=bar.Bar(widgets=[widget.TextBox(text='', background=colors['black'])], size=50),
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
