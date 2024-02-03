#!/bin/bash

# Mengunduh file tar.gz
wget -O apphub-windows-amd64.tar.gz "https://assets.coreservice.io/public/package/59/app-market-gaga-pro/1.0.4/app-market-gaga-pro-1_0_4.tar.gz"

# Ekstrak file tar.gz
tar -zxf apphub-windows-amd64.tar.gz

# Menghapus file tar.gz setelah diekstrak
rm -f apphub-windows-amd64.tar.gz

# Pindah ke direktori apphub-windows-amd64
cd ./apphub-windows-amd64

# Menginstal layanan apphub
./apphub.exe service install

# Menunggu 5 detik
sleep 5

# Memulai layanan apphub
./apphub.exe service start

# Menunggu 10 detik
sleep 10

# Menampilkan status apphub
./apphub.exe status

# Menunggu 5 detik
sleep 5

# Mengatur konfigurasi gaganode.exe dengan token
./apps/gaganode/gaganode.exe config set --token=fzucgoekdmybuibb0b0fddf169d85d47

# Menampilkan status apphub setelah konfigurasi
./apphub.exe status
