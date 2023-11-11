count=0
while :; do
    sleep 2
    speedtest-cli --no-upload
    ((count++))
    if [ $count -eq 100 ]; then
        sleep 60
        count=0
    fi
done
