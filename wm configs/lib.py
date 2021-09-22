from libqtile import widget, bar
import funx

colors = {
        'orange' : '#F0Af16',
        'black'  : '#000000',
        }

janek = [('system shutdown', 'shutdown now', 'calkiem niezle')]

widgset1 = [
                widget.LaunchBar(default_icon = '/home/mcnuggetsx20/.config/qtile/arch_icon_orange.png', progs=janek),
                widget.Spacer(length=3),
                widget.GroupBox(highlight_method='line', this_current_screen_border='#F0AF16', this_screen_border='#F0AF16'),
                widget.TextBox(' | '),
                widget.TaskList(parse_text=funx.remtext, borderwidth=0, margin_x=0, margin_y=0, icon_size=18, txt_floating=''),
                widget.Spacer(length=bar.STRETCH),
                widget.Systray(),
                widget.TextBox(' | '),
                widget.CPU(background=colors['orange'], foreground=colors['black'], font='SauceCodePro NF Bold', format='CPU {load_percent}%', update_interval=2.0),
                widget.TextBox(' '),
                widget.NvidiaSensors(background=colors['orange'], foreground=colors['black'], font='SauceCodePro NF Bold', format='GPU {temp}°C'),
                widget.TextBox(' '),
                widget.CurrentLayout(background=colors['orange'], foreground=colors['black'], font='SauceCodePro NF Bold'),
                widget.TextBox(' '),
                widget.Clock(background=colors['orange'], foreground=colors['black'], font='SauceCodePro NF Bold', format="%d.%m.'%y %a %H:%M:%S"),
           ] 

widgset2 = [
                widget.LaunchBar(default_icon = '/home/mcnuggetsx20/.config/qtile/arch_icon_orange.png', progs=janek),
                widget.Spacer(length=3),
                widget.GroupBox(highlight_method='line', this_current_screen_border='#F0AF16', this_screen_border='#F0AF16'),
                widget.TextBox(' | '),
                widget.TaskList(parse_text=funx.remtext, borderwidth=0, margin_x=0, margin_y=0, icon_size=18, txt_floating=''),
                widget.Spacer(length=bar.STRETCH),
                widget.CurrentLayout(background=colors['orange'], foreground=colors['black'], font='SauceCodePro NF Bold'),
                widget.TextBox(' '),
                widget.Clock(background=colors['orange'], foreground=colors['black'], font='SauceCodePro NF Bold', format="%d.%m.'%y %a %H:%M:%S"),
           ]
