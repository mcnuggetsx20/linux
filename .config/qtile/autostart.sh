#!/bin/sh

picom &

xrdb ~/.config/xterm/wttr
xterm -e wttr &
#killall trayer
#trayer --transparent true --alpha 256 --edge top --align right --widthtype pixel --width 100 --height 20 --margin 130 &

