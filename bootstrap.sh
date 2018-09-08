#!/usr/bin/env bash
# Reference: https://stackoverflow.com/questions/7534184/git-alias-multiple-commands-and-parameters

pip3 install ginteract --user
git config --global alias.ch '!ginteract checkout'
git config --global alias.mg '!ginteract merge'
git config --global alias.dl '!ginteract delete'
