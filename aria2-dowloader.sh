#!/bin/bash

count=0
while [ $count -lt 5 ]; do
  aria2c -d /root/Downloads --max-connection-per-server=16 https://bit.ly/1GB-testfile && rm -r /root/Downloads/* && clear
  sleep 1
  ((count++))
done
