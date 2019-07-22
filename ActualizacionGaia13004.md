# Aquí se describen los pasos necesarios para actualizar el nodo de Cosmos en la Testnet `Gaia-13003` a `Gaia-13004` 

[Este](https://github.com/cosmos/gaia) es el reposotorio de Cosmos para gaia y [este](https://github.com/cosmos/cosmos-sdk/) 
el repositorio para el sdk de Cosmos.

## Necesitamos la última version de [Go](https://golang.org/dl/) instalada, en caso de tener Go podemos saltar este paso:
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

## Actualizamos Cosmos-sdk a la versión v0.34.7 __(mínimo necesitamos la versión 0.34.6)__:
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

## Clonamos el repositorio de [gaia](https://github.com/cosmos/gaia.git), (usamos la rama [1.0.0-rc1](https://github.com/cosmos/gaia/releases/tag/v1.0.0-rc1) ) e instalamos:
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

- Recuerda que toda la información la puedes encontrar en su [RIOT](https://riot.im/app/#/room/#cosmos_validators_technical_updates:matrix.org). 

- Comenzará el proceso de actualización a la 1 PM PST y se establece la hora del génesis a la 1:30PM PST.


