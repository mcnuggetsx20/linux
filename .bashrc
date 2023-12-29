#
# ~/.bashrc
#

# If not running interactively, don't do anything

export GITHUB_API_TOKEN=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
export PATH="$PATH:/home/mcnuggetsx20/.local/bin"

GREEN="\[$(tput setaf 2)\]"
YELLOW="\[$(tput setaf 3)\]"
BLUE="\[$(tput setaf 4)\]"
ORANGE="\[$(tput setaf 9)\]"
RED="\e[31m"
RESET="\[$(tput sgr0)\]"
[[ $- != *i* ]] && return

COLUMNS=$(tput cols)

alias ls='ls --color=auto'
#the first one is the default, the second one shows the whole directory
#ZEBY BYL TYLKO TEN JEDEN FOLDER TO MUSI BYC W (DUZE)

PS1="[${ORANGE}\e[1m\u${RESET} \w]: ${BLUE}\t${RESET}\n${ORANGE} >$ ${RESET}"
#PS1="[\u \w]`printf "%${COLUMNS}s" "\t" `$PS1"
#PS1="[\w]${GREEN}$ ${RESET}"
#PS1='[\u@\h \w]$ '

#set -o vi

alias qconf='nv ~/.config/qtile/config.py'
alias uconf='nv ~/.config/qtile/res_config'
alias gdr='cd /mnt/hdd/programming'
alias hdd='cd /mnt/hdd'
alias term='sudo vim ~/.Xresources'
alias l='exa --group-directories-first --icons -lagBh'
alias pacinstall='sudo pacman -S'
alias pacclear='echo y | sudo pacman -Scc; sudo pacman -Scc --noconfirm'
alias pacremove='sudo pacman -Rns'
alias pacrefresh='sudo pacman -Syy'
alias pacupgrade='configpush; sudo pacman -Syyu --noconfirm; sudo pacman -Scc --noconfirm; echo y | sudo pacman -Scc; echo; speed'
alias oi='cd ~/hdd/programming/oi_2021'
alias pconf='gvim /home/mcnuggetsx20/.config/qpanel/panelrc.py'
alias pcom='nv ~/.config/picom/picom.conf &'
alias urxvt='urxvt -lsp 4'
alias pb='python -B'
alias lf='lfub'
alias cd='nvim_autocd'
alias vim='internal_nvim'
alias nv='internal_nvim'
alias lookfor='sudo find / -path /mnt/hdd -prune -iname'
#alias setCover='eyeD3 --add-image $2:FRONT_COVER:front $1' #SONG / IMAGE
alias kanter='nv /mnt/b/SteamLibrary/steamapps/common/Counter-Strike\ Global\ Offensive/game/csgo/cfg/autoexec.cfg'
alias take='_take'
#alias picom='/mnt/hdd/Program-Files/picom-pij/build/src/start'
alias mk='gcc -o main main.c -lX11 -Wextra -Wall'
#alias usbstick='dd bs=4M if=$1 of=$2 conv=fsync oflag=direct status=progress' #iso / device
alias nvidia-settings='nvidia-settings --config="$XDG_CONFIG_HOME"/nvidia/settings'
alias fetch='fastfetch'
alias speed='xset r rate 200 90'
alias discord='/mnt/hdd/Program-Files/discord_linux/Discord/Discord'

bind "set completion-ignore-case on"

function gitpush(){
    DATE=$(date "+%d %b %Y %H:%M:%S")
    git add -A
    git commit -m "${DATE}"
    git push
}

function usbstick (){
    dd bs=4M if=${1} of=${2} conv=fsync oflag=direct status=progress
}

function evim (){
    urxvt -e vim $1 &
}

function initx (){
    cat ~/wms/$1 > ~/.xinitrc
    startx
}

function brightness(){
    xrandr --output DP-4 --brightness $1
    xrandr --output HDMI-0 --brightness $1
}

nvim_autocd(){
    builtin cd "$@"
    if [ -v NVIM ]; then
        (nvim_client_python -cd &) > /dev/null
    fi
}

internal_nvim(){
    if [ -v NVIM ]; then
        (nvim_client_python -c "tabnew $1" &) > /dev/null
    fi
}

_take(){
    mkdir "$@"
    cd "$@"
}

