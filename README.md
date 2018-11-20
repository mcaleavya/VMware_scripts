# Initial placeholder
### csvtoflare.py -- script to map CSV format for VSAN to D3.js flare.json format.
### nstat.awk -- parse output from net-stats command 
``net-stats -A -tc -i 1 -n 300 | sed 's/["|":|:|/|,]//g' |awk -f ./nstat.awk``
