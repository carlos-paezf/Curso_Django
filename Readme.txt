Para crear un proyecto en Django en un entorno local, debemos ingresar a la consola de comandos en Windows,
desplazarnos a la carpeta donde se planea empezar el proyecto e ingresar el siguiente comando:

	django-admin startproject <NombreProyecto>			(1)

Para permitir que el proyecto se conecte a una BBDD debemos ingresar a la cmd y ubicarnos dentro del proyecto 
creado, posteriormente se ingresa el siguiente comando:

	python manage.py migrate					(2)

Para ejecutar un servidor de pruebas integrado con Django, ingresamos el siguiente comando en cmd:
	
	python manage.py runserver					(3)

Por medio del comando anterior se genera la ruta por la que podemos ingresar a nuestro navegador y observar el 
servidor de pruebas. La linea dice lo siguiente:
	
	Starting development server at http://127.0.0.1:8000/		(4)

Esa direccion es igual a ingresar en el navegador 	localhost:8000
Cada vez que se desee entrar al modo debug, si el servidor ha sido detenido, ejecutar el comando (3)

Django hace uso del patrón MTV (Model Template View), el cual sigue la misma filosofia del modelo MVC (Model View Controller).
Este patron permite que sea un modelo funcional, facil de mantener y escalable.

Cada vez que se crea un vista dentro del arhivo views.py, para poder darle una ruta, nos dirigimos al archivo urls.py
Dentro de dicho archivo, importamos la vista que deseamos traer, y en la tupla de urlpatterns ingresamos un nuevo 
elemento, o en este caso, una nueva url, donde se indica la url y la vista que deseamos mostrar