#!/bin/bash
################################################
#                                              #
#  Made with love in Colm3naSVQ by :           #
#                                              #
#  @wimel85(wiπΞl)->@cosmaut:matrix.org        #
#  @DerFredy -> @derfredy:matrix.org           #                              
#                                              #
################################################

# ./check_default.sh [ ip_list.txt ]
# Read all IPs line to line 

ip_list=()
port=26657

while read -r ip || [[ -n "$ip" ]]; do
	ip_list+=($ip)
done < $1 

for ip in ${ip_list[@]}
do
	nmap -p $port -oG - $ip | grep --color=always -P "(?<=/)([[:lower:]]+)(?=/tcp/{5})"
done
