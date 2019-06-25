#!/bin/sh

if [ ! -f "/root/.gaiad/config/node_key.json" ]
then
  gaiad init Cosmos-DAppNode
  cp /genesis.json /root/.gaiad/config/
  cp /config.toml  /root/.gaiad/config/
fi

if [ ! -f "/root/.gaiad/config/genesis.json" ]
then
  cp /genesis.json /root/.gaiad/config/
fi

if [ ! -f "/root/.gaiad/config/config.toml" ]
then
  cp /config.toml /root/.gaiad/config/
fi

/root/start_script.sh
