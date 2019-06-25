## Para compilar con lo mínimo:

`
git clone git@github.com:Colm3na/Cosmos.git`

`
cd Cosmos/docker`

`
git clone https://github.com/cosmos/cosmos-sdk.git`

`
git clone https://github.com/luniehq/lunie.git`

`
cd cosmos-sdk`

`
git fetch --tags`

`
git checkout v0.34.7`

`
cd ..`

`
docker build -t gaia .`

