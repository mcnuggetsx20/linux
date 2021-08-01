#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
#the first one is the default, the second one shows the whole directory
PS1='[\W]\$ '
#PS1='[\u@\h \w]$ '

alias monad='sudo urxvt -e vim ~/.xmonad/xmonad.hs &'
alias dwmconf='sudo vim ~/dwm-6.2/config.def.h'
alias qconf='sudo vim ~/.config/qtile/config.py'
alias mobar1='sudo urxvt -e vim ~/.xmonad/xmobar/xmobar.config'
alias mobar2='sudo urxvt -e vim ~/.xmonad/xmobar/xmobar2.hs'
alias gdr='cd /mnt/hdd/programming'
alias hdd='cd /mnt/hdd'
alias term='sudo urxvt -e vim ~/.Xresources'
alias l='ls -la'

function evim (){
    urxvt -e vim $1 &
}

function initx (){
    cat ~/wms/$1 > ~/.xinitrc
    startx
}
