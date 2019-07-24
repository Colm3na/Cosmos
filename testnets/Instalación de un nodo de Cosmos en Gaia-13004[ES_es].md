<h1 align="center"> Aquí se describen los pasos necesarios para instalar un nodo de Cosmos en la testnet <code>Gaia-13004.</code></h1>

<p>· <a href="https://github.com/cosmos/gaia">Este</a> es el repositorio de Cosmos para Gaia.</p>

<p>· <a href="https://github.com/cosmos/testnets">Este</a> es el repositorio de Cosmos para testnets.</p>

## Instalamos prerequisitos _(`jq` no es esencial pero lo usaremos alguna vez)_:

```
sudo apt install -y make wget curl git gcc jq build-essential software-properties-common 
```


## Instalamos la última versión de [GO](https://golang.org/dl/)

```
wget -c 'https://dl.google.com/go/go1.12.7.linux-amd64.tar.gz' -O go1.12.7.linux-amd64.tar.gz

sudo tar -C /usr/local -xzf go1.12.7.linux-amd64.tar.gz

sudo rm -Rf go1.12.7.linux-amd64.tar.gz
```

## Añadimos Go a nuestro [PATH](https://es.wikipedia.org/wiki/PATH_(informática)).

>::Abrimos el archivo para añadirle algunas líneas con vim __(en mi caso uso vim, podemos cambiarlo por nano u otro editor)__, **recuerda modificar "<USER>" por tu usuario**::

```
vim /home/<USER>/.profile
```

>::Añadimos al final del archivo las siguientes líneas::

```
export PATH="$PATH:/usr/local/go/bin"

export GOPATH="$HOME/go"

export PATH="$PATH:$GOROOT/bin:$GOPATH/bin"

export GOBIN="$GOPATH/bin"
```

>::Recargamos nuestra terminal::

```
source /home/$USER/.profile 
```

>::Comprobamos la version de Go::

```
> go version

go version go1.12.7 linux/amd64
```

## Clonamos el repositorio de [gaia](https://github.com/cosmos/gaia):

```
git clone https://github.com/cosmos/gaia.git
```

>::Entramos en la carpeta de gaia y nos aseguramos de estar en la versión correcta, _(en el momento la última versión es `v1.0.0-rc1`)_ **comprobar [aqui](https://github.com/cosmos/gaia/releases) la última versión**::

```
cd gaia/

git checkout v1.0.0-rc1
```

>::Instalamos::

```
make install
```

>::Comprobamos nuestra versión de gaiad y gaiacli::

```
> gaiad version --long

name: gaia
servername: gaiad
clientname: gaiacli
version: 1.0.0-rc1
gitcommit: fd2691818f4fbb5b03b79481ae8e2f07d9a7d0b0
buildtags: netgo,ledger
goversion: go version go1.12.7 linux/amd64
```

```
> gaiacli version --long

name: gaia
servername: gaiad
clientname: gaiacli
version: 1.0.0-rc1
gitcommit: fd2691818f4fbb5b03b79481ae8e2f07d9a7d0b0
buildtags: netgo,ledger
goversion: go version go1.12.7 linux/amd64
```

## Creamos los primeros archivos de configuración, el nombre que pongamos será el nombre del nodo _(recuerda modificar los valores que estan señalados con `< >`)_

```
gaiad init <NOMBRE>
```

>::Comprobamos que nos ha creado la carpeta `.gaiad/`, dentro de la misma podemos encontrar `config/`_(contiene los archivos de configuración)_ y `data/`_(contiene la información de la blockchain, asi como la base de datos para su sincronización con otro nodo)_::

>::Eliminamos el genesis creado y nos descargamos el de Cosmos, _(comprobar [aquí](https://github.com/cosmos/testnets/tree/master/gaia-13k) la version del genesis)_

```
cd .gaiad/config/

rm genesis.json

wget https://raw.githubusercontent.com/cosmos/testnets/master/gaia-13k/genesis.json 
```

>::Comprobamos el shasum del genesis descargado _(comprobar con el del [repositorio oficial](https://github.com/cosmos/testnets#july-22-2019-2120-gmt--gaia-13004))_::

```
shasum -a 256 genesis.json
```

>::Debería ser::

```
a22d5d16ec2666b0a8cca9bd374fe26c1c0f2f52b1dc1ccf6e0cb8c93eefc771  genesis.json
```

## Añadimos los seeds, podemos encontrarlos en el [repositorio de gaia](https://github.com/cosmos/testnets#july-22-2019-2120-gmt--gaia-13004)

>::Seeds::

```
35b9658ca14dd4908b37f327870cbd5007ee06f1@116.203.146.149:26656

c24f496b951148697f8a24fd749786075c128f00@35.203.176.214:26656

6be0856f6365559fdc2e9e97a07d609f754632b0@cosmos-gaia-13004-seed.nodes.polychainlabs.com:26656
```


>::Peers de [Colmena](https://www.coworkingcolmena.com), [DelegaNetworks](https://delega.io) y [DragonStake](https://dragonstake.io/#/) para la testnet::

```
06b158b29797610476e621f28867cbae926fd1d3@163.172.129.132:26656

3d354e7383afa29b5bf9741fa4b9831403e880c5@51.15.127.68:26656
```

## Comprobamos el ID de nuestro nodo, podemos compartirlo en un futuro para conectarnos con otros nodos:

```
gaiad tendermint show-node-id
```

## Iniciamos el nodo:

```
gaiad start
```

## Añadir gaiad como un servicio de sistema:

>::Entramos en la carpeta::

```
cd /etc/systemd/system/
```

>::Creamos un archivo llamado `gaiad.service`::

```
sudo vim gaiad.service
```

>::Dentro copiamos lo siguiente, **recordad cambiar USER por vuestro usuario**::

```
[Unit]
Description=Cosmos Gaia Node
After=network.target

[Service]
Type=simple
User=USER
WorkingDirectory=/home/USER
ExecStart=/home/USER/go/bin/gaiad start
Restart=on-failure
RestartSec=3
LimitNOFILE=4096

[Install]
WantedBy=multi-user.target
```

>**Paramos `gaiad` si lo tenemos funcionando antes de seguir!!**

>::Activamos el servicio y lo iniciamos::

```
sudo systemctl enable gaiad.service 

sudo systemctl start gaiad.service
```

>::Para comprobar que el servicio está funcionando y ver el estado creamos un script::

```
vim chechGaiad
```

>::Copiamos lo siguiente, guardamos y salimos::

```
#!/bin/bash
#
#
sudo journalctl -f -u gaiad.service
```

>::Damos permisos de ejecución:

```
chmod +x checkgaiad
```

>::Ejecutamos el script para ver la información del nodo::

```
./checgaiad
```
>_Aunque nosotros paremos el script, el servicio de gaia seguirá funcionando, y en caso de reiniciarse la máquina el servicio de gaia se iniciará con el sistema_
