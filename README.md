# examen_python_miguel_carpio

## Requsitos
Versión Python >= 3.08
Librerías: Colorama

## Como iniciar la aplicación
Abre la terminal
Asegurate de estar situado en el directorio raíz del proyecto
Una vez estes en el directorio hay que ejecutar el siguiente comando "python main.py" opara iniciar el proyecto

## funcionalidad de la aplicación

Al iniciar la aplicación obtendremos un menu como el siguiente:

====================
========Menu Principal========
====================
1. Nueva nota
2. Muestra todas las notas
3. Busca nota por título
4. Muestra nota por contenido
5. Actualiza nota
6. Elimina nota
0. Salir
====================
[+] Elige una tarea:

Para elegir una opción simplemente debemos introducir uno de los indices mostrados en el menu:

[+] Elige una tarea: 1 

Seguidamente pulsamos enter para aceptar
A continuación se mostrará las diferentes funcionalidades de la aplicación accediendo con cada índice

1 - Nueva nota
Se nos abrira el siguiente submenu que nos da la opción de volver hacia atrás
====================
1. Crear nota
0. Volver al menú principal
====================
[+] Elige una tarea:

si elegimos la opción 1 nos pedirá que insertemos un título (el título debe ser único)
[+] Elige una tarea: 1
Inserte el título de la nota: nota de prueba

seguidamente nos pedirá que insertemos el contenido de la nota
Inserte el contenido: el contenido de mi nota

Al final obtendremos un mensaje de éxito al crear la nota
[+] Elige una tarea: 1
Inserte el título de la nota: nota de prueba
Inserte el contenido: el contenido de mi nota
Nota creada exitosamente!

una vez terminado podremos volver a crear otra nota o regresar al menu principal

====================
========Crear nueva nota========
====================
1. Crear nota
0. Volver al menú principal
====================
[+] Elige una tarea:

2 - Muestra todas las notas
nos muestra todas las notas que están creadas en columna

[+] Elige una tarea: 2

Mostrando todas las notas:

==============================
Título: nota de prueba
Contenido: el contenido de mi nota
==============================
==============================
Título: otra nota de prueba
Contenido: otro contenido de prueba
==============================

seguidamente tendremos acceso directamente al nenu principal

3 y 4 - Busca por el título o contenido
Las opciones 3 y 4 funcionan de la misma forma, aunque una es para el título y otra para el contenido

Si elegimos la 3 nos pedirá que introduzcamos un título
[+] Elige una tarea: 3
Inserte el título para buscar: nota de prueba

Si elegimos la 4 nos pedirá que introduzcamos un contenido
[+] Elige una tarea: 4
Inserte el contenido a buscar: contenido

Se buscará por un título o incluso palabra indicada mostrandonos las notas que coinciden
Notas encontradas:

==============================
Título: nota de prueba
Contenido: el contenido de mi nota
==============================
==============================
Título: otra nota de prueba
Contenido: otro contenido de prueba
==============================

5 - Actualizar nota
La quinta opción nos vuelve ha abrir un submenu
[+] Elige una tarea: 5
====================
========Actualizar nota========
====================
1. Actualizar nota
0. Volver al menú principal
====================
[+] Elige una tarea:

Nos pedirá que introduzcamos el título de la nota que queremos actualizar (debe ser el título entero, nada de palabras sueltas)
[+] Elige una tarea: 1
Inserte el título de la nota a actualizar: nota de prueba

Al sinsertar el título nos pedirá el contenido nuevo para actualizar y mostrará el mensaje de realizado
[+] Elige una tarea: 1
Inserte el título de la nota a actualizar: nota de prueba
Ingrese el nuevo contenido: actualizo contenido
Nota actualizada correctamente.

6 - Eliminar
La forma de eliminar es muy parecida a la actualización, abre un submenu también
[+] Elige una tarea: 6
====================
========Eliminar nota========
====================
1. Eliminar nota
0. Volver al menú principal
====================
[+] Elige una tarea:

Al elegir la tarea de eliminar nos pedirá que demos el título de la nota (debe ser el título entero, nada de palabras sueltas)
[+] Elige una tarea: 1
Inserte el título de la nota a eliminar: nota de prueba
Nota eliminada correctamente.

0 - salir
Como su nombre indica se usa para cerrar la aplicación y que deje de funcionar
[+] Elige una tarea: 0
Salir del programa ... Cerrando
