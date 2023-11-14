#!/bin/bash

count=0
echo "Skrip ini akan terus berjalan tanpa batas waktu."

while true; do
  ((count++))
  echo "Looping telah dijalankan sebanyak $count kali."
  aria2c -d /root/Downloads --max-connection-per-server=16 --console-log-level=error https://ash-speed.hetzner.com/100MB.bin 
  sleep 1
  rm -r /root/Downloads/* 
  sleep 1
  clear
  sleep 1
done
