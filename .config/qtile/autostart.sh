#!/bin/sh

picom &

xrdb ~/.config/xterm/wttr_today
xterm -e "mywatch curl -s wttr.in/Wojnów?4 | awk 'FNR < 39'" &
#killall trayer
#trayer --transparent true --alpha 256 --edge top --align right --widthtype pixel --width 100 --height 20 --margin 130 &

