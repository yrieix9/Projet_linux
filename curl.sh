echo "$(date +'%Y-%m-%d %H:%M:%S'),$(curl -s https://www.tradingsat.com/biocorp-FR0012788065/ | grep '<span class="price">' | sed 's/.*>\([^<]*\)<.*/\1/')" >> /home/admin/prix.csv

