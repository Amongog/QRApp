# QRApp
Aplicación para creación y decodificación de códigos QR con una interfaz gráfica en un servidor web.

Instrucciones para correrlo:
  1. sudo apt install python3-virtualenv

En el directorio de trabajo:

  2. virtualenv venv

  4. source venv/bin/activate

  6. pip install flask

  8. pip install qrcode

  10. pip install pyyaml

  12. pip install opencv-python

  14. pip install qrcode

  16. ... todos los paquetes (yaml, cv2, etc..)

  18. export FLASK_APP="flask_server"

  20. export FLASK_ENV="development"

  22. flask run

  24. Escribir 127.0.01:5000 en el navegador.
  
Nota: Para el decodificador, se debe modificar el path que contiene plataformas.py en cada
funcón decode, ya que esto varía dependendo dónde el usuario guarda las imágenes.
