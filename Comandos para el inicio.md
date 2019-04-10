##  Esto es para empezar con los playbooks posibles, ordenados para la ejecución, necesita ejecutar estos comandos en la misma carpeta _`/roles`_ 

# Para los nodos _sentry_ :

1. **Añadir _sudoers_:**
 
`ansible-playbook -l sentry roles/add-sudoers.yml -b -K `

**Recuerda, cambia tu _moniker (el nombre que identificará al nodo)_**

2. **Ejecuta el _playbook_ motherfucker:**
 
`ansible-playbook -l sentry roles/master-playbook-sentrys.yml`

3. **Matar Gaiad**

`ansible-playbook -l sentry roles/kill-gaiad.yml`

4. **Restablecer Gaiad**

`ansible sentry -m shell -a "./bin/gaiad unsafe-reset-all"`

5. **Inicio Gaiad**

`ansible-playbook -l sentry roles/run-gaia.yml`

**Notas:**

* **Guardar logs de _ID&IPs_:**

`./scripts/get-peers.py`

* **Ver los logs formateados**:

`./scripts/fixformat.py`


# Para el nodo validador:
1. **Añadir _sudoers_:**

`ansible-playbook -l valid roles/add-sudoers.yml -b -K`

**Recuerda, cambia tu _moniker (el nombre que identificará al nodo)_**

2. **Ejecuta el _playbook_ motherfucker:**
 
`ansible-playbook -l valid roles/master-playbook-valid.yml`

3. **Deposita tu participación, _recuerda cambiar la cantidad_:**
 
```
gaiacli tx stake create-validator --amount=10STAKE --chain-id=$(curl -s http://localhost:26657/status | jq -r '.result.node_info.network') --pubkey=$(gaiad tendermint show-validator) --moniker=$(gaiacli keys list | awk 'FNR==2{print $1}') --from=$(gaiacli keys list | awk 'FNR==2{print $3}') --commission-rate="0.10" --commission-max-rate="0.20" --commission-max-change-rate="0.01"
```
