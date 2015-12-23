#!/bin/bash

# set CDPATH
echo export CDPATH=/Users/patrick/workspace >>~/.bash_profile
echo export CDPATH=/Users/patrick/workspace >>~/.zshrc

# set alias
echo alias ..="cd .." >>~/.zshrc
echo alias ..2="cd ../.." >>~/.zshrc
echo alias ..3="cd ../../.." >>~/.zshrc
echo alias ..4="cd ../../../.." >>~/.zshrc
echo alias ..5="cd ../../../../../" >>~/.zshrc
# homestead configuration
echo alias inithomestead=""sh /Users/patrick/VirtualBox VMs/Homestead/init.sh"" >>$HOME/.zshrc
echo alias edithomestead=""mvim /Users/patrick/.homestead/Homestead.yaml"" >>$HOME/.zshrc

