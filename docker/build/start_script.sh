#!/bin/sh
# Start the first process

mkdir -p /root/.gaiad/config

if [ ! -f "/root/.gaiad/config/genesis.json" ]
then
  cp /usr/src/app/genesis.json /root/.gaiad/config/genesis.json
fi

if [ ! -f "/root/.gaiad/config/config.toml" ]
then
  cp /usr/src/app/config.toml /root/.gaiad/config/config.toml
fi

nginx > /dev/null 2>&1 & 
gaiad start
