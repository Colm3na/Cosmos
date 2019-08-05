## Steps to create `gentx`:

# If we need to delete address:
```
gaiacli keys delete $(gaiacli keys list -o=json | jq -r '.[].name') 
```

# Reset values:
```
gaiad unsafe-reset-all 
```

# Backup of your old files (remember, somes names of files can be diferent):
```
mv .gaiad/ /home/user/old.copies/
```

# Recover address:
```
gaiacli keys add --recover <ADDRESSNAME>
```

# Run `gaiad init`:
```
gaiad init --moniker=$(gaiacli keys list -o=json | jq -r '.[].name') 
```

# Download genesis:
```
curl https://raw.githubusercontent.com/cosmos/game-of-stakes/master/genesis.json > $HOME/.gaiad/config/genesis.json 
```

# Generate `gentx`:
```
gaiad gentx --amount 10000STAKE --commission-rate "0.10" --commission-max-rate "1.00" --commission-max-change-rate "0.01" --pubkey $(gaiad tendermint show-validator) --name $(gaiacli keys list -o=json | jq -r '.[].name') 
```

# See the file `gentx` (use tab to fill), copy and send a `PR` to repo of [Game of Steaks](https://github.com/cosmos/game-of-stakes/pulls):
```
cat /home/user/.gaiad/config/gentx/gentx-
```
