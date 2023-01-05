
devices = [
    "alsa_output.pci-0000_00_1f.3.analog-stereo",
    "alsa_output.pci-0000_01_00.1.hdmi-stereo",
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
        'Minecraft* 1.18.2 - Singleplayer' :   1.2,
        'Minecraft* 1.19.2 - Singleplayer' :   1.2,
        'Minecraft* 1.19.2 - Multiplayer (3rd-party Server)' :   1.2,
        'Counter-Strike: Global Offensive - OpenGL' :   1.9,
}

WALLPAPER = '/mnt/hdd/zdjecia/wallpaper/gory1.png'

curr_gamma = 1

comp = True
bars = True
walp = True
