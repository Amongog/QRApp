# QRApp
Aplicación para creación y decodificación de códigos QR con una interfaz gráfica en un servidor web.

Instrucciones para correrlo:
  1. sudo apt install python3-virtualenv

En el directorio de trabajo:
  2. virtualenv venv
  3. source venv/bin/activate
  4. pip install flask
  5. pip install qrcode
  6. pip install yaml
  7. pip install opencv-python
  8. pip install qrcode
... todos los paquetes (yaml, cv2, etc..)
  9. export FLASK_APP="flask_server"
  export FLASK_ENV="development"
  10. flask run
  11. Escribir 127.0.01:5000 en el navegador.
  
Nota: Para el decodificador, se debe modificar el path que contiene plataformas.py en cada
funcón decode, ya que esto varía dependendo dónde el usuario guarda las imágenes.
