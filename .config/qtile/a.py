from lib import *
def findClass(_class):
    for i in gamma_classes:
        if i in _class: return gamma_classes[i]
    return 0
_class = "Minecraft* 1.19.2"
print(findClass(_class))
