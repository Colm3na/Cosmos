## Para compilar con lo mínimo:

`
git clone git@github.com:Colm3na/Cosmos.git`

`
cd Cosmos/docker`

`
Dentro de nuestro repositorio vamos a anidar 2 repositorios más. 
También los hemos añadimos al archivo .gitignore para
que nuestro repo principal no le haga seguimiento:`

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
cd ../lunie`

`
git checkout master`

`
cd ..`

`
docker build -t cosmos .`

