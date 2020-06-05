import telegram_send #install https://pypi.org/project/telegram-send
import os
import time

def query_states():
	command = 'gaiacli q ibc client states --limit 1000 --chain-id=gameofzoneshub-1a --node tcp://35.233.155.199:26657 --output json | jq \'sort_by(.value.last_header.SignedHeader.header.chain_id) | .[] | .value.last_header.SignedHeader.header.chain_id + " - " + .value.last_header.SignedHeader.header.time\' | grep regengoz'
	output = os.popen(command).read()
	print(output)
	telegram_send.send(messages=[output])


if __name__ == "__main__":
	while 1==1:
		query_states()
		print("\nDone! new update in 60 minutes")
		time.sleep(3600)  #(60*60)
