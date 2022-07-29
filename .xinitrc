xset s off
xset s 0 0
xset -dpms
xset r rate 200 90
nvidia-settings --load-config-only &
nvidia-settings -a "[gpu:0]/GPUFanControlState=1" -a "[fan:0]/GPUTargetFanSpeed=55"
/usr/bin/qtile start
