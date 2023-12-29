xset s off
xset s 0 0
xset -dpms
xset r rate 200 90

nvidia-settings --load-config-only &
nvidia-settings -a "[gpu:0]/GPUFanControlState=1" -a "[fan:0]/GPUTargetFanSpeed=55"

xrandr --output DP-4 --mode 3440x1440 --rate 100 --primary
xrandr --output HDMI-0 --mode 1920x1080 --rate 75 --right-of DP-4 --rotate left
xrandr --dpi 96

xsetwacom --set "HUION Huion Tablet Pad pad" MapToOutput 1080x1920+3440+0
xsetwacom --set "HUION Huion Tablet Pen stylus" MapToOutput 1080x1920+3440+0
xsetwacom --set "HUION Huion Tablet Pen stylus" Rotate CW

xrdb ~/.Xresources

/usr/bin/qtile start

