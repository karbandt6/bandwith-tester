# PowerShell Script

# Mengunduh file tar.gz
Invoke-WebRequest -Uri "https://assets.coreservice.io/public/package/59/app-market-gaga-pro/1.0.4/app-market-gaga-pro-1_0_4.tar.gz" -OutFile "apphub-windows-amd64.tar.gz"

# Ekstrak file tar.gz
tar -zxf apphub-windows-amd64.tar.gz

# Menghapus file tar.gz setelah diekstrak
Remove-Item -Path "apphub-windows-amd64.tar.gz" -Force

# Pindah ke direktori apphub-windows-amd64
Set-Location -Path ".\apphub-windows-amd64"

# Menginstal layanan apphub
Start-Process -FilePath ".\apphub.exe" -ArgumentList "service install" -Wait

# Menunggu 5 detik
Start-Sleep -Seconds 5

# Memulai layanan apphub
Start-Process -FilePath ".\apphub.exe" -ArgumentList "service start" -Wait

# Menunggu 10 detik
Start-Sleep -Seconds 10

# Menampilkan status apphub
Start-Process -FilePath ".\apphub.exe" -ArgumentList "status" -Wait

# Menunggu 5 detik
Start-Sleep -Seconds 5

# Mengatur konfigurasi gaganode.exe dengan token
Start-Process -FilePath ".\apps\gaganode\gaganode.exe" -ArgumentList "config set --token=fzucgoekdmybuibb0b0fddf169d85d47" -Wait

# Menampilkan status apphub setelah konfigurasi
Start-Process -FilePath ".\apphub.exe" -ArgumentList "status" -Wait
