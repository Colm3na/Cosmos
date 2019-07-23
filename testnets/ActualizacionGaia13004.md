<h1 align="center"> Aquí se describen los pasos necesarios para actualizar el nodo de Cosmos en la Testnet <code>Gaia-13003</code> a <code>Gaia-13004</code> </h1> 

[Este](https://github.com/cosmos/gaia) es el repositorio de Cosmos para gaia y [este](https://github.com/cosmos/cosmos-sdk/) 
el repositorio para el sdk de Cosmos.

<sumary>
  <h2 align="center">Necesitamos la última version de <a href="https://golang.org/dl/"> Go</a> instalada, <i>en caso de tener Go podemos saltar este paso:</i></h2>

</sumary>
<details>

```
wget -c 'https://dl.google.com/go/go1.12.7.linux-amd64.tar.gz' -O go1.12.7.linux-amd64.tar.gz

sudo tar -C /usr/local -xzf go1.12.7.linux-amd64.tar.gz

sudo rm -Rf go1.12.7.linux-amd64.tar.gz
```

```
cat <<EOT >> ~/.profile
#Go:
export PATH="$PATH:/usr/local/go/bin"
export GOPATH="$HOME/go"
export PATH="$PATH:$GOROOT/bin:$GOPATH/bin"
export GOBIN="$GOPATH/bin"
EOT 
```

>::Recargamos nuestra terminal::
```
source /home/$USER/.profile 
```
</details>

<sumary>
  <h2 align="center">Actualizamos Cosmos-sdk a la versión v0.34.7 <i>(mínimo necesitamos la versión 0.34.6)</i>:</h2>

</sumary>
<details>

```
cd $GOPATH/src/github.com/cosmos/cosmos-sdk/

git checkout v0.34.7

make install
```

>::Comprobamos la versión de gaia y gaiacli:

```
>gaiad version --long
cosmos-sdk: 0.34.7
git commit: f783cb71e7fe976bc01273ad652529650142139b
vendor hash: f60176672270c09455c01e9d880079ba36130df4f5cd89df58b6701f50b13aad
build tags: netgo ledger
go version go1.12.7 linux/amd64
```

```
>gaiacli version --long
cosmos-sdk: 0.34.7
git commit: f783cb71e7fe976bc01273ad652529650142139b
vendor hash: f60176672270c09455c01e9d880079ba36130df4f5cd89df58b6701f50b13aad
build tags: netgo ledger
go version go1.12.7 linux/amd64
```
</details>

<sumary>
  <h2 align="center"> Clonamos el repositorio de 
    <a href="https://github.com/cosmos/gaia.git">gaia</a>, 
      <i>usamos la rama <a href="https://github.com/cosmos/gaia/releases/tag/v1.0.0-rc1">1.0.0-rc1</a></i> e instalamos:
  </h2>
</sumary>
<details>


```
git clone https://github.com/cosmos/gaia.git && cd gaia/ 

git checkout v1.0.0-rc1

make install
```

>::Comprobamos la version de gaiad y gaiacli::

```
>gaiad version --long
name: gaia
servername: gaiad
clientname: gaiacli
version: 1.0.0-rc1
gitcommit: fd2691818f4fbb5b03b79481ae8e2f07d9a7d0b0
buildtags: netgo,ledger
goversion: go version go1.12.7 linux/amd64
```

```
gaiacli version --long
name: gaia
servername: gaiad
clientname: gaiacli
version: 1.0.0-rc1
gitcommit: fd2691818f4fbb5b03b79481ae8e2f07d9a7d0b0
buildtags: netgo,ledger
goversion: go version go1.12.7 linux/amd64
```
</details>

<sumary>
  <h2 align="center"> Descargamos el <a href="https://raw.githubusercontent.com/cosmos/testnets/master/gaia-13k/genesis.json"> genesis </a> correcto, hacemos un reset  e iniciamos el nodo:</h2>
</sumary>
<details>

```
cd .gaiad/config/

rm -r genesis.json

wget https://raw.githubusercontent.com/cosmos/testnets/master/gaia-13k/genesis.json
```

>::Comprobamos el shasum del genesis descargado, lo podemos encontrar en el <a href="https://github.com/cosmos/testnets#july-22-2019-2120-gmt--gaia-13004">repo de testnets</a>::

```
shasum -a 256 genesis.json
```

>::Debería ser::

```
a22d5d16ec2666b0a8cca9bd374fe26c1c0f2f52b1dc1ccf6e0cb8c93eefc771  -
```

- Podemos encontrar seeds en el <a href="https://github.com/cosmos/testnets">repo de testnets</a> de Cosmos.

```
35b9658ca14dd4908b37f327870cbd5007ee06f1@116.203.146.149:26656
c24f496b951148697f8a24fd749786075c128f00@35.203.176.214:26656
6be0856f6365559fdc2e9e97a07d609f754632b0@cosmos-gaia-13004-seed.nodes.polychainlabs.com:26656
```

- Los __persistent peers__ de la <a href="https://www.coworkingcolmena.com">Colmena</a>,<a href="https://delega.io"> Delega Networks</a> y <a href="https://dragonstake.io/#/">Dragon Stake</a> son:

```
06b158b29797610476e621f28867cbae926fd1d3@163.172.129.132:26656

3d354e7383afa29b5bf9741fa4b9831403e880c5@51.15.127.68:26656
```

>::Iniciamos el nodo::

```
gaiad start
```
</details>


- Recuerda que toda la información sobre actualizaciones y más las puedes encontrar en su canal de [RIOT](https://riot.im/app/#/room/#cosmos_validators_technical_updates:matrix.org). 

- [Este](https://matrix.to/#/!vIMgGaMqkLIWPCZvPF:matrix.org?via=matrix.org&via=kde.org&via=ru-matrix.org) es el RIOT de Cosmos.

- [Este](https://t.me/cosmosproject) es su canal de Telegram.

- [Este](https://t.me/Cosmos_Network_ES) es el canal de Telegram en Español.
