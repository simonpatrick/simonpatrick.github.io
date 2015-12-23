#!/bin/bash
ssh-keygen -t rsa -C "simonpatrick@163.com"
cat ~/.ssh/id_rsa.pub
eval ("$(ssh-agent -s)")
ssh-add ~/.ssh/id_rsa
pbcopy <~/.ssh/id_rsa.pub

