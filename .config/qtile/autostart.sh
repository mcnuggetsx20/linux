#!/bin/sh

 pulseaudio-equalizer enable

(pactl subscribe &) | (~/.config/qtile/audio &)

#xrdb ~/.config/xterm/hack
#xterm -e 'unimatrix -g=black -s 96' & sleep .8s && transset -n hack 0.5
#
#xrdb ~/.config/xterm/default

