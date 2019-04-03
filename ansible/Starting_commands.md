##  This is to start with ansible playbooks, sorted for the execution,
## you need to execute these commands in the same folder as `/roles` 

# For the sentry node:

1. **Add sudoers:**
 
`ansible-playbook -l sentry roles/add-sudoers.yml -b -K `

_Remember, change your moniker_

2. **Run motherfucker playbook:**
 
`ansible-playbook -l sentry roles/master-playbook-sentrys.yml`

3. **Kill Gaiad**

`ansible-playbook -l sentry roles/kill-gaiad.yml`

4. **Reset Gaiad**

`ansible sentry -m shell -a "./bin/gaiad unsafe-reset-all"`

5. **Start Gaiad**

`ansible-playbook -l sentry roles/run-gaia.yml`

**Notes:**

* Save logs ID&IPs:

`./scripts/get-peers.py`

* See output formated:

`./scripts/fixformat.py`


# For the validator node:
1. **Add sudoers:**

`ansible-playbook -l valid roles/add-sudoers.yml -b -K`

_Remember, change your moniker_

2. **Run motherfucker playbook:**
 
`ansible-playbook -l valid roles/master-playbook-valid.yml`

3. **Stake your deposit, _change the amount_:**
 
```
gaiacli tx stake create-validator --amount=10STAKE --chain-id=$(curl -s http://localhost:26657/status | jq -r '.result.node_info.network') --pubkey=$(gaiad tendermint show-validator) --moniker=$(gaiacli keys list | awk 'FNR==2{print $1}') --from=$(gaiacli keys list | awk 'FNR==2{print $3}') --commission-rate="0.10" --commission-max-rate="0.20" --commission-max-change-rate="0.01"
gaiacli tx stake create-validator --amount=10STEAK --chain-id=$(curl -s http://localhost:26657/status | jq -r '.result.node_info.network') --pubkey=$(gaiad tendermint show-validator) --moniker=$(gaiacli keys list | awk 'FNR==2{print $1}') --from=$(gaiacli keys list | awk 'FNR==2{print $3}') --commission-rate="0.10" --commission-max-rate="0.20" --commission-max-change-rate="0.01"
```
