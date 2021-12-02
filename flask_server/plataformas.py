# !/usr/bin/env python3
import qrcode
import cv2
import yaml


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
    img = qrcode.make(qr_informacion_contacto)
    type(img)
    img.save('./flask_server/static/informacion_contacto.jpg', 'JPEG')


def texto_simple(texto):
    texto_simple = str(texto)
    img = qrcode.make(texto_simple)
    type(img)
    img.save('./flask_server/static/informacion_texto.jpg', 'JPEG')


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

    img = qrcode.make(qr_informacion_covid)
    type(img)
    img.save('./flask_server/static/informacion_covid.jpg', 'JPEG')


def decode_contacto():
    decode = cv2.QRCodeDetector()
    datos, _, _ = decode.detectAndDecode(
        cv2.imread("./flask_server/static/informacion_contacto.jpg"))
    print(datos)
    return datos


def decode_texto():
    decode = cv2.QRCodeDetector()
    datos, _, _ = decode.detectAndDecode(
        cv2.imread("./flask_server/static/informacion_texto.jpg"))
    print(datos)
    return datos


def decode_vacuna():
    decode = cv2.QRCodeDetector()
    datos, _, _ = decode.detectAndDecode(
        cv2.imread("./flask_server/static/informacion_covid.jpg"))
    print(datos)
    return datos
