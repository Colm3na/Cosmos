import json
import os
import time
from datetime import datetime

#Config
source_chain_id = "regenchain-raul"
coin_amount = "100"
coin_denom = "utree"
url = "file_chains.json"
log = "send_coins.log"


def send_coins():

	try: json_data=open(url)

	except:
		print ("Can not open file")
		result = 0
	else:
		chain = json.load(json_data)
		for lines in chain:
			chain_id = lines.get('chain-id')
			if chain_id != source_chain_id:
				print ("SENDING COINS TO: " + chain_id)
				command = "rly tx transfer " + source_chain_id + " " + chain_id + " " + coin_amount + coin_denom + " true $(rly ch addr " + chain_id + ")"
				output = os.popen(command).read()
				print (output)
				file= open(log, "a+")
				file.write(output)
				file.close()

def write_file_chains():
	command2 = "rly chains  list  -j > " +  url
	output2 = os.popen(command2).read()

if __name__ == "__main__":
	write_file_chains()  #List all chains configured in Relayer
	while 1==1:
		send_coins() #Send coins to all fetched chains
		print("Done!")
		#time.sleep(540)  #(60*9)
