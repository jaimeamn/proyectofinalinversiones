# MY COMPRAVENTA DE CRIPTOS

## General Info
***
Proyecto que esta dirigo a ser una aplicaion WEB encargada de realziar compraventa de criptos, se hace  un registro de inversiones y compra/venta de criptos para jugar con los valores a ver si podemos hacer crecer nuestra inversión en euros o no. Para ello nos vamos a crear una aplicación en flask que consultará el valor real en euros de las siguientes criptomonedas: EUR, BTC, ETH, BCH, BNB, LINK, LUNA, ATOM, SOL, USDT.
El proyecto aun no esta terminado falta mostrar en pantalla del usuario el resultado despues de genrar ua lista de compra y venta de monedas en este caso seria mostrar en pantalla valor **invertido**  **valor actual** **valor de resultado**, ademas de control de algunos  posibles errores y todos los detalles que se puedan hacer para que sea amigable con el usuario
* La consultas de valores relativos entre estas criptomonedas se harán utilizando la api siguiente [COIN-API](https://www.coinapi.io/)

* para ello habrá que obtener la api key según sus instrucciones y utilizaremos el siguiente
endpoint de los que están en el plan básico que es gratuito. A saber [url](https://rest.coinapi.io/v1/exchangerate/{base}/{quota}?time={time}&apikey={apikey})
***
## Technologies
***
* Python 
* framework flask
* JavaScript, HTML, CSS, Bootstrap
* Gestor de Base Datos sqlite
* Maquina con sistema Windows 10

## Installation
A little intro about the installation. 
***
**Crear entorno virtual**
 python -m venv venv

**Activar entorno virtual**
macOS: . venv/bin/activate

Windows: venv\Scripts\activate

pip install -r requirements.txt

**crea base de datos**
Crear una base de datos desde el mandato sql que se encuentra en Basedatos/crea_tablas.sql

## Clonar repositorio
```
$ git clone https://github.com/jaimeamn/proyectofinalinversiones.git
$ cd ../path/to/the/file
$ npm install
$ npm start
```
## Lanzar la aplicacion Flask
Desde el terminal

flask run

