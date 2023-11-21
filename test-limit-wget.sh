#!/bin/bash

counter=0

while true; do
    ((counter++))
    echo "Running the script for the $counter time(s)"
    
    rm -rf /root/download/*
    wget -P /root/download https://bit.ly/1GB-testfile
    rm -rf /root/download/*
    clear
    
    sleep 1  # Tunggu 1 detik sebelum mengulang
done
