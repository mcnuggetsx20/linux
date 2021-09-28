from libqtile import widget, bar
import funx

colors = {
        'orange' : '#F0Af16',
        'ored'   : '#F77B53',
        'black'  : '#000000',
        'swamp'  : '#335D03',  
        'lime'   : '#32CD32',
        }

janek = [('system shutdown', 'shutdown now', 'calkiem niezle')]

widgset1 = [
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
                    update_interval=3.0,
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
                        text = ' ',
                        foreground = colors['ored'],
                ),

                widget.GenPollText(
                        foreground=colors['swamp'],
                        font = 'mononoki',
                        func = funx.vol1,
                        update_interval = 1.5,
                ),

                widget.TextBox(
                        foreground=colors['ored'],
                        font = 'mononoki',
                        text = '|',
                ),

                widget.GenPollText(
                        font = 'mononoki',
                        func = funx.vol2,
                        update_interval = 1.5,
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
           ] 

widgset2 = [
                widget.LaunchBar(default_icon = '/home/mcnuggetsx20/.config/qtile/arch_icon_orange.png', progs=janek),
                widget.Spacer(length=3),
                widget.GroupBox(font='Font Awesome 5 Brands Bold', highlight_method='line', this_current_screen_border='#F0AF16', this_screen_border='#F0AF16'),
                widget.TextBox(' | '),
                widget.TaskList(parse_text=funx.remtext, borderwidth=0, margin_x=0, margin_y=0, icon_size=18, txt_floating=''),
                widget.Spacer(length=bar.STRETCH),
                widget.CurrentLayout(background=colors['orange'], foreground=colors['black'], font='SauceCodePro NF Bold'),
                widget.TextBox(' '),
                widget.Clock(background=colors['orange'], foreground=colors['black'], font='SauceCodePro NF Bold', format="%d.%m.'%y %a %H:%M:%S"),
           ]
