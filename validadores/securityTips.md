# Security for Cosmos Network

## Index

[Spin up a new Full-node quickly](/securityTips.md#spin-up-a-new-full-node-quickly)

[Move the “Validator soul” from one node to a new one](/securityTips.md#move-the-validator-soul-from-server-a-to-server-b)

[Close RPC port](/securityTips.md#Close-RPC-port)

[Change SSH port](/securityTips.md#Change-SSH-port)

### Summary

We, [@wimel85](https://github.com/wimel) and [@DerFredy](https://github.com/derfredy) elaborated this table with some relevant network information. We discovered that almost nobody is hiding their IP's and almost everybody has RPC port open. There are even some nodes with too many open ports and running services.
The color Green represents well configured parameter.

The aim of this document is to help our validator set to gain certain skills needed for running a Sentinel tendermint node during this Sentinel Testnet phase and prepare the setup for the mainnet. We have detected severe to medium lack of proper configuration in the actual set and is our wish that every validator do their best to improve the network security.
Basically we encourage almost every validator to spin up a new machine. That new machine will be the new validator. The old one will be reused as a public sentry node. It is up to the validator set to form alliances and share resources (such as sentries) between them. We think that practice of dealing with sentry nodes is important. Actually almost all validators seem to be running without any sentry.

### Spin up a new Full-node quickly

Boot a new server. You can use any cloud VPC. We call this new server Server-B later in this document.

Upload the binaries to the folder `$HOME/go/bin`, create this folder if it doesn't exist.
Init the daemon to let it create all the folders and files it needs. Then run:

```bash
$HOME/go/bin/gaiad init [ Your-Validator-Moniker ]
```

Upload the current `genesis.json` file that match the network and overwrite the one in your `$HOME/.gaiad/config` folder

2 steps [rsync](https://es.wikipedia.org/wiki/Rsync)

Why 2 steps rsync?

>**Explanation:**
rsync command will copy all files in the blockchain database but it will fail to copy some of them that are currently in use by the daemon. The 2 steps rsync let you sync a new node without stopping the first one for a long time.

Basically you rsync once (it may take very long to finish), them stop the node and rsync again (this time it will be much faster). Finally start the node.

What to rsync  Warning!!!, only data folder, **NEVER config folder** -> **doublesign risk**

>We will be copying just the entire `.gaiad/data` folder from **Server-A** to **Server-B**

What command to use

We have different rsync commands depending of your case. If you use ssh key and a custom ssh port this is the command (change the `3456` for your ssh port):

```bash
rsync -i ~/.ssh/id_rsa -arvz -e 'ssh -p 3456' user@[Server-A IP]:$HOME/.gaiad/data/ $HOME/.gaiad/data --progress
```

Sustitute `$HOME` for your home path

If you use standar 22 port and no ssh keys use this one:

```bash
rsync -arvz user@[Server-A IP]:$HOME/.gaiad/data/ $HOME/.gaiad/data --progress
```

### Move the _“Validator soul”_ from **Server-A** to **Server-B**

_“Validator soul”_ consists of 2 files:  `priv_validator_key.json`  and  `node_key.json`

Both of them are placed in `$HOME/.gaiad/config`  folder.

>**You have to backup those files the same way you did with the 24 words of your Wallet.**

We will need to move our validator from one server to a new one very few times. This is a risky maintenance task because this time is where a mistake could end in a tombstone validator, what it means: **game over, forever in jail…** And not only that, a **severe punishment** is applied if your validator get tombstone because doublesigning. It is **actually a 5% of your total stake**, and this punishment is also suffered by your delegators.

What we should **ALWAYS** avoid is having 2 servers running at the same time with the same _“soul”_, that is, with the same **private keys**. If this happened, the network will consider you are trying a double spend attack, and will punish you and your delegators.

#### Step by step guide:

We are moving our validator form **Server-A** to **Server-B**. At the same time we are going to use **Server-A** as a sentry node for our new **Server-B** validator in order to hide our public IP behind it.

Before starting obtain your validator ID. It will not change after this procedure. We are only changing it's IP. This is the command that will show your validator ID

`gaiad tendermint show-node-id`

1. On **Server-A** completely ensure that you have a backup of the 2 important files outside of the machine, `priv_validator_key.json` and `node_key.json`. Several encrypted USB drives on different locations is recommended. Do not missvalue your mum bedroom :-)

2. On **Server-A**, after twice checking point number 1 proceed to delete `priv_validator_key.json` and `node_key.json`

3. Now we will add our validator ID to the `config.toml` We will add the ID in the parameter _“private_peers_id”_ on **Server-A**. When the new validator connect to its sentry, the new IP will not be gossiped. Due to a bug in the p2p it is prefereable that the validator connects to its sentry, and not the reverse way. If the sentry happen to start the connectiong against the validator this bug may ( or may not ) gossip our validator IP. So we will do it in a secure way by now just in case. That is, we will not add our new validator ID@IP:PORT to _"persisnte_peers"_ in Server-A. 

4. Stop **Server-A** daemon. You will start losing blocks at this moment. Don't panic or hurry. It's ok.

5. Start again **Server-A**. Now, without the validator keys, this machine will be a normal full node, not a validator anymore. So it will still be losing blocks. Look for your new sentry ID and add it to your new validator `config.toml` in **Server-B** in the _"persisnte_peers"_ parameter. Use ID@IP:PORT in this case. Yo can get the ID of **Server-A** with this command:

`gaiad tendermint show-node-id`

6. On **Server-B**, overwrite `priv_validator_key.json` and `node_key.json` with your priceless backed files.

7. **Stop Server-B daemon**

8. **Start Server-B daemon**

After number 8, your validator should connect to your sentry and start signing blocks again. If this does not happen double check that each machine has the other one ID and IP in its `config.toml` 

It is a good idea to watch the explorer in your browser to see the entire process. It is ok if you lose a bunch of blocks. More experienced validators can do this without losing a single block. But it does not worth the chance to doublesign.

### Close RPC port

This really easy, but we have found almost every validator has this port ( 26657 ) open in the testnet. Requesting information from this port you could know the IP of the nodes you are connected to, including the validator.

>Look for the following section and change laddr from `0.0.0.0` to `127.0.0.1`

```bash
##### rpc server configuration options

[rpc]

##### TCP or UNIX socket address for the RPC server to listen on

laddr = "tcp://127.0.0.1:26657"
```

Then **stop and start your daemon** to apply the new configuration.

### Change SSH port

By default this port is `tcp/22`. It is considered a good practice to change this value to something over `1024`. Below `1024` we find the reserved standard system ports.

Before you apply any change to this port it is important that you ensure that the new port will not be filtered by your VPC provider. For example, if you chose port 4567 as your new SSH port and you are using an AWS instance you should add a new security group to permit this trafic. Consult your VPC provider.
A second piece of advice is that once you change it you should not close your terminal session until you are confident that you can login from a different terminal using the new port. In case you lose access you could revert the changes easily

#### The SSH port is changed in this config file:

`/etc/ssh/sshd_config`

Search for a parameter like this:

`# Port 22`

Change it and un-comment the line:

`Port 4567`

Save the file and restart the service:

`systemctl restart ssh`

You can check if your new port is in use with this command:

`netstat -tulpn`

If so, try to login with a different terminal tab or window and the new port. If you succeed you are done.
