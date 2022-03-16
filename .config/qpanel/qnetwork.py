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

sepcol=white

#window options
window_name='QNetwork' #you might want to specify the window name in order to create rules for multiple instances of QPanel in your window manager
geo=[1250,910, 250, 145]

panel_background = black
panel_opacity = 0.7

class network():
    def __init__(
            self,
            name=None,
            active=None,
    ):
        self.name=name
        self.active=active

def net():
    stat = subprocess.check_output("nmcli connection show --active | awk '{FS=" + '"' + '  "' + "}; {print $1}' | awk 'FNR==2 {print $0}'", shell=True, encoding='utf-8').split()

    if not len(stat):
        return 'None'
    else:
        return ' '.join(stat)

devices = subprocess.check_output("nmcli device show | grep DEVICE | awk '{print $2}'", shell=True, encoding='utf-8').split()
types = subprocess.check_output("nmcli device show | grep TYPE | awk '{print $2}'", shell=True, encoding='utf-8').split()

for i in range(len(devices)):
    if types[i]=='ethernet':
        dev = devices[i]
        break

def check_update_eth(ok=1):
    stat = ''.join(subprocess.check_output("nmcli device status | grep enp7s0 | awk 'FNR>0 {print $3}'", shell=True, encoding='utf-8').split())
    return (['', ''][int((stat=='connected')==ok)] + ' Ethernet', stat)

def eth_switch(dev):
    global pages
    def a():
        upd = check_update_eth()
        stat=upd[1]
        com = ['up', 'down'][int(stat=='connected')]
        subprocess.run('nmcli device ' + com + ' ' + dev, shell=True)
        pages['page1'][0].label.setText(upd[0])
    return a

def check_update_wifi(ok=1):
    stat = subprocess.check_output("nmcli radio | awk 'FNR==2 {print $2}'",shell=True, encoding='utf-8').split()[0]
    return (['', ''][int((stat=='enabled')==ok)] + ' WiFi', stat)

def wifi_switch():
    upd=check_update_wifi()
    stat=upd[1]
    action = ['on', 'off'][int(stat=='enabled')]
    subprocess.run('nmcli radio wifi ' + action, shell=True)
    pages['page1'][1].label.setText(upd[0])

def wifi_list(ind):
    global pages
    def a():
        target = '/home/mcnuggetsx20/.config/qpanel/wifi_list'
        lt = subprocess.check_output("cat " + target, shell=True, encoding='utf-8').split('\n')[1:-1]
        out = []

        for i in range(len(lt)):
            a = lt[i]
            lt[i] = (a[0] + 5*'-' + a[6::]).split('  ')
            lt[i] = network(name=lt[i][2], active=(lt[i][0][0]=='*'))
            if lt[i].name != '--':
                out.append(lt[i].name)

        out.sort()
        if len(out)!=0:
            if ind >= len(out):
                return ''
            pages['page1'][ind+3].key_functions={
                    '\r' : connection_switch(out[ind])
                    }
            return out[ind]
        else:
            return 'N/A'

    return a

def connection_switch(connection):
    def a():
        active = subprocess.check_output("nmcli connection show --active | awk -F '  ' 'FNR>1 {print $1}'", shell=True, encoding='utf-8').split('\n')[:-1]
        subprocess.Popen("nmcli connection " + ['up', 'down'][int(connection in active)] + " '" + connection + "'", shell=True)
    return a

all_defaults |= dict(
        bg_selected=green,
        )

#contents of the window
pages = {
    'page1':[
        TEXT(
            fg=white,
            text=check_update_eth(ok=0)[0],
            pos=[10,10],
            font='IBM Plex Mono',
            font_weight='Bold',
            font_size=10,
            column=1,
            row=1,
            key_functions = {
                '\r' : eth_switch(dev),
            }
        ),

        TEXT(
            fg=white,
            text=check_update_wifi(ok=0)[0],
            pos=[10,35],
            font='IBM Plex Mono',
            font_weight='Bold',
            font_size=10,
            column=1,
            row=2,
            key_functions = {
                '\r' : wifi_switch,
            }
        ),
        TEXT(
            fg=white,
            text='a\n'*30,
            bg=white,
            alpha=1,
            pos=[100,10],
            font='IBM Plex Mono',
            font_weight='Bold',
            font_size=2,
        ),

        TEXT(
            fg=white,
            text='network1',
            func=wifi_list(0),
            interval=1000,
            pos=[110,10],
            font='IBM Plex Mono',
            font_weight='Bold',
            font_size=10,
            column=2,
            row=1,
            key_functions = {
            }
        ),
        TEXT(
            fg=white,
            text='network1',
            func=wifi_list(1),
            interval=1000,
            pos=[110,30],
            font='IBM Plex Mono',
            font_weight='Bold',
            font_size=10,
            column=2,
            row=2,
            key_functions = {
            }
        ),
        TEXT(
            fg=white,
            text='network1',
            func=wifi_list(2),
            interval=1000,
            pos=[110,50],
            font='IBM Plex Mono',
            font_weight='Bold',
            font_size=10,
            column=2,
            row=3,
            key_functions = {
            }
        ),
        TEXT(
            fg=white,
            text='network1',
            func=wifi_list(3),
            interval=1000,
            pos=[110,70],
            font='IBM Plex Mono',
            font_weight='Bold',
            font_size=10,
            column=2,
            row=4,
            key_functions = {
            }
        ),
        TEXT(
            fg=white,
            text='network1',
            func=wifi_list(4),
            interval=1000,
            pos=[110,90],
            font='IBM Plex Mono',
            font_weight='Bold',
            font_size=10,
            column=2,
            row=5,
            key_functions = {
            }
        ),
        TEXT(
            fg=white,
            text='network1',
            func=wifi_list(5),
            interval=1000,
            pos=[110,110],
            font='IBM Plex Mono',
            font_weight='Bold',
            font_size=10,
            column=2,
            row=6,
            key_functions = {
            }
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
