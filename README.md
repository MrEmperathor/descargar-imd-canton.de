# Script Para Descargar Imagenes de Canton.de

_Scipt sencillo para descargar imagenes optimizadas con su respectiva variacion de productos_



## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._


### Pre-requisitos 📋

_Librerias necesarias_

```
from bs4 import BeautifulSoup
from googletrans import Translator
import requests
import shutil
import os
import tinify
import pandas as pd
```

### Instalación 🔧

_Para instalar las librerias_


```
pip install requests
pip install shutil
pip install tinify
pip install pandas
pip install googletrans==3.1.0a0
```

_Finaliza con un ejemplo de cómo obtener datos del sistema o como usarlos para una pequeña demo_

## Ejecutando las pruebas ⚙️

_Para ejecutarlo_


```
python descargar_img_canton.py
```

_Seleccionamos una de las 3 keys disponibles. Esto se hace para evitar algun tipo de limite maduro con la api de tynipng_


```

$ Numero key [1,2,3]: 
```

_Pegamos la url del producto el cual vamos a descargar las imagenes_

```
# https://www.canton.de/de/produkte/reference-k/smart-reference-5-k?number=04114
$ URL DEL PRUDUCTO: 
```


_Agregar la cantidad de imagenes que se descargaran para la variacion predefinda por el script_

```
$ Cantidad de enlaces para la variacion --->: Acabado piano lacado blanco:
```


_Agregar la cantidad de imagenes que se descargaran para la variacion predefinda por el script_

```
$ Cantidad de enlaces para la variacion --->: Acabado piano lacado blanco:
```


_una ves indicada la cantidad de enlaces, procedemoos a pegar los enlaces de las imagenes._
_Recomiendo utilizar una extencion de su navegadoor para obtener los enlaces de las imagenes_

* [Link Grabber](https://chrome.google.com/webstore/detail/link-grabber/caodelkhipncidmoebgbbeemedohcdma) - Navegador Google Chrome

```
$ ingresar url:
```

