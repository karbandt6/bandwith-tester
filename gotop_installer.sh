#!/bin/bash

wget https://github.com/cjbassi/gotop/releases/download/3.0.0/gotop_3.0.0_linux_amd64.deb
sleep 1
dpkg -i gotop_3.0.0_linux_amd64.deb
sleep 1
gotop
