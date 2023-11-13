#!/bin/bash

count=0
while [ $count -lt 5 ]; do
  aria2c -d /root/Downloads --max-connection-per-server=16 https://bit.ly/1GB-testfile 
  sleep 1
  rm -r /root/Downloads/* 
  sleep 1
  clear
  sleep 1
  ((count++))
done
