Aquí se describen los pasos para instalar un nodo de Cosmos en la testnet [gaia-13006](https://hubble.figment.network/cosmos/chains/gaia-13006).

Si necesitas instalar Go puedes ver los pasos [aquí](https://github.com/Colm3na/Cosmos/blob/master/testnets/Instalación%20de%20un%20nodo%20de%20Cosmos%20en%20Gaia-13004%5BES_es%5D.md#instalamos-la-última-versión-de-go), recuerda que debes clonar el repositorio en el `/home` para no tener problemas.

# Clonamos el repositorio de [gaia](https://github.com/cosmos/gaia)

```
git clone https://github.com/cosmos/gaia.git
```

>::Entramos en la carpeta de gaia y nos aseguramos de estar en la versión correcta, _(en el momento la última versión es `v2.0.0-rc1`)_ **comprobar [aqui](https://github.com/cosmos/gaia/releases) la última versión**::

```
cd gaia

git checkout v2.0.0-rc1
```

>::Instalamos::

```
make install
```

>::Comprobamos nuestra versión de gaiad y gaiacli::

```
> gaiacli version --long

name: gaia
server_name: gaiad
client_name: gaiacli
version: 2.0.0-rc1
commit: 89fe9e4ce8ddc96497ad4473ed4e78ab2e611f3d
build_tags: netgo,ledger
go: go version go1.12.7 linux/amd64
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

```
shasum -a 256 genesis.json
```
>::Debería ser::

```
75339ffb0a8be5489c16f00891a2984a8e0691b9fc82323d69ec906ec975c888
```

## Añadimos los peers, estos son de [DelegaNetworks](https://delega.io), [DragonStake](https://dragonstake.io/#/) y [La Colmena](https://www.colmenalabs.org), hasta el momento Cosmos no ha puesto peers para esta testnet, puedes comprobarlo [aquí](https://github.com/cosmos/testnets#testnet-status).

>::Peers::

```
06b158b29797610476e621f28867cbae926fd1d3@163.172.129.132:26656

3d354e7383afa29b5bf9741fa4b9831403e880c5@51.15.127.68:26656

dcbe32e354dd53ec9f0c47e6bb5acf03f70a920c@51.15.121.63:26656
```

## Comprobamos el ID de nuestro nodo, podemos compartirlo en un futuro para conectarnos con otros nodos:

```
gaiad tendermint show-node-id
```

## Iniciamos el nodo:

```
gaiad start
```

>Si queremos poner gaia como un servicio de sistema podemos seguir [estos](https://github.com/Colm3na/Cosmos/blob/master/testnets/Instalación%20de%20un%20nodo%20de%20Cosmos%20en%20Gaia-13004%5BES_es%5D.md#añadir-gaiad-como-un-servicio-de-sistema) pasos
