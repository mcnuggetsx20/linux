from subprocess import check_output, Popen

target = '/home/mcnuggetsx20/.config/qpanel/qnetwork/wifi_list'
lt = check_output("cat " + target, shell=True, encoding='utf-8').split('\n')[1:-1]
out = []

class network():
    def __init__(
            self,
            name=None,
            active=None,
    ):
        self.name=name
        self.active=active

for i in range(len(lt)):
    a = lt[i]
    lt[i] = (a[0] + 5*'-' + a[6::]).split('  ')
    lt[i] = network(name=lt[i][2], active=(lt[i][0][0]=='*'))
    if lt[i].name != '--':
        out.append([lt[i].name, int(lt[i].active)])
print(out)
