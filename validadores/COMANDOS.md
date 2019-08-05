## configuración para el validador __(puedes encontrar estos tips en la [documentacion](https://cosmos.network/docs/validators/validator-setup.html#validator-setup) de Cosmos y el cliente [Gaia](https://cosmos.network/docs/gaia/gaiacli.html#gaia-cli))__:

## Comandos para `Cosmos`:

* **Inicio de un nuevo nodo:**
```
gaiad init --moniker <your_custom_moniker>
```

* **Inicio gaiad:**
```
gaiad start
```

* **Para la resolución de problemas:**
```
gaiad start --trace --log_level "*:debug"
```

* **Comprobar el estado de gaiad:**
```
gaiacli status
```

* **Generar el `gentx` para `GoS`** (recuerda modificar los valores):
```
gaiad gentx --amount 10000uatom --commission-rate "0.10" --commission-max-rate "1.00" --commission-max-change-rate "0.01" --pubkey $(gaiad tendermint show-validator) --name $(gaiacli keys list -o=json | jq -r '.[].name')
```

# Setup Validator:
* **Init validator:**
```
gaiacli tx stake create-validator --amount=5uatom --pubkey=$(gaiad tendermint show-validator) --moniker="choose a moniker" --chain-id=<chain_id> --from=<key_name> --commission-rate="0.10" --commission-max-rate="0.20" --commission-max-change-rate="0.01"

```
* **Edit validator description:**
```
gaiacli tx stake edit-validator --moniker="choose a moniker" --website="https://cosmos.network" --identity=6A2265E29A4CBC8E --details="To infinity and beyond!" --chain-id=<chain_id> --from=<key_name> --commission-rate="0.10"
```

* **View validator description:**
```
gaiacli query stake validator <account_cosmos>
```

* **Generate Keys:**
```
gaiacli keys add <account_name>
```

* **Show all address:**
```
gaiacli keys list
```

* **Show address generate:**
```
gaiacli keys show <account_name>
```

* **Validator operator's address:**
```
gaiacli keys show <account_name> --bech=val
```

* **Validator pubkey for node:**
```
gaiad tendermint show-validator
```

* **View validator description:**
```
gaiacli query stake validator <account_cosmos>
```

* **Track validator signing information:**
```
gaiacli query slashing signing-info <validator-pubkey> --chain-id=<chain_id>
```

* **Unjail validator:**
```
gaiacli tx slashing unjail --from=$(gaiacli keys list -o=json | jq -r '.[].name') --chain-id=game_of_stakes_5 --trust-node=true
```

* **confirm validator is running:**
```
gaiacli query tendermint-validator-set | grep "$(gaiad tendermint show-validator)"
```

* **Account balance:**
```
gaiacli query account <account_cosmos>
```

* **Send tokens:**
```
gaiacli tx send --amount=10uatom --chain-id=<chain_id> --from=<key_name> --to=<destination_cosmos>
```

* **Bond tokens:**
```
gaiacli tx stake delegate --amount=10uatom --validator=<validator> --from=<key_name> --chain-id=<chain_id>
```

* **See information about a validator:**
```
gaiacli query stake delegation --address-delegator=<account_cosmos> --validator=<account_cosmosval>
```

* **Check all current delegations with disctinct validators:**
```
gaiacli query stake delegations <account_cosmos>
```

* **Unbond tokens:**
```
gaiacli tx stake unbond --validator=<account_cosmosval> --shares-fraction=0.5 --from=<key_name> --chain-id=<chain_id>
```

* **See information about `unbonding-delegation`:**
```
gaiacli query stake unbonding-delegation --address-delegator=<account_cosmos> --validator=<account_cosmosval>
```

* **Check all current `unbonding-delegations` with disctinct validators:**
```
gaiacli query stake unbonding-delegations <account_cosmos>
```

* **Check all the `unbonding-delegations` from a particular validator:**
```
  gaiacli query stake unbonding-delegations-from <account_cosmosval>
```

* **Redelegate tokens:**
```
gaiacli tx stake redelegate --addr-validator-source=<account_cosmosval> --addr-validator-dest=<account_cosmosval> --shares-fraction=50 --from=<key_name> --chain-id=<chain_id>
```

* **Query redelegations:**
```
gaiacli query stake redelegation --address-delegator=<account_cosmos> --addr-validator-source=<account_cosmosval> --addr-validator-dest=<account_cosmosval>
```

* **Check all current `unbonding-delegations` with disctinct validators:**
```
gaiacli query stake redelegations <account_cosmos>
```

* **All outgoing redelegations for a particula validator**
```
gaiacli query stake redelegations-from <account_cosmosval>
```

* **Current high level settings for staking:**
```
gaiacli query stake parameters
```

# Governance:

* **Create a governance proposal:**
```
gaiacli tx gov submit-proposal --title=<title> --description=<description> --type=<Text/ParameterChange/SoftwareUpgrade> --deposit=<40uatom> --from=<name> --chain-id=<chain_id>
```

* **Query proposals (once created):**
```
gaiacli query gov proposal --proposal-id=<proposal_id>
```

* **Query all available proposals:**
```
gaiacli query gov proposals
```

* **Increased deposit proposals (default `10uatom`):**
```
gaiacli tx gov deposit --proposal-id=<proposal_id> --deposit=<200uatom> --from=<name> --chain-id=<chain_id>
```

* **Query all deposits submited (once a new proposal is created):**
```
gaiacli query gov deposits --proposal-id=<proposal_id>
```

* **Query deposit submitted (specific address):**
```
gaiacli query gov deposit --proposal-id=<proposal_id> --depositor=<account_cosmos>
```

* **Vote on a proposal:**
```
gaiacli tx gov vote --proposal-id=<proposal_id> --option=<Yes/No/NoWithVeto/Abstain> --from=<name> --chain-id=<chain_id>
```

* **Query votes (option submitted):**
```
gaiacli query gov vote --proposal-id=<proposal_id> --voter=<account_cosmos>
```

* **Previous submitted proposal:**
```
gaiacli query gov votes --proposal-id=<proposal_id>
```

* **Query proposal tally results:**
```
gaiacli query gov tally --proposal-id=<proposal_id>
```



# Variables used:

* **Chain id:**
```
curl -s http://localhost:26657/status | jq -r '.result.node_info.network'
```

* **Account Cosmos:**
```
gaiacli keys list -o=json | jq -r '.[].name'
```

* **Key name:**
```
gaiacli keys list -o=json | jq -r '.[].name'
```

* **Cosmosvaloper:**
```
gaiacli keys show $(gaiacli keys show ${keyname} --bech=val --output=json | jq -r '.address'')
```

* **Balance:**
```
gaiacli query account $(gaiacli keys list -o=json | jq -r '.[].address') --chain-id=${chain_id} --trust-node=true | jq -r '.value.coins[0].amount'
```
* **Proposal id:**
```
gaiacli query gov proposals --trust-node=true | tail -n 1 | cut -d'-' -f1
```

* **Connect to Endpoints:**
```
ssh -i ~/.ssh/user_rsa -L 26657:localhost:26657 user@[ IP ]
```
