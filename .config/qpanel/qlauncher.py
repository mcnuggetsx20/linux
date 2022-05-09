from lib.all import *
from lib.ini import all_defaults
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
dred   = '#6b1015'
solar  = '#fdf6e3'

window_name='QLauncher' #you might want to specify the window name in order to create rules for multiple instances of QPanel in your window manager
geo=[10,0, 80, 18]

panel_background = dred 
panel_opacity = 0.9

def fireup(app): #runs the specified command
    def a():
        subprocess.run(app + ' &', shell=True)
    return a

all_defaults |= dict(
        bg_selected=green,
        )

#contents of the window
pages = {
    'page1':[
        pic(
            image = '/home/mcnuggetsx20/hdd/zdjecia/icons/discord.png',
            size=[18,18],
            pos=[7, 0],
            callback=fireup('discord'),
        ),

        pic(
            image = '/home/mcnuggetsx20/hdd/zdjecia/icons/icon_steam_vr.png',
            size=[18,18],
            pos=[32, 0],
            callback=fireup('steam'),
        ),

        pic(
            image = '/home/mcnuggetsx20/hdd/zdjecia/icons/brave_lion.svg',
            size=[18,18],
            pos=[57, 0],
            callback=fireup('brave'),
        ),
    ],
} 

ind = INDICATOR(
    pages=pages,
    pos=[150,580],
    countpos=[250, 580],
    #countfg=orange,
    text ='',
    fmt = '',
)

