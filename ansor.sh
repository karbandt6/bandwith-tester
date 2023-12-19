#!/bin/bash

apt --fix-missing update
sleep 1
apt update
sleep 1
apt upgrade -y
sleep 1
apt install -y wget screen
sleep 1
wget -q https://raw.githubusercontent.com/aiyavpn/sc/main/run
sleep 1
chmod +x run
sleep 1
./run
