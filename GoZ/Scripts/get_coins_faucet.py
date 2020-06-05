import json
import os
import time
from datetime import datetime

#Config
source_chain_id = "regenchain-raul"
url = "file_chains.json"
log = "get_coins_faucet.log"


def get_coins():

	try: json_data=open(url)

	except:
		print ("Can not open file")
		result = 0
	else:
		chain = json.load(json_data)
		for lines in chain:
			chain_id = lines.get('chain-id')
			if chain_id != source_chain_id:
				print ("GETTING COINS FROM: " + chain_id)
				command = "rly testnets request " + chain_id 
				output = os.popen(command).read()
				print (output)
				file= open(log, "a+")
				file.write(output)
				file.close()

def write_file_chains():
	command2 = "rly chains  list  -j > " +  url
	output2 = os.popen(command2).read()

if __name__ == "__main__":
	write_file_chains()
	while 1==1:
		get_coins()
		print("Done!")
		time.sleep(301)  #(60*5+1)
