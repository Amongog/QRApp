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

# Inicialización de estructuras de datos.
informacion_contacto = {}
texto_simple = ''
informacion_vacuna = {}

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
            print('| (3) Información de vacuna (COVID-19).  |')
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
                    print('| Seleccione la opción deseada.          |')
                    print('| (0) Regresar.                          |')
                    print('| (1) Nombre(s).                         |')
                    print('| (2) Apellidos.                         |')
                    print('| (3) Cédula de Identidad.               |')
                    print('| (4) Teléfono.                          |')
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

                    elif(opcion_contacto == 2):
                        print('\n******************************************')
                        print('|----------------------------------------|')
                        print('|Digite sus apellidos.                   |')
                        print('|----------------------------------------|')
                        print('******************************************')

                        informacion_contacto['Apellidos'] = str(input('» '))

                    elif(opcion_contacto == 3):
                        print('\n******************************************')
                        print('|----------------------------------------|')
                        print('|Digite su cédula de identidad.          |')
                        print('|----------------------------------------|')
                        print('******************************************')

                        informacion_contacto['Cedula'] = str(input('» '))

                    elif(opcion_contacto == 4):
                        print('\n******************************************')
                        print('|----------------------------------------|')
                        print('|Digite su número de teléfono.           |')
                        print('|----------------------------------------|')
                        print('******************************************')

                        informacion_contacto['Telefono'] = str(input('» '))

                    elif(opcion_contacto == 5):
                        print('\n******************************************')
                        print('|----------------------------------------|')
                        print('|        Generando código QR ...         |')
                        print('|----------------------------------------|')
                        print('******************************************')
                        qr_informacion_contacto = yaml.dump(
                            informacion_contacto, sort_keys=False,
                            default_flow_style=False
                            )
                        # Para guardar la imagen.
                        img = qrcode.make(qr_informacion_contacto)
                        type(img)
                        img.save('informacion_contacto.jpg', 'JPEG')
                        # Para mostrar la imagen.
                        img_saved = Image.open('informacion_contacto.jpg')
                        img_saved.show()

                    else:
                        print(
                            '\n!!! Ingrese una opción válida (╯°□°）╯︵ ┻━┻ !!!'
                        )
                        sleep(2)

            elif(tipo_qr == 2):
                while True:

                    print('\n******************************************')
                    print('|----------------------------------------|')
                    print('|     Generar Mensaje de Texto           |')
                    print('|----------------------------------------|')
                    print('| Seleccione la opción deseada.          |')
                    print('| (0) Regresar.                          |')
                    print('| (1) Ingresar texto.                    |')
                    print('| (2) Generar QR.                        |')
                    print('|----------------------------------------|')
                    print('******************************************')

                    opcion_texto = int(input('» '))

                    if(opcion_texto == 0):
                        break

                    elif(opcion_texto == 1):
                        print('\n******************************************')
                        print('|----------------------------------------|')
                        print('|Ingrese el mensaje de texto.            |')
                        print('|----------------------------------------|')
                        print('******************************************')

                        texto_simple = str(input('» '))

                    elif(opcion_texto == 2):
                        print('\n******************************************')
                        print('|----------------------------------------|')
                        print('|        Generando código QR ...         |')
                        print('|----------------------------------------|')
                        print('******************************************')
                        # Para guardar la imagen.
                        img = qrcode.make(texto_simple)
                        type(img)
                        img.save('texto_simple.jpg', 'JPEG')
                        # Para mostrar la imagen.
                        img_saved = Image.open('texto_simple.jpg')
                        img_saved.show()

                    else:
                        print(
                            '\n!!! Ingrese una opción válida (╯°□°）╯︵ ┻━┻ !!!'
                        )
                        sleep(2)

            elif(tipo_qr == 3):
                while True:

                    print('\n******************************************')
                    print('|----------------------------------------|')
                    print('|Generar Información de Vacuna (COVID-19)|')
                    print('|----------------------------------------|')
                    print('| Seleccione la opción deseada.          |')
                    print('| (0) Regresar.                          |')
                    print('| (1) Fecha (primera dosis).             |')
                    print('| (2) Nombre de vacuna (primera dosis).  |')
                    print('| (3) Lote vacuna (primera dosis).       |')
                    print('| (4) Fecha (segunda dosis).             |')
                    print('| (5) Nombre de vacuna (segunda dosis).  |')
                    print('| (6) Lote vacuna (segunda dosis).       |')
                    print('| (7) Generar QR.                        |')
                    print('|----------------------------------------|')
                    print('******************************************')

                    opcion_vacuna = int(input('» '))

                    if(opcion_vacuna == 0):
                        break

                    elif(opcion_vacuna == 1):
                        print('\n******************************************')
                        print('|----------------------------------------|')
                        print('|Digite la fecha de la primera dosis.    |')
                        print('|----------------------------------------|')
                        print('******************************************')

                        informacion_vacuna[
                            'Fecha de Primera Dosis'] = str(input('» '))

                    elif(opcion_vacuna == 2):
                        print('\n******************************************')
                        print('|----------------------------------------|')
                        print('|Digite el nombre de la farmacéutica para|')
                        print('|la primera dosis.                       |')
                        print('|----------------------------------------|')
                        print('******************************************')

                        informacion_vacuna[
                            'Nombre de la Vacuna de la Primera Dosis'
                            ] = str(input('» '))

                    elif(opcion_vacuna == 3):
                        print('\n******************************************')
                        print('|----------------------------------------|')
                        print('|Digite el número de lote de la primera  |')
                        print('|dosis.                                  |')
                        print('|----------------------------------------|')
                        print('******************************************')

                        informacion_vacuna[
                            'Numero de Lote de la Primera Dosis'
                            ] = str(input('» '))

                    elif(opcion_vacuna == 4):
                        print('\n******************************************')
                        print('|----------------------------------------|')
                        print('|Digite la fecha de la segunda dosis.    |')
                        print('|----------------------------------------|')
                        print('******************************************')

                        informacion_vacuna[
                            'Fecha de Segunda Dosis'] = str(input('» '))

                    elif(opcion_vacuna == 5):
                        print('\n******************************************')
                        print('|----------------------------------------|')
                        print('|Digite el nombre de la farmacéutica para|')
                        print('|la segunda dosis.                       |')
                        print('|----------------------------------------|')
                        print('******************************************')

                        informacion_vacuna[
                            'Nombre de la Vacuna de la Segunda Dosis'
                            ] = str(input('» '))

                    elif(opcion_vacuna == 6):
                        print('\n******************************************')
                        print('|----------------------------------------|')
                        print('|Digite el número de lote de la segunda  |')
                        print('|dosis.                                  |')
                        print('|----------------------------------------|')
                        print('******************************************')

                        informacion_vacuna[
                            'Numero de Lote de la Segunda Dosis'
                            ] = str(input('» '))

                    elif(opcion_vacuna == 7):
                        print('\n******************************************')
                        print('|----------------------------------------|')
                        print('|        Generando código QR ...         |')
                        print('|----------------------------------------|')
                        print('******************************************')
                        qr_informacion_vacuna = yaml.dump(
                            informacion_vacuna, sort_keys=False,
                            default_flow_style=False
                            )
                        # Para crear la imagen.
                        img = qrcode.make(qr_informacion_vacuna)
                        type(img)
                        img.save('informacion_vacuna.jpg', 'JPEG')
                        # Para mostrar la imagen.
                        img_saved = Image.open('informacion_vacuna.jpg')
                        img_saved.show()

                    else:
                        print(
                            '\n!!! Ingrese una opción válida (╯°□°）╯︵ ┻━┻ !!!'
                        )
                        sleep(2)

    elif(accion_principal == 2):
        while True:

            print('\n******************************************')
            print('|----------------------------------------|')
            print('|         Lector de Códigos QR           |')
            print('|----------------------------------------|')
            print('| Seleccione el QR que desea decodificar.|')
            print('| (0) Regresar.                          |')
            print('| (1) informacion_contacto.jpg           |')
            print('| (2) texto_simple.jpg                   |')
            print('| (3) informacion_vacuna.jpg             |')
            print('|----------------------------------------|')
            print('******************************************')

            tipo_lectura = int(input('» '))

            if(tipo_lectura == 0):
                break

            elif(tipo_lectura == 1):
                # Decodifica
                decode = cv2.QRCodeDetector()
                # dato, ____ , ___
                datos, _, _ = decode.detectAndDecode(
                    cv2.imread("informacion_contacto.jpg"))

                print('\n******************************************')
                print('|----------------------------------------|')
                print('|        Decodificando código QR ...     |')
                print('|----------------------------------------|')
                print('******************************************')
                print(datos)

            elif(tipo_lectura == 2):
                # Decodifica
                decode = cv2.QRCodeDetector()
                # dato, ____ , ___
                datos, _, _ = decode.detectAndDecode(
                    cv2.imread("texto_simple.jpg"))

                print('\n******************************************')
                print('|----------------------------------------|')
                print('|        Decodificando código QR ...     |')
                print('|----------------------------------------|')
                print('******************************************')
                print(datos)

            elif(tipo_lectura == 3):
                # Decodifica
                decode = cv2.QRCodeDetector()
            # dato, ____ , ___
                datos, _, _ = decode.detectAndDecode(
                    cv2.imread("informacion_vacuna.jpg"))

                print('\n******************************************')
                print('|----------------------------------------|')
                print('|        Decodificando código QR ...     |')
                print('|----------------------------------------|')
                print('******************************************')
                print(datos)

            else:
                print('\n!!! Ingrese una opción válida (╯°□°）╯︵ ┻━┻ !!!')
                sleep(2)

    else:
        print('\n!!! Ingrese una opción válida (╯°□°）╯︵ ┻━┻ !!!')
        sleep(2)
