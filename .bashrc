#
# ~/.bashrc
#

# If not running interactively, don't do anything
GREEN="\[$(tput setaf 2)\]"
PURPLE="\[$(tput setaf 6)\]"
RED="\e[31m"
RESET="\[$(tput sgr0)\]"
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
#the first one is the default, the second one shows the whole directory
#ZEBY BYL TYLKO TEN JEDEN FOLDER TO MUSI BYC W (DUZE)

PS1="[${PURPLE}\e[1m\u${RESET} \w]: ${GREEN}\t${RESET}\n${GREEN} >$ ${RESET}"
#PS1="[\u \w]`printf "%${COLUMNS}s" "\t" `$PS1"
#PS1="[\w]${GREEN}$ ${RESET}"
#PS1='[\u@\h \w]$ '

#set -o vi

alias qconf='nv ~/.config/qtile/config.py'
alias gdr='cd /mnt/hdd/programming'
alias hdd='cd /mnt/hdd'
alias term='sudo vim ~/.Xresources'
alias l='exa --group-directories-first --icons -lagBh'
alias pacinstall='sudo pacman -S'
alias pacclear='sudo pacman -Scc'
alias pacremove='sudo pacman -Rns'
alias pacrefresh='sudo pacman -Syy'
alias pacupgrade='configpush; sudo pacman -Syyu'
alias oi='cd ~/hdd/programming/oi_2021'
alias pconf='gvim /home/mcnuggetsx20/.config/qpanel/panelrc.py'
alias pcom='nv ~/.config/picom/picom.conf &'
alias urxvt='urxvt -lsp 4'
alias pb='python -B'
alias lf='lfub'
alias cd='nvim_autocd'
alias nv='internal_nvim'
alias search='sudo find / -path /mnt/hdd -prune -iname'

alias nvidia-settings='nvidia-settings --config="$XDG_CONFIG_HOME"/nvidia/settings'

bind "set completion-ignore-case on"

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
