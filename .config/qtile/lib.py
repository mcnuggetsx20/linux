
sinks = [
    "ladspa_output.mbeq_1197.mbeq",
    "alsa_output.pci-0000_00_1f.3.analog-stereo",
]

ports = [
    "analog-output-lineout",
    "analog-output-headphones",
]

mic = 'alsa_input.usb-C-Media_Electronics_Inc._USB_PnP_Sound_Device-00.mono-fallback' 

device_indicators = ['', '', '']

network_devices={
        'ethernet' : 'I',
        'wireless'     : 'H',
        'None'     : 'J',
        }

colors = {
        'orange' : '#F0Af16',
        'ored'   : '#F77B53',
        'black'  : '#000000',
        'swamp'  : '#335D03',  
        'lime'   : '#32CD32',
        }


gamma_rules={
        'Counter-Strike: Global Offensive - OpenGL' :   1.4,
        'League of Legends (TM) Client':    1.0,
}

gamma_classes={
        'Minecraft' : 1.2,
}

WALLPAPER1 = '/mnt/hdd/zdjecia/wallpaper/cieszyn.png'
WALLPAPER2 = '/mnt/hdd/zdjecia/wallpaper/jager.png'

curr_gamma = 1

comp = True
bars = True
walp = True

RES_CUSTOM = '2560x1440'
RES_NORMAL = '3440x1440'
SCALE = False

RES_SECONDARY = '1920x1080'

RES = True
#RES_CUSTOM = f'nvidia-settings -a CurrentMetaMode="DP-4: 3440x1440_100 @{RES_CUSTOM} +0+0 {{ViewPortIn={RES_CUSTOM}, ViewPortOut={[RES_CUSTOM, RES_NORMAL][SCALE]}+0+0, ForceCompositionPipeline=Off, ForceFullCompositionPipeline=Off}}"'
#RES_NORMAL = 'nvidia-settings -a CurrentMetaMode="DP-4: 3440x1440_100 @3440x1440 +0+0 {ViewPortIn=3440x1440, ViewPortOut=3440x1440+0+0, ForceCompositionPipeline=On, ForceFullCompositionPipeline=On}"'
RES_SECONDARY= f'xrandr --output HDMI-0 --mode {RES_SECONDARY} --rate 75 --right-of DP-4 --rotate left'
#RES_SECONDARY=f'xrandr --output HDMI-0 --off'
DPI_COMMAND = 'xrandr --dpi 96'

class config_class():
    def __init__(self):
        return

