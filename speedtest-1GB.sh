#!/bin/bash

download_speed_test() {
    start_time=$(date +%s.%N)
    curl -o /dev/null -s "$1"
    end_time=$(date +%s.%N)

    duration=$(echo "$end_time - $start_time" | bc)
    download_speed=$(echo "8 / $duration" | bc -l | awk '{printf "%.2f", $0}')
    echo "Kecepatan unduh: $download_speed Mbps"
}

# Ganti URL dengan file atau sumber daya yang ingin diunduh
download_url="https://bit.ly/1GB-testfile"

# Penghitung untuk penundaan
counter=0

while true; do
    download_speed_test "$download_url"
    ((counter++))

    if [ $((counter % 10)) -eq 0 ]; then
        echo -e "\n--- Menunggu 1 menit sebelum pengukuran berikutnya ---\n"
        sleep 60  # Menunggu 1 menit setiap 10 iterasi
    fi
done
