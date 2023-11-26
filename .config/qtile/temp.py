from lib import *

def findClass(name):
    for i in gamma_classes:
        if i in name: return gamma_classes[i]
    return False

print(findClass('Minecraft 1.20.2 - Singleplayer'))
