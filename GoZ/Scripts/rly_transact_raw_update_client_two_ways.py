import random
import string
import json
import os
import time
from datetime import datetime

#Config 
source_chain_id = "regenchain-raul" #change.me
url = "paths.json"
log = "monitorize_paths.log"


def query_connections():
	try: json_data=open(url)

	except:
		print ("Can not open file")
		result = 0
	else:
		chain = json.load(json_data)

		for key, value in chain.items(): #iteritems():
			path = key
			src_chain_id = str(value["src"]["chain-id"])
			print (str(datetime.now()) + ' : Update PATH: ' + path)
			src_client_id = str(value["src"]["client-id"])
			dst_chain_id = str(value["dst"]["chain-id"])
			print (str(datetime.now()) + ' : >> SRC-CHAIN-ID: ' +  src_chain_id)
			print (str(datetime.now()) + ' : >> DST-CHAIN-ID: ' +  dst_chain_id)
			dst_client_id = str(value["dst"]["client-id"])
			print (str(datetime.now()) + ' : >> DST-CLIENT-ID: ' + dst_client_id)

			command = 'rly tx raw update-client ' + src_chain_id + ' ' + dst_chain_id + ' '+ src_client_id # + ' -d'
			command2 = 'rly tx raw update-client ' + dst_chain_id + ' ' + src_chain_id + ' '+ dst_client_id # + ' -d'
			list_commands = [command, command2]

			must_reset = 0
			for line in list_commands:
				output = os.popen(line).read()
				print (output)

				if output.find('"msg_index":0') == -1:
					must_reset = 1

			print (must_reset)
			if not must_reset: 
				message = str(datetime.now()) + ' : The PuLsE is flowing...\n'
				print (message)

			else:
				print("\nInitiating connection recovery\n")

				random_st = random_generator()
				recovery = 'rly l d ' + src_chain_id + ' && rly l d ' + dst_chain_id + ' && rly paths d ' + path + ' && rly pth gen ' + src_chain_id + ' transfer  ' + dst_chain_id +  ' transfer ' + random_st + ' -f && rly l i ' + src_chain_id + ' -f  && rly l i ' + dst_chain_id + ' -f && rly tx link ' + random_st 
				print ('Recovery commands >> ' +  recovery)

				output_recovery = os.popen(recovery).read()
				message = str(datetime.now()) + ' : ' + output + '\n' + output_recovery

			file= open(log, "a+")
			file.write(message )
			file.close()


def random_generator(size=10, chars=string.ascii_lowercase):
	return ''.join(random.choice(chars) for x in range(size))

def write_file_paths():
	command2 = "rly paths list  -j > " +  url
	output2 = os.popen(command2).read()



if __name__ == "__main__":
	while 1==1:
		write_file_paths()
		query_connections()
		print("\nDone! new update in 9 minutes")
		time.sleep(540)  #(60*9)
