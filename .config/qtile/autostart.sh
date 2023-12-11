#!/bin/sh

 pulseaudio-equalizer enable

(pactl subscribe &) | (~/.config/qtile/audio &)

xinput --set-prop "Microsoft Microsoft® Nano Transceiver v2.0 Mouse" "Coordinate Transformation Matrix" 1.7 0 0 0 1.7 0 0 0 1

#xrdb ~/.config/xterm/hack
#xterm -e 'unimatrix -g=black -s 96' & sleep .8s && transset -n hack 0.5
#
#xrdb ~/.config/xterm/default

