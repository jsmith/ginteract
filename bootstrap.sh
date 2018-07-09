#!/usr/bin/env bash
# Reference: https://stackoverflow.com/questions/7534184/git-alias-multiple-commands-and-parameters

pip3 install gitcheckout
git config --global alias.ch '!gitcheckout checkout'
git config --global alias.mg '!gitcheckout merge'
git config --global alias.dl '!gitcheckout delete'
