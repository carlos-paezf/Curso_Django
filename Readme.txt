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