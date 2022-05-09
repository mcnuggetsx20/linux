from lib import *
from subprocess import check_output,run
ind = int(check_output("qtile cmd-obj -o screen -f info | awk -F ', ' '{print $2}' | awk '{print $2}'", shell=True, encoding='utf-8')[:-1])

a = 1
b = 0
print(not a, not b)

