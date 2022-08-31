# Pasos para instalar y trabajar con flask

1.- Crear un entorno virtual
2.- A los requerimientos del entorno virtual agregar flask
3.- Instalar flask mediante pip
4.- Crear nuetros archivo python principal main.py
    -Importamos el modulo de flask
    -Creamos una instancia a flask para inicializarlo
    -Creamos una funcion con su decorador @app.route('/') la cual contendra el manejo de las respuestas para esto necesitamos el modulo make_response e instanciar una variable que contendra la respuesta que genera el servidor
    -Creamos una carpeta llamada templates donde flask automaticamente buscara los archivos html segun los vayamos utilizando
    -Dentro de la carpeta templates creamos nuestro index y podemos crear archivos extras que importaremos dentro del index

5.- Para incializar nuestro servidor debemos seguir los siguientes pasos:
        1.- Instanciar una variable en la terminal export FLASK_APP=main.py esta variable debe contener el nombre de nustro archivo principal de python
        2.- Instanciar la variable para entorno de desarrollador con el nombre y valor export FLASK_DEBUG=1
        3.- Ejecutar el comando flask run para inciar el servidor

6.- Dentro de nuestro archivo blocks crearemos un bloque llamado contenido el cual importaremos en nuestro index
        -Cada bloque debe tener la sintaxis {% block nombre %} y se debe de cerrar usando {% endblock %}
        -Una vez creado el bloque podemos escribir HTML o codigo python usando los caractesres {% expresion %} para mandar a llamar variables se usa {{ nombre_variable }}

7.- Para poder anadir nuestro bloque a otro archivo debemos de extenderlo dentro del archivo para esto se usa:
        {% extends 'nombredelarchivo.html' %}
        Una vez que extendimos podemos incluir nuestro bloque en el nuevo html usando:
            {% block nombredelblock %}
            {% endblock %}