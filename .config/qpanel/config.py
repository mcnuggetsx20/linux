from lib.all import *
import subprocess

#colors
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


#window options
window_name='QPanel' #you might want to specify the window name in order to create rules for multiple instances of QPanel in your window manager
geo=[1610,240,300,600]

panel_background = dgray
panel_opacity = 0.7
key_functions={}

def check_space():
    return subprocess.check_output('df -h | grep nvme', shell=True, encoding='utf-8').split()[2]

def fireup(app): #runs the specified command
    def a():
        subprocess.run(app + ' &', shell=True)
    return a

#contents of the window
pages = {
    'page1':[
        CLOCK(
            interval=200,
            font='Ubuntu Mono',
            font_weight='Bold',
            font_size=22,
            fg=orange,
            pos=[95, 0],
            fmt='%H:%M:%S',
        ),
        CLOCK(
            font='Ubuntu Mono',
            font_weight='Bold',
            font_size=12,
            fg=ored,
            pos=[45, 30],
            fmt='%A, %B %-d %Y',
        ),

        #CPU(
        #    interval=2000,
        #    font='Ibm Plex Mono',
        #    font_weight='Bold',
        #    font_size=12,
        #    fg=gray,
        #    pos=[5, 90],
        #    fmt='$percent',
        #    cores=[1,2,3,4,5,6],
        #),

#        TEXT(
#            font='Ibm Plex Mono',
#            font_weight='Bold',
#            font_size=12,
#            text='USED: ',
#            pos=[5, 120],
#            fg=gray,
#            underline=TEXT(
#                alpha=1,
#                pos =[5,138],
#                size=[420, 2],
#                bg=violet,
#            ),
#
#        ),
#
#        TEXT(
#            font='Ibm Plex Mono',
#            font_weight='Bold',
#            font_size=12,
#            interval=1000,
#            func=check_space,
#            fg=gray,
#            pos=[58,120],
#            underline=TEXT(
#                alpha=1,
#                pos =[58,138],
#                size=[420, 2],
#                bg=violet,
#            ),
#        ),

    ],
    'page2':[
        TEXT(
            font='Ubuntu Mono',
            font_weight='Bold',
            font_size=22,
            text='Cool Apps',
            pos=[85,0],
            fg=orange,
            underline=TEXT(
                alpha=1,
                bg=ored,
                size=[1,2],
                pos=[85, 30],
            ),
        ),
        pic(
            image='/home/mcnuggetsx20/hdd/zdjecia/icons/kolourpaint.svg',
            size=[32,32],
            pos=[5,55],
            callback=fireup('kolourpaint'),
        ),  
        TEXT(
            text='KolourPaint',
            font='Ubuntu Mono',
            font_weight='Bold',
            font_size=12,
            pos=[40, 65],
            fg=lime,
        ),

        pic(
            image='/home/mcnuggetsx20/hdd/zdjecia/icons/asunder.svg',
            size=[32,32],
            pos=[5,95],
            callback=fireup('asunder'),
        ),  
        TEXT(
            text='Asunder',
            font='Ubuntu Mono',
            font_weight='Bold',
            font_size=12,
            pos=[40, 105],
            fg=red,
        ),

        pic(
            image='/home/mcnuggetsx20/hdd/zdjecia/icons/steam_blue.svg',
            size=[30,30],
            pos=[5,135],
            callback=fireup('steam'),
        ),  
        TEXT(
            text='Steam',
            font='Ubuntu Mono',
            font_weight='Bold',
            font_size=12,
            pos=[40, 145],
            fg=dblue,
        ),
    ],
} 

ind = INDICATOR(
        pages=pages,
        pos=[150,580],
        countpos=[250, 580],
        countfg=orange,
        text ='@',
        fmt = '[$current/$max]',
    )
