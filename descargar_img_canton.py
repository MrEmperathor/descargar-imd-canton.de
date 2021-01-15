#DESCARGAR IMAGENES DE CANTON.DE
from bs4 import BeautifulSoup
from googletrans import Translator
import requests
import shutil
import os
import tinify
import pandas as pd

keyUse = int(input('Numero key [1,2,3]: '))
if keyUse == 1:
    tinify.key = "PTLC4X87kV6dwVmgsv3XmQ6XDPDMGpWK"
elif keyUse == 2:
    tinify.key = "0QM7Lm0n206yMLhm65WKrcQhBrXKSfQR"
else:
    tinify.key = "WWpWQ6pddvXZ4ldvrkZCdnyMf8fcY5QN"

urlp = str(input('URL DEL PRUDUCTO: '))
page = requests.get(urlp)
soup = BeautifulSoup(page.content, 'html.parser')

#Titulo del producto
titulo = soup.find_all('h1', class_='product--title')[0].text
print(titulo)
if os.path.exists(titulo):
    print('carpeta ' + titulo + ' creada')
else:
    os.mkdir(titulo)

#Nombre de variaciones
try:

    vari = soup.find_all('div', class_="select-field")[0]

except:
    print('No hay Variaciones')
    v = [titulo]

if vari:
    space = vari.text.split('  ')
    for es in space:
        if len(es) > 2:
            spaceA = es.split(' ')

    if len(spaceA) > 4:
        v = [titulo]
    else:
        v = vari.text.split('  ')

nameVariaciones = list()
translator = Translator()

#Traduciendo variaciones
for s in v:
    if len(s) > 2:
        tradu = translator.translate(s.replace('"', ''), src="de", dest='es')
        nameVariaciones.append(tradu.text.replace('"', ''))

#Obteniendo enlaces de productos
listurl = {}
for cantUrl in nameVariaciones:
    cantidadEnlaces = list()
    cantidadU = int(input('Cantidad de enlaces para la variacion --->: ' + str(cantUrl) + str(': ')))
    i = 1
    while i <= cantidadU:
        cantidadEnlaces.append(str(input('ingresar url: ')))
        i +=1
    listurl[cantUrl] = cantidadEnlaces

    if os.path.exists(cantUrl):
        print('carpeta ' + cantUrl + ' creada')
    else:
        folder = titulo + cantUrl
        os.mkdir(folder)

    del(cantidadEnlaces)
    del(cantidadU)
    
name = titulo

#Importanto imagenes desde la url a la api de Tynipng y obteniendo las imagenes comprimidas en su respectiva carpeta
for nameVaria in nameVariaciones:
    vv = int(1)
    folder = titulo + nameVaria
    for line in listurl[nameVaria]:
        url = line.rstrip()
        print(line)
        print('Optimizando imagen: ' + url)
        extencion = url.split('.')
        namee = name + str(" ") + str(vv) + str('.') + extencion[-1]
        print(namee)
        response = requests.get(url)
        if response.status_code == 200:
            source = tinify.from_url(url)
            source.to_file(namee)
            shutil.move(namee, folder)
        else:
            print('Error al acceder a la url')

        vv = vv + 1
    shutil.move(folder, titulo)
print('proceso terminado')

