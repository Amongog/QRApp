#!/usr/bin/python3
# -----------------------------------------------------------------------------
#             IE-0117 Programación Bajo Plataformas Abiertas
#                      Proyecto Python: App Código QR
#                               Grupo 06
#        Generador  QR: Samuel Berrocal Soto.   samuel.berrocal@ucr.ac.cr
#        Escáner    QR: Mario Benavides
#        UI Design    : David Campos Espinoza
# -----------------------------------------------------------------------------
# Clase principal.
import qrcode
# Otras clases útiles.
# import cv2
from PIL import Image
from time import sleep

# img = qrcode.make("https://www.youtube.com/")
# type(img)
# img.save("youtubeQR.jpg")
# img = Image.open('youtubeQR.jpg')
# img.show(youtubeQR.jpg)

# Inicialización de estructuras de datos.
informacion_contacto = {}
texto_simple = ''
informacion_vacunas = {}

while True:

    print('\n******************************************')
    print('|----------------------------------------|')
    print('|                  QRApp                 |')
    print('|----------------------------------------|')
    print('| Seleccione la opción deseada.          |')
    print('| (0) Salir.                             |')
    print('| (1) Generador de QR.                   |')
    print('| (2) Lector de QR.                      |')
    print('|----------------------------------------|')
    print('******************************************')

    accion_principal = int(input('» '))

    if(accion_principal == 0):
        break

    elif(accion_principal == 1):
        while True:

            print('\n******************************************')
            print('|----------------------------------------|')
            print('|         Generador de Códigos QR        |')
            print('|----------------------------------------|')
            print('| Ingrese el tipo de QR que desea generar|')
            print('| (0) Regresar.                          |')
            print('| (1) Información de contacto.           |')
            print('| (2) Texto simple.                      |')
            print('| (3) Información de vacunación.         |')
            print('|----------------------------------------|')
            print('******************************************')

            tipo_qr = int(input('» '))

            if(tipo_qr == 0):
                break

            elif(tipo_qr == 1):
                while True:

                    print('\n******************************************')
                    print('|----------------------------------------|')
                    print('|     Generar Información de Contacto    |')
                    print('|----------------------------------------|')
                    print('| Seleccione la información deseada.     |')
                    print('| (0) Regresar.                          |')
                    print('| (1) Nombre(s).                         |')
                    print('| (2) Apellidos.                         |')
                    print('| (3) Teléfono.                          |')
                    print('| (4) Email.                             |')
                    print('| (5) Generar QR.                        |')
                    print('|----------------------------------------|')
                    print('******************************************')

                    opcion_contacto = int(input('» '))

                    if(opcion_contacto == 0):
                        break

                    elif(opcion_contacto == 1):
                        print('\n******************************************')
                        print('|----------------------------------------|')
                        print('|Digite su nombre a continuación.        |')
                        print('|----------------------------------------|')
                        print('******************************************')
                        informacion_contacto['Nombre(s)'] = str(input('» '))
                        print('\n', informacion_contacto)

    elif(accion_principal == 2):
        break

    else:
        print('\n!!! Ingrese una opción válida (╯°□°）╯︵ ┻━┻ !!!')
        sleep(2)
