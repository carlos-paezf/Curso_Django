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
Dentro de dicho archivo, importamos la vista que deseamos traer, y en la lista de urlpatterns ingresamos un nuevo 
elemento, o en este caso, una nueva url, donde se indica la url y la vista que deseamos mostrar
Dentro de las funciones de las views, podemos hacer inserciones de codigo HTML, permitiendo asi, darle formato
al rexto que deseamos mostrar. 

Django tiene una caracterisitica llamada URL friendly, lo cual permite que no hayan caracteres extraños que generen
error al indexar una página. Se intenta evitar que al pasar parametros por la URL se implementen simbolos comunes en 
otros lenguaje como php, el cual manera el simbolo ? para pasar un parametro. En el caso de Django, los parametros
se pasan por medio de <>.

En Django encontramos las Plantillas, las cuales permiten cadenas de texto (HTML casi siempre) que sirven para separar
la parte logica o datos, de la parte visual o presentacion de un documento web. Para emplearlas, existen diversas formas
pero la mas habitual es guardar la cadena de texto en un documento independiente y cargarlo a la vista. Esto evita que 
se inserten las cadenas de texto de manera rudimentaria dentro de las vistas en views. Al hacer esto, se pueden realizar
cambios en el diseño con independencia del codigo de la vista, tambien se puede diversificar el trabajo del proyecto, y 
tambien permite que se pueda trabajar a la vez ambas disciplinas (logica y diseño). Para crear las plantillas existen unos 
pasos: Crear objeto de tipo template - Crear un contexto (Datos adicionales para el template [variables, funciones, etc...])
- Renderizar el objeto template.
Desde una plantilla podemos acceder a las variables que declaramos en las vistas, para esto, creamos un diccionario 
dentro del contexto asignando la llave-valor correspondiente. Posteriormente en el Template, podemos acceder a las llaves 
mediante {{llave}}, esto tambien nos permite acceder a las propiedades que posea dicha variable. Tambien podemos usar la
Programación Orientada a Objetos y la nomenclatura del punto para acceder a dichas propiedades.
Dentro de las plantillas encontramos una jerarquia u orden de llamadas -> Diccionario-Atributo-Método-Índice de lista

Aunque en las plantillas se pueden ingresar estructuras de control de flujo, no es recomendable abusar de ellas, ya que el 
modelo MTV busca que la logica se separe de la parte grafica, esto permite el multitrabajo en un grupo o proyecto.
Para usar un filtro, empleamo el simbolo tuberia "|", por ejemplo "nombre|upper", si queremos encadenar filtros seguimos usando
las tuberias, por ejemplo, "nombre|first|lower"
Para emplear los cargadores, se ingresa el directorio raiz donde se encuentran todas las plantillas dentro del apartado 'DIRS':[]
de la lista TEMPLATES ubicada en el archivo settings.py, Cuando se empieza a emplear los cargadores, la sintaxis cambia a la 
manjeada de manera rustica, por un lado se simplifican algunas lineas y por otro lado, el metodo .render(), cambia el contexto 
que recibe. Esto se debe el Template que recibe, es diferente al manejado anteriormente. Para solucionar esto, le pasamos por 
parametro un diccionario como contexto, de hecho, es el mismo diccionario que se manejaba como contexto en las vistas rusticas.
En la documentacion de Django encontramos el porque de las diferencias entre los 2 Template. Uno se instancia en 
<class 'django.template.backends.django.Template'> y el otro se instancia en <class 'django.template.base.Template'>

Podemos reutilizar codigo dentro de las plantillas, haciendo uso de una plantilla donde se ingrese el codigo repetido, para luego
incrustarlo en una plantilla especifica. Se debe tener en cuenta el folder en donde se ubique para poder llamarlo, recordando que 
los templates ya estan sido asignados a una direccion en especifico. Para llamarlas, se usa la palabra clave "include".
La herencia de plantillas permite que se tenga una clase padre en la cual ira el codigo fijo, y unas clases hijas que permiten un
codigo cambiente. Para hacer esto, se debe llamar desde la clase hija a la clase padre con la palabra clave "extends".

En Django es importante diferenciar entre una aplicacion y un proyecto. Las aplicaciones son paquetes o modulos que se encargan de
realizar una suma de tareas concretas, esto hace que en proyecto tengamos varias aplicaciones que se encarguen de partes especificas
de la logica. Las tablas de las bases de datos SQLite3 se crean empleando las Clase Model, la cual permite manejar en su totalidad
las tablas de las BBDD. Pero la clase Model debe estar relacionado si o si dentro de una aplicación.
Para crear una aplicacacion usamos el comando dentro del directorio del proyecto:

	python manage.py startapp <nombreAplicacion>			(5)		

Para registrar una aplicacion nos debemos dirigir al archivo settings.py ubicado en la subcarpeta del proyecto. Nos dirigimos a la
lista INSTALLED_APPS, y ponenmos el nombre de la aplicacion que vamos a agregar. Para ver el status de la aplicacion, ingresamos
el comando en consola:

	python manage.py check <nombreAplicacion>			(6)

Para crear la base de datos de nuestra aplicacion, ingresamos el comando:
	
	python manage.py makemigrations					(7)

Cuando ingresamos el comando anterior tendremos el numero de migracion en el siguiente formato: <nombreApp>\migrations\<numMigracion>_initial.py
Para crear el codigo sql de las tablas ingresamos el comando:

	python manage.py sqlmigrate <nombreAplicacion> <numeroMigracion> 		(8)

Para usar dicho codigo sql ingresamos el comando (2).
Para insertar, eliminar o actualizar datos, podemos acceder desde la consola al shell de python, para ello ingresamos:

	python manage.py shell						(9)

Estando en el shell podemos ingresar el siguiente codigo en lenguaje python para añadir un elemento:

	from <nombreApp>.models import <Modelo>
	variable1 = Modelo(llave1='valorChar', llave2=valorInt)
	variable1.save()
o tambien en una sola linea:
	variable2 = Modelo.objects.create(llave1='valorChar', llave2=valorInt)

Ahora para actualizar un elementos escribimos el siguiente codigo

	from <nombreApp>.models import <Modelo>
	variable1.propiedad = valor
	variable1.save()

Para eliminar un registro usamos el codigo:

	from <nombreApp>.models import <Modelo>
	variable3 = Modelo.objects.get(llave=valor)
	variable3.delete()

Para realizar un Select ingresamos el codigo:

	from <nombreApp>.models import <Modelo>
	lista = Modelo.objects.all()
	lista.query.__str__()

Para hacer las conexiones con una BBDD en PostgreSQL, se debe hacer la instalacion de una libreria llamada psycopg2
la cual no viene con Django, para ello ingresamos por consola dentro del directorio del proyecto el siguiente comando:

	pip install psycopg2						(10)

Ahora en el archivo settings.py, en la lista de DATABASES, ingresamos los siguientes cambios:

	'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '<nombre de la BBDD>',
        'USER': '<usuario de conexion a la BBDD>',
        'PASSWORD': '<contraseña de ingreso a la BBDD>',
        'HOST': '<direccion de conexion>',
        'DATABASE_PORT': '<puerto de conexion>',

Repetimos los comandos (7) y (2) en el orden presentado. Para observar los cambios ingresamos a la pagina de conexion
con PostgreSQL, nos dirigimos a la base de datos, luego a la seccion Schemas, y por ultimo a Tables, alli deben estar
las tablas que hemos creado en nuestro proyecto. Posteriormente podemos hacer uso del manejo de registros por consola, 
mientras se aprende el uso de formularios.

Para realizar consultas empleando criterios debemos ingresar al shell de python con el comando (9), y alli ingresamos el siguiente
codigo:

	from <nombreApp>.models import <Modelo>
	Modelo.objects.filter(criterio1='valorChar', criterio2=valorInt, ....)

Para ver la informacion detallada escribimos en archivo models.py, dentro de la clase del modelo deseado, la funcion __str__():
Posteriormente migramos los cambios con el comando (7) y (2) respectivamente, saliendo del shell con exit. Luego podemos 
ingresar al shell y observaremos el cambio. Ahora bien, si en nuestras consultas por shell requerimos usar los operadores '>' o '<', 
debemos hacer un reemplazo por: 

	'>' criterio__gte=valorInt		'<' criterio__lte=valorInt

Para mostrar la informacion de un criterio comprendido entre un valor y otro, usamos la sintaxis: 
	
	criterio__range(num1, num2)

Si queremos ver los registros de manera ordenada ascendentemente segun el filtro, (ORDER BY en lenguaje SQL), concatenamos a la funcion filter la
sintaxis .order_by('criterio')

	from <nombreApp>.models import <Modelo>
	Modelo.objects.filter(criterio1__range=(num1, num2)).order_by('criterio')

Si queremos ver los registros de manera ordenada descendetemente, escribimos la sintaxis:
	
	from <nombreApp>.models import <Modelo>
	Modelo.objects.filter(criterio1__range=(num1, num2)).order_by('-criterio')

Los paneles de administracion en cualquier pagina web, permiten modificar el contenido de la misma, sin hacer cambios gigantescos en 
el codigo. En las ultimas versiones de Django, ya vienen por defecto al crearse el proyecto con el comando (1). Si queremos acceder al 
panel de administracion, ingresamos en el navergador la ruta localhost:8000/admin/ pero necesitamos crear un superusuario y contraseña.
Para crearlo, ingresamos el comando en consola dentro del directorio del proyecto:

	python manage.py createsuperuser				(11)

Por defecto Django nos muestra 2 secciones: Groups y Users. Todos los usuarios que se creen se pueden observar en la base de datos, dentro
de la tabla auth_user. Para manipular las tablas del panel de administracion, nos dirigimos al archivo admin.py y ingresamos el codigo para 
nuestro objetivo. Los campos de las tablas, por defecto, seran requeridos y no opcionales, para cambiar esta opcion modificamos el cogido en
la funcion del modelo en el campo que se puede dejar opcional. Posteriomente ejecutamos los comandos (7) y (2).
Para cambiar el nombre de los campos de una tabla en el panel de administracion debemos dirigirnos al modelo y hacer el cambio en el campo
que deseamos ver reflejado el cambio. Para mostrar de manera personalizada la lista de objetos, creamos una funcion en admin.py y la
instanciamos junto al parametro que se quiere asociar. Para crear un sistema de busqueda, dentro de la misma funcion personalizada, ingresamos
los cambios.
Para agregar filtros debemos agregar funcionalidad en la funcion personalizada del archivo admin.py. Para manejar el panel de administracion
en español, nos dirigimos al archivo settings.py y localizamos la seccion LENGUAGE_CODE y cambiamos a es-CO, es decir, español-Colombia.
Para establecer permisos a los usuarios debemos modificar los usuarios desde el panel de administracion, al igual que asignarselos a los grupos.

Los formularios son importantes para obtener la informacion y enviarla a un servidor. En nuestro proyecto estamos manejando un formulario 
basico en HTML, en cual recordamos manejo de vistas y rutas. Uno de estos formularios es el de envio de emails, para el cual usamos la libreria
core.mail. Debemos buscar un servidor de correo que nos permita usar sus parametros para que desde nuestro framework podamos enviar los correos.
Los parametros los definimos en el archivo settings.py. Si queremos usar G-mail, debemos configurarlo para permitir el acceso a terceros. Luego 
de hacer las configuraciones en el archivo, podemos hacer una prueba con el shell de python, ingresamos el siguiente codigo:

	from django.core.mail import send_mail
	send_mail(
	    'Subject here',
	    'Here is the message.',
	    'from@example.com',
	    ['to@example.com'],
	    fail_silently=False,
	)