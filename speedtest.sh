count=0
while true; do
    speedtest
    sleep 2
    ((count++))
    if [ $count -eq 100 ]; then
        sleep 60
        count=0
    fi
done
