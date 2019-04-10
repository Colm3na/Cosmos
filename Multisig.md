<sumary>
<h1 align="center">Cómo enviar 1 Atom y quemar 9 Atoms al mismo tiempo:fire:</h1>
<br>
<details>
<h2 align="center">Primero hay que compilar una versión especial de gaiacli</h2>


```
mkdir -p ~/go/src/github.com/cosmos
cd ~/go/src/github.com/cosmos
git clone https://github.com/cosmos/cosmos-sdk
cd cosmos-sdk
git fetch --tags
git checkout bez/limited-multisend-cmd
make update_tools
make get_vendor_deps
make install
```
> ::

```
gaiacli version --long
```

>Debería dar un resultado más o menos asi:

```
gaiacli version --long
cosmos-sdk: 0.33.0-1-ga08822d
git commit: a08822d6b6afc1cd7b927d20e614f6c1a90736a6
vendor hash: 81cd66597752534f2724035e5444bf2394d32623
build tags: netgo ledger
go version go1.11.5 linux/amd64
```

> NOTA: Suponemos que ya tienes la wallet importada en tu nodo.

<h2>Creamos la transacción especial que destruye 9atom y envía 1atom</h2>

```
gaiacli tx multisend <cosmos address>  --from=YourKey --fees=5000uatom --chain-id=cosmoshub-1 > unsigned_limited_multisend.json
```

<h2>Firmamos la transacción:</h2>

```
gaiacli tx sign unsigned_limited_multisend.json --fees=5000uatom --from=YourKey --validate-signatures --chain-id=cosmoshub-1 > signed_limited_multisend.json
```

<h2>Enviamos la transacción a la red</h2>


```
gaiacli tx broadcast signed_limited_multisend.json --fees=5000uatom --from=YourKey --memo=MushoBetis --chain-id=cosmoshub-1
```

<h1 align="center">Es todo!!</h1>
</details>
</sumary>



<sumary>
<h1 align="center">HowTo send 1 Atom and burn 9 Atoms at the same time.:fire:</h1>
<br>
<details>
<h2 align="center">Firtly you have to compile a special version of gaiacli</h2>


```
mkdir -p ~/go/src/github.com/cosmos
cd ~/go/src/github.com/cosmos
git clone https://github.com/cosmos/cosmos-sdk
cd cosmos-sdk
git fetch --tags
git checkout bez/limited-multisend-cmd
make update_tools
make get_vendor_deps
make install
```
> ::


```
gaiacli version --long
```

<h2>It should match this:</h2>

```
gaiacli version --long
cosmos-sdk: 0.33.0-1-ga08822d
git commit: a08822d6b6afc1cd7b927d20e614f6c1a90736a6
vendor hash: 81cd66597752534f2724035e5444bf2394d32623
build tags: netgo ledger
go version go1.11.5 linux/amd64
```

>  NOTE: It is supposed you have imported the wallet in your node.

<h2>Create de special TX that burns 9atoms and send 1atom</h2>

```
gaiacli tx multisend <cosmos address>  --from=YourKey --fees=5000uatom --chain-id=cosmoshub-1 > unsigned_limited_multisend.json
```

<h2>Sign the TX</h2>

```
gaiacli tx sign unsigned_limited_multisend.json --fees=5000uatom --from=YourKey --validate-signatures --chain-id=cosmoshub-1 > signed_limited_multisend.json
```

<h2>Sent the TX to the network</h2>


```
gaiacli tx broadcast signed_limited_multisend.json --fees=5000uatom --from=YourKey --memo=MushoBetis --chain-id=cosmoshub-1
```

<h1 align="center">End!!</h1

</details>

</sumary>
