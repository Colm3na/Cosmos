#!/bin/sh

sleep 5
mkdir -p /root/.gaiad/config

if [ ! -f "/root/.gaiad/config/node_key.json" ]
then
  cp /genesis.json /root/.gaiad/config
  cp /config.toml  /root/.gaiad/config
fi

if [ ! -f "/root/.gaiad/config/genesis.json" ]
then
  cp /genesis.json /root/.gaiad/config/genesis.json
fi

if [ ! -f "/root/.gaiad/config/config.toml" ]
then
  cp /config.toml /root/.gaiad/config/config.toml
fi

/root/start_script.sh
