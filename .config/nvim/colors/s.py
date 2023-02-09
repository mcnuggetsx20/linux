file = open('custom.vim','r').read().split('\n')[:-1]
file = [i.split() for i in file]

for v, i in enumerate(file):
    if 'links' not in i: continue

    temp= ['hi', 'link']
    temp.append(i[1])
    temp.append(i[-1])
    file[v] = temp

for i in file:
    print(*i)


