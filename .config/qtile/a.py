from lib import *
from subprocess import check_output,run
status = check_output("xrandr --current --verbose | grep Brightness | awk 'FNR>1'", shell=True, encoding='utf-8')[13:-1]
print(status)
val = 1 + 0.15 * (status=='1.0')
print(val)
run("xrandr --output DP-4 --brightness %(new)f" % {'new': val}, shell=True, encoding='utf-8')



