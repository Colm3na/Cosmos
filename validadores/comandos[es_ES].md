## configuración para el validador _(puedes encontrar estos tips en la [documentacion](https://cosmos.network/docs/validators/validator-setup.html#validator-setup) de Cosmos y el cliente [Gaia](https://cosmos.network/docs/gaia/gaiacli.html#gaia-cli))_:

## Comandos para `gaia-9002` & `Game of Stakes`:
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

* **Generar el _`gentx`_ para `GoS` _(recuerda modificar los valores)_**:
```
gaiad gentx --amount 10000STAKE --commission-rate "0.10" --commission-max-rate "1.00" --commission-max-change-rate "0.01" --pubkey $(gaiad tendermint show-validator) --name $(gaiacli keys list -o=json | jq -r '.[].name')
```

# Configuración del validador _(recuerda modificar los valores)_:
* **Crear validador:**
```
gaiacli tx stake create-validator --amount=5STAKE --pubkey=$(gaiad tendermint show-validator) --moniker="choose a moniker" --chain-id=<chain_id> --from=<key_name> --commission-rate="0.10" --commission-max-rate="0.20" --commission-max-change-rate="0.01"
```

* **Editar la descripción del validador:**
```
gaiacli tx stake edit-validator --moniker="choose a moniker" --website="https://cosmos.network" --identity=6A2265E29A4CBC8E --details="To infinity and beyond!" --chain-id=<chain_id> --from=<key_name> --commission-rate="0.10"
```

* **Ver la descripción del validador:**
```
gaiacli query stake validator <account_cosmos>
```

* **Generar la wallet:**
```
gaiacli keys add <account_name>
```

* **Mostrar todas las wallets:**
```
gaiacli keys list
```

* **Mirar la wallet generada:**
```
gaiacli keys show <account_name>
```

* **Address para operar del validador:**
```
gaiacli keys show <account_name> --bech=val
```

* **Clave pública para el nodo del validador:**
```
gaiad tendermint show-validator
```

* **Ver la descripción del validador:**
```
gaiacli query stake validator <account_cosmos>
```

* **Track validator signing information:**
```
gaiacli query slashing signing-info <validator-pubkey> --chain-id=<chain_id>
```

* **_Unjail_ validador:**
```
gaiacli tx slashing unjail --from=$(gaiacli keys list -o=json | jq -r '.[].name') --chain-id=game_of_stakes_5 --trust-node=true
```

* **Confirmar que el validador está funcionando:**
```
gaiacli query tendermint-validator-set | grep "$(gaiad tendermint show-validator)"
```

* **Balance:**
```
gaiacli query account <account_cosmos>
```

* **Enviar tokens:**
```
gaiacli tx send --amount=10STAKE --chain-id=<chain_id> --from=<key_name> --to=<destination_cosmos>
```

* **Vincular tokens:**
```
gaiacli tx stake delegate --amount=10STAKE --validator=<validator> --from=<key_name> --chain-id=<chain_id>
```

* **Ver información del validador:**
```
gaiacli query stake delegation --address-delegator=<account_cosmos> --validator=<account_cosmosval>
```

* **Comprobar todas las actuales delegaciones de distintos delegadores:**
```
gaiacli query stake delegations <account_cosmos>
```

* **Desvincular tokens:**
```
gaiacli tx stake unbond --validator=<account_cosmosval> --shares-fraction=0.5 --from=<key_name> --chain-id=<chain_id>
```

* **Mirar información acerca de _`unbonding-delegation`_:**
```
gaiacli query stake unbonding-delegation --address-delegator=<account_cosmos> --validator=<account_cosmosval>
```

* **Comprobar todas las actuales _`unbonding-delegations`_ de distintos delegadores:**
```
gaiacli query stake unbonding-delegations <account_cosmos>
```

* **Comprobar todas las _`unbonding-delegations`_ de un validador en particular:**
```
  gaiacli query stake unbonding-delegations-from <account_cosmosval>
```

* **Redelegar tokens:**
```
gaiacli tx stake redelegate --addr-validator-source=<account_cosmosval> --addr-validator-dest=<account_cosmosval> --shares-fraction=50 --from=<key_name> --chain-id=<chain_id>
```

* **Consultas de las redelegaciones:**
```
gaiacli query stake redelegation --address-delegator=<account_cosmos> --addr-validator-source=<account_cosmosval> --addr-validator-dest=<account_cosmosval>
```

* **Comprobar todas las actuales _`unbonding-delegations`_ de distintos validadores:**
```
gaiacli query stake redelegations <account_cosmos>
```

* **Todas las redelegaciones salientes para un validador en particular**
```
gaiacli query stake redelegations-from <account_cosmosval>
```

* **Ajustes actuales de alto nivel para realizar el stake:**
```
gaiacli query stake parameters
```

# Governanza:
* **Crear una propuesta de gobernanza:**
```
gaiacli tx gov submit-proposal --title=<title> --description=<description> --type=<Text/ParameterChange/SoftwareUpgrade> --deposit=<40STAKE> --from=<name> --chain-id=<chain_id>
```

* **Consulta de propuestas _(una vez creadas)_:**
```
gaiacli query gov proposal --proposal-id=<proposal_id>
```

* **Consultar todas las propuestas disponibles:**
```
gaiacli query gov proposals
```

* **Aumento del depósito de las propuestas _(por defecto `10STAKE`)_:**
```
gaiacli tx gov deposit --proposal-id=<proposal_id> --deposit=<200STAKE> --from=<name> --chain-id=<chain_id>
```

* **Consultar todos los depósitos presentados _(una vez creada una nueva propuesta)_:**
```
gaiacli query gov deposits --proposal-id=<proposal_id>
```

* **Depósito de consulta _(dirección específica)_:**
```
gaiacli query gov deposit --proposal-id=<proposal_id> --depositor=<account_cosmos>
```

* **Votar en una propuesta:**
```
gaiacli tx gov vote --proposal-id=<proposal_id> --option=<Yes/No/NoWithVeto/Abstain> --from=<name> --chain-id=<chain_id>
```

* **Consulta de votos _(opción enviada)_:**
```
gaiacli query gov vote --proposal-id=<proposal_id> --voter=<account_cosmos>
```

* **Propuesta presentada anteriormente:**
```
gaiacli query gov votes --proposal-id=<proposal_id>
```

* **Propuesta de consulta para los resultados**
```
gaiacli query gov tally --proposal-id=<proposal_id>
```

# Variables usadas:
* **Id de la rama:**
```
curl -s http://localhost:26657/status | jq -r '.result.node_info.network'
```

* **Wallet Cosmos:**
```
gaiacli keys list -o=json | jq -r '.[].name'
```

* **Nombre de la wallet:**
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
* **ID de la proposición:**
```
gaiacli query gov proposals --trust-node=true | tail -n 1 | cut -d'-' -f1
```

* **Conectarse a los _endpoints_:**
```
ssh -i ~/.ssh/user_rsa -L 26657:localhost:26657 user@[ IP ]
```
