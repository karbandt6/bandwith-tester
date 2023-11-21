count=0
while true; do
    speedtest --server-id=12807
    sleep 2
    ((count++))
    if [ $count -eq 100 ]; then
        sleep 60
        count=0
    fi
done
