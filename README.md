# Invera To-Do List Challenge

Desafio realizado para Invera, consistente en construir una webapp de una ToDo list.

Tecnologia usada:
  - Python + Django
  - Rest Framework
  - Html + Css + Js
  - Docker

## Iniciando el proyecto
Primero tenemos que clonar el proyecto
```sh
$ git clone https://github.com/danilodiez/todo-challenge.git
```
Nos movemos a la carpeta de la app
```sh
$ cd todo-challenge
$ cd todoList
```

Lo ideal al trabajar con python es establecer un entorno virtual, para ello yo utilice pipenv:
```sh
$ pip install pipenv
$ pipenvshell
```
Instalamos los paquetes del proyecto
```sh
$ pip install -r requirements.txt
```

Ahora tenemos todo listo para ejecutar la aplicacion en el entorno
```sh
$ python manage.py runserver
```

## Otra opcion es utilizar el contenedor de Docker
Para ello debemos tener instalado Docker y docker-compose.
Simplemente ejecutamos
```sh
$ docker-compose build
```
Y una vez que la aplicacion se haya construido
```sh
$ docker-compose up
```

Y listo, con cualquiera de las opciones anteriores ahora tenemos corriendo la aplicacion en:
[http://localhost:8000/todo/](http://localhost:8000/todo/) - Para el fronEnd
[http://localhost:8000/api](http://localhost:8000/api/) - Para el backend y utilizar la API


# ToDo App

![](https://github.com/danilodiez/todo-challenge/blob/main/imagenesTemplate/principal.jpeg)
