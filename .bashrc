#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
#the first one is the default, the second one shows the whole directory
PS1='[\u@\h \W]\$ '
#PS1='[\u@\h \w]$ '

alias monad='evim ~/.xmonad/xmonad.hs'
alias mobar='evim ~/.xmonad/xmobar/xmobar.config'
alias gdr='cd /mnt/hdd/programming'
alias term='evim ~/.Xresources'
alias l='ls -la'

function evim (){
    urxvt -e vim $1 &
}
