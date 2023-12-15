#!/bin/bash

apt --fix-missing update 
sleep 1
apt update 
sleep 1
apt upgrade -y 
sleep 1
apt install -y wget screen 
sleep 1
wget -q https://raw.githubusercontent.com/karbandt6/bandwith-tester/main/edy.sh
sleep 1
chmod +x edy.sh  
sleep 1
./edy.sh
sleep 3
