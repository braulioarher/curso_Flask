# Curso de Flask

Para comenzar a trabajar primero debemos de crar un ambiente virtual para esto

    python3 -m venv venv

Despues debemos instalar mediante pip flask pra esto

    pip install flask

Es importante crear un archivo requiremets.txt para saber la dependecias a usarse en este caso agregariamos flask a estas dependencias

Creamos un archivo que se llamara main

Ejecutamos el comando flask run para inicializar nuestro servidor

Dentro de la terminal debemos de instanciar una variable que es export FLASK_APP=main.py

Para actualizar automaticamente los cambios echos debemos de activar el modo debug

Se debe de crear una variable en la consola llamada export FLASK_DEBUG=1

## Template con ninja

Un template de flask es un archivo de html que permite renderizar informacion dinamica y estatica en el ejemplo en lugar de regresar una cadena de texto de python se regresa un archivo html

Flask esta por defecto configurado para buscar en una carpeta llamada templates un archivo html

## Macros

Los macros son pequenos pedazos de codigo reutilizables que se repitenen en varias ocaciones de nuestro template