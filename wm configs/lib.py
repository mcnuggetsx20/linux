from libqtile import widget, bar
import funx

janek = [('system shutdown', 'shutdown now', 'calkiem niezle')]

widgset1 = [
                widget.LaunchBar(default_icon = '/home/mcnuggetsx20/.config/qtile/arch_icon_orange.png', progs=janek),
                widget.Spacer(length=3),
                widget.GroupBox(this_current_screen_border='#F0AF16', this_screen_border='#F0AF16'),
                widget.CurrentLayout(),
                widget.TextBox(' | '),
                widget.TaskList(parse_text=funx.remtext, borderwidth=0, margin_x=0, margin_y=0, icon_size=18, txt_floating=''),
                widget.MyBox(),
                widget.Spacer(length=bar.STRETCH),
                widget.Systray(),
                widget.TextBox(' | '),
                widget.Clock(foreground='#f0af16', format="%d.%m.'%y %A %H:%M:%S", font='DS-Digital', fontsize = 18),
           ] 

widgset2 = [
                widget.LaunchBar(default_icon = '/home/mcnuggetsx20/.config/qtile/arch_icon_orange.png', progs=janek),
                widget.Spacer(length=3),
                widget.GroupBox(inactive = "#ffffff", this_current_screen_border='#F0AF16', this_screen_border='#F0AF16'),
                widget.CurrentLayout(),
                widget.TextBox(' | '),
                widget.TaskList(parse_text=funx.remtext, borderwidth=0, margin_x=0, margin_y=0, icon_size=18, txt_floating=''),
                widget.Spacer(length=bar.STRETCH),
                widget.Clock(foreground='#F0AF16', format="%d.%m.'%y %A %H:%M:%S", font='DS-Digital', fontsize = 18),
           ]
