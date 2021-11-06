import os

def remtext(text):
    return ''

def vol1(qtile):
    com = os.popen('pamixer --get-volume').read().split()
    #   =====|----
    seg1 = (int(com[0]) // 15 -1) * '='
    #qtile.widgets_map['volumebox2'].update(seg1)
    return seg1

def vol2(qtile):
    #qtile.widgets_map['volumebox2'].update((10 - len(vol1()) - 1) * '-')
    return (10 - len(vol1()) - 1) * '-'


