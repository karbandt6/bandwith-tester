#!/bin/bash

# Take the number of screens as input
read -p "Enter the number of screens: " num_screens

for ((i = 1; i <= num_screens; i++)); do
    screen -dmS bw$i bash -c "
        counter=0
        download_path=/root/download/$i

        while true; do
            ((counter++))
            echo \"Running the script for the \$counter time(s) in session bw$i\"

            rm -rf \$download_path/*
            wget -P \$download_path https://bin.kartolo.cloud/100MB.bin
            rm -rf \$download_path/*
            clear

            sleep 1  # Wait for 1 second before repeating
        done
    "
done
