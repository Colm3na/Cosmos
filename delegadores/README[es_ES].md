<h1 align="center">Cosmos Delegators</h1>


<p align="center"> 
<img src="/images/cosmosLogo.png">
</p>


_Esta información ha sido traducida del repositorio de [Cosmos](https://cosmos.network/docs/gaia/delegator-guide-cli.html#table-of-contents)_

<sumary>
  
<h1 align="center">Guía para el Delegador (CLI):</h1>
</sumary>
<details>
 
Este documento contiene toda la información necesaria para que los delegadores interactúen con el Cosmos Hub a través de la Interfaz Comando-Línea (CLI).

<br>

_También contiene instrucciones sobre cómo administrar las cuentas, restaurar las cuentas desde la recaudación de fondos y usar un dispositivo LedgerNano._
</details>

<sumary>
<h2 align="center">Cuentas de Cosmos:</h2>
<br>
<details>
En el centro de cada cuenta del Cosmos, hay una semilla, que toma la forma de una mnemotecnia de 12 o 24 palabras. Desde esta mnemotecnia, es posible crear cualquier número de cuentas Cosmos, es decir, pares de claves privadas/llaves públicas. Esto se denomina billetera HD (ver <a href="https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki">BIP32</a> para más información sobre la especificación de la billetera HD)

_Los fondos almacenados en una cuenta son controlados por la clave privada. Esta clave privada se genera utilizando una función unidireccional de la mnemotécnica. Si pierde la clave privada, puede recuperarla usando la mnemotécnica. Sin embargo, si pierde la mnemotécnica, perderá el acceso a todas las claves privadas derivadas. Del mismo modo, si alguien obtiene acceso a tu mnemotécnica, obtiene acceso a todas las cuentas asociadas._
</details>
</sumary>

<sumary>
<h2 align="center">Restaurar una cuenta de la recaudación de fondos:</h2>
<br>
<details>

_Si usted participó en la recaudación de fondos, debe tener en su poder una mnemotécnica de 12 palabras. Los mnemónicos recién generados usan 24 palabras, pero los mnemónicos de 12 palabras también son compatibles con todas las herramientas de Cosmos._
</details>
</sumary>

<sumary>
<h2 align="center">En una Ledger:</h2>
<br>
<details>
En el núcleo de un dispositivo Ledger, hay una mnemotécnica utilizada para generar cuentas en múltiples cadenas de bloques (incluyendo el Cosmos Hub). Normalmente, creará una nueva mnemotécnica cuando inicialice el dispositivo Ledger. Sin embargo, es posible decirle al dispositivo Ledger que utilice un mnemotécnico proporcionado por el usuario. Sigamos adelante y veamos cómo puedes introducir la mnemotécnica que obtuviste durante la recaudación de fondos como la semilla de tu dispositivo Ledger.

Los siguientes pasos deben realizarse en un dispositivo de ledger no inicializado:

1. Conecte su dispositivo Ledger al ordenador a través de USB

2. Presione ambos botones

3. NO elija la opción "Configurar como nuevo dispositivo". En su lugar, elija "Restaurar configuración".

4. Elija un PIN

5. Elija la opción de 12 palabras

6. Ingrese cada una de las palabras que recibió durante la recaudación de fondos, en el orden correcto.

_Su ledger está ahora correctamente configurado con su mnemotécnico de recaudación de fondos! No pierdas este mnemotécnico! Si su Ledger está comprometida, siempre puede restaurar un nuevo dispositivo utilizando la misma mnemotécnica._
</details>
</sumary>


<sumary>
<h2 align="center">Creando una cuenta:</h2>
<details>

_Para crear una cuenta, sólo necesitas tener instalado `gaiacli`. Antes de crearlo, necesita saber dónde desea almacenar e interactuar con sus claves privadas. Las mejores opciones son almacenarlas en un ordenador dedicado sin conexión o en una Ledger wallet. Almacenarlas en su computadora en línea implica más riesgo, ya que cualquiera que se infiltre en su computadora a través de Internet podría extraer sus claves privadas y robar sus fondos._
</details>
</sumary>

<sumary>
<h2 align="center">Usando una Ledger wallet:</h2>
<details>

Al inicializar la Ledger, se genera una mnemotécnica de 24 palabras que se almacena en el dispositivo. Esta mnemotécnica es compatible con Cosmos y de ella se pueden derivar cuentas del Cosmos. Por lo tanto, todo lo que tienes que hacer es hacer tu libro de contabilidad compatible con gaiacli. Para ello, debe seguir los siguientes pasos:

1. Descargue la aplicación Ledger [aquí](https://www.ledger.com/pages/ledger-live).

2. Conecte su Ledger a través de USB y actualícelo con el firmware más reciente.

3. Vaya a la tienda de aplicaciones de Ledger y descargue la aplicación "Cosmos" (_esto puede tardar un poco_). Nota: Para poder descargar la aplicación "Cosmos", es posible que tenga que habilitar el `modo de desarrollo` en la `configuración` del Ledger Live.

4. Navegue hasta la aplicación Cosmos en su Ledger.

Luego, para crear una cuenta, use el siguiente comando:
```
gaiacli keys add <NombreDeLaCuenta> --ledger 
```

* `NombreDeLaCuenta` es el nombre de la cuenta. Es una referencia al número de cuenta utilizado para derivar el par de claves de la mnemotécnica. Usted usará este nombre para identificar su cuenta cuando quiera enviar una transacción.

* Puede añadir el indicador opcional `--account` para especificar la ruta (`0`, `1`, `2`,...) que desea utilizar para generar su cuenta. Por defecto, se genera la cuenta `0`.
</details>
</sumary>


<sumary>
<h2 align="center">En un ordenador:</h2>
<details>

Para restaurar una cuenta utilizando una nemotécnica de recaudación de fondos y almacenar la clave privada cifrada asociada en un ordenador, utilice el siguiente comando:

```
gaiacli keys add --recover <NombreDeWallet>
```

Se le pedirá que introduzca una frase de contraseña que se utiliza para cifrar la clave privada de la cuenta `0` en el disco. Cada vez que desee enviar una transacción, se le solicitará esta contraseña. Si pierdes la contraseña, siempre puedes recuperar la clave privada con la mnemotécnica.

* `<NombreDeWallet>`  es el nombre de la cuenta. Es una referencia al número de cuenta utilizado para derivar el par de claves de la mnemotécnica. Usted usará este nombre para identificar su cuenta cuando quiera enviar una transacción.

* Puede añadir el indicador opcional `--account` para especificar la ruta (0, 1, 2,...) que desea utilizar para generar su cuenta. Por defecto, se genera la cuenta `0`.
</details>
</sumary>

<br>


**En [este](/scriptsTestnet/) directorio se pueden encontrar algunos scripts para usar en la testnet que ayudan a gestionar los fondos de Cosmos.**

**En [este](/scriptsMainnet/) directorio se pueden encontrar algunos scripts para usar en la mainnet que ayudan a gestionar los fondos de Cosmos.**

<sumary>
<h2 align="center">¿Como usar los scripts?</h2>
<br>
<details>

* Para poder usar los scripts necesitamos clonar el repositorio y darle permisos de ejecución a los mismos.

1. Clonamos el repositorio en nuestro ordenador:

    `git clone https://github.com/Colm3na/Cosmos-Delegators.git`

2. Entramos en el directorio que contiene los scripts y le damos permisos de ejecución a los scripts(`chmod +x`):

    `cd Cosmos-Delegators/scripts/`

    `chmod +x *`

3. Ejecutamos los scripts poniendo `./` + el nombre del script (debemos estar en el directorio scripts):

    > Ej:
    `./balance`

</details>
</sumary>