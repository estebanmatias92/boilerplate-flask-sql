# boilerplate-flask-sql

Plantilla base para crear web apps con persistencia.

## Sinopsis del juego

Es una simple app web de tareas (TO-DO), hecha en Flask + Bootstrap + SQlite3.

- La arquitectura de la applicacion responde a MVC
- El controlador esta representado en las 'routes'
- Las vistas estan representadas en los 'templates'
- Los metodos CRUD estan en las 'routes' (por cuestion de tiempo, lo dejo asi, pero podrian ir dentro del modelo 'Todo')
- La base de datos se va a crear, junto con la carpeta 'instance' en el root del proyecto, la primera vez que corra la app
- La configuracion de la base de datos se encuentra en 'db/database.py'
- 'static' no esta siendo usado en este caso, por el uso de bootstrap desde un CDN, pero esta disponible

## Instalacion

Deben instalar desde la consola la libreria Pygame (asegurense de tener actualizado PIP)

```bash
pip install -Ur .\requirements.txt 
```

- En el archivo 'requirements.txt' se encuentra la libreria listada

## Scaffolding (organizacion de carpetas)

```bash
.
│   .gitignore
│   app.py
│   requirements.txt
│
├───db
│       database.py
│
├───models
│       Todo.py
│
├───routes
│       todo.py
│
├───static
│   ├───css
│   │       style.css
│   │
│   └───js
└───templates
        edit_task.html
        index.html
```

## Uso

Como cualquier script o programa de python.

```bash
python "app.py"
```

*Para correrlo sin mencionar el directorio, la consola debe estar posicionada sobre la carpeta del proyecto.
