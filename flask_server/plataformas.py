# !/usr/bin/env python3
# -----------------------------------------------------------------------------
#             IE-0117 Programación Bajo Plataformas Abiertas
#                      Proyecto Python: App Código QR
#                               Grupo 06
#        Generador  QR: Samuel Berrocal Soto.   samuel.berrocal@ucr.ac.cr
#        Escáner    QR: Mario Benavides
#        GUI          : David Campos Espinoza
# -----------------------------------------------------------------------------
# Clase principal.
import qrcode
import cv2
# Otras clases útiles.
from PIL import Image       # Para mostrar las imágenes.
from time import sleep      # Para crear un delay en la ejecución de código.
import yaml                 # Para darle formato al texto en el código QR.


def informacion_contacto(nombre, apellido, cedula, telefono):
    informacion_contacto = {}
    informacion_contacto['Nombre'] = nombre
    informacion_contacto['Apellido'] = apellido
    informacion_contacto['Cedula'] = cedula
    informacion_contacto['Telefono'] = telefono
    qr_informacion_contacto = yaml.dump(
         informacion_contacto, sort_keys=False,
         default_flow_style=False
         )
     # Para guardar la imagen.
    img = qrcode.make(qr_informacion_contacto)
    type(img)
    img.save('./flask_server/static/informacion_contacto.jpg', 'JPEG')
    # Para mostrar la imagen.
    img_saved = Image.open('./flask_server/static/informacion_contacto.jpg')
    #img_saved.show()

def texto_simple(texto):
    texto_simple = str(texto)
    img = qrcode.make(texto_simple)
    type(img)
    img.save('./flask_server/static/informacion_texto.jpg', 'JPEG')
    # Para mostrar la imagen.
    img_saved = Image.open('./flask_server/static/informacion_texto.jpg')
    #img_saved.show()

def informacion_covid(fecha1, marca1, lote1, fecha2, marca2, lote2):
    informacion_covid1 = {}
    informacion_covid1['Fecha (primera dosis)'] = fecha1
    informacion_covid1['Nombre Vacuna (primera dosis)'] = marca1
    informacion_covid1['Lote Vacuna (primera dosis)'] = lote1
    informacion_covid1['Fecha (segunda dosis)'] = fecha2
    informacion_covid1['Nombre Vacuna (segunda dosis)'] = marca2
    informacion_covid1['Lote Vacuna (segunda dosis)'] = lote2
    qr_informacion_covid = yaml.dump(
         informacion_covid1, sort_keys=False,
         default_flow_style=False
         )
     # Para guardar la imagen.
    img = qrcode.make(qr_informacion_covid)
    type(img)
    img.save('./flask_server/static/informacion_covid.jpg', 'JPEG')
    # Para mostrar la imagen.
    img_saved = Image.open('./flask_server/static/informacion_covid.jpg')
    #img_saved.show()

def decode_contacto():
    # Decodifica
    decode = cv2.QRCodeDetector()
    datos, _, _ = decode.detectAndDecode(
        cv2.imread("/home/david/Escritorio/campos_sevice/flask_server/static/informacion_contacto.jpg"))
    print(datos)
    return datos
def decode_texto():
    # Decodifica
    decode = cv2.QRCodeDetector()
    datos, _, _ = decode.detectAndDecode(
        cv2.imread("/home/david/Escritorio/campos_sevice/flask_server/static/informacion_texto.jpg"))
    print(datos)
    return datos
def decode_vacuna():
    # Decodifica
    decode = cv2.QRCodeDetector()
    datos, _, _ = decode.detectAndDecode(
        cv2.imread("/home/david/Escritorio/campos_sevice/flask_server/static/informacion_covid.jpg"))
    print(datos)
    return datos


#informacion_contacto('David', 'Campos', 504200023, 85601373)
#texto_simple('Programación Bajo Plataformas Abiertas')
#informacion_covid(27022021,'Pfizer', 123213, 25942021, 'AstraZeneca', 12321)
#decode()
