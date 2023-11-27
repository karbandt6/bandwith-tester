#!/bin/bash

for i in {1..5}; do
    screen -dmS bw$i bash -c "
        counter=0
        download_path=/root/download/$i

        while true; do
            ((counter++))
            echo \"Running the script for the \$counter time(s) in session bw$i\"

            rm -rf \$download_path/*
            wget -P \$download_path https://bandwidth-tester.biz.id/
            rm -rf \$download_path/*
            clear

            sleep 1  
        done
    "
done
