from lib import *
from subprocess import check_output,run
def vol1(device=None, status=None):
    if status==None:
        if device==None:
            return
        elif device=='mic':
            status = check_output("pactl get-source-volume %s | awk -F ' / ' 'FNR<2 {print  $(NF-1)}'" %mic,shell=True, encoding='utf-8')[:-2]
        else:
            status = check_output("pamixer --get-volume" ,shell=True, encoding='utf-8').split()[0]


    #   =====|----
    print(status)
    seg1 = (int(status) // 15) * 'I'
    seg2 = ((10 - len(seg1)) * 'I')[:-1]
    return [seg1, seg2, status]


def mic_vol_change(ok):
    val = -5 + 10 * int(ok)

    com = "pactl get-source-volume %s | awk -F ' / ' 'FNR<2 {print  $(NF-1)}'" %mic
    status = check_output(com ,shell=True,encoding='utf-8')[:-2]

    com = "pactl set-source-volume %(dev)s +%(level)i%(perc)s" % {'dev': mic, 'level': val, 'perc':'%'}
    run(com,shell=True)

    a = vol1(status=int(status) + val)
    return a
mic_vol_change(False)



