# TeleHelpBot 🤖 
 _Iniciado el 12 de Octubre del 2021 por **Isael Diroche**_
---

## ➜ Bot de telegram
Un bot de Telegram es un programa automatizado que puede interactuar con los usuarios a través de la plataforma de mensajería de Telegram. Los bots de Telegram pueden realizar una variedad de tareas, desde proporcionar información útil hasta realizar acciones específicas porsupuesto que este no es la excepcion.

Algunos ejemplos comunes de lo que puede hacer este bot de Telegram son:

1. **Proporcionar información:** los bots pueden responder a preguntas comunes y proporcionar información útil sobre una amplia variedad de temas.

2. **Realizar tareas automatizadas:** los bots pueden realizar tareas automatizadas, como enviar mensajes, programar citas o hacer reservas en línea.

3. **Ofrecer entretenimiento:** los bots pueden proporcionar juegos, chistes y otros tipos de entretenimiento a los usuarios.

4. **Interactuar con otros servicios:** los bots pueden interactuar con otros servicios en línea, como Google Maps, Twitter o YouTube, para proporcionar información adicional o realizar acciones específicas.

5. **Realizar tareas personalizadas:** los bots pueden ser programados para realizar tareas personalizadas específicas para un usuario o grupo de usuarios en particular.

En resumen, los bots de Telegram son programas automatizados que pueden realizar una variedad de tareas para interactuar con los usuarios y proporcionar información útil o servicios.


Trato de acortar lo mas posible da descipcion del bot y sus funcionalidades en el README por lo que estare haciendo una descripcion mas detallada en un archivo ageno al repositorio.

[**Entra y prueba a Firulais**](https://t.me/isael_ayuda_bot)


## ➜ Instalación

ya deberias de tener Python en tu ordenador y ya actualizado para poder llevar a cabo todo sin problemas. Esto para poder preparar el entorno para controbuir en el 

 1. `pip install -r requirements.txt`
 
 con esto ya tendras todas las librerias y paquetes necesarios para ejecutar el bot en tu ordenador

## Estructura del Proyecto


``` php
├── src/
│   ├── bot/
│   │   ├── buttons/
│   │   │   └── main.py
│   │   ├── commands/
|   |   |   ├── ext/
|   |   |   |   └── conversation.py
|   |   |   └── main.py
│   │   └── filters/
|   |   |   ├── ext/
|   |   |   |   ├── hashtag.py
|   |   |   |   ├── mention.py
|   |   |   |   └── messages.py
|   |   |   ├── main.py
|   |   |   └── questions.py
│   ├── static/
│   │   ├── documents/
│   │   |   └── .keep
│   │   ├── images/
│   │   |   └── .keep
│   │   └── notes/
│   │   |   ├── .keep
│   │   |   └── nota.mp3
│   ├── conexion.py
│   ├── data.sqbpro
│   └── data.sqlite3
├── .gitignore
├── bot.py
├── migrations.py
├── Profile
├── README.md
├── requirements.txt
└── runtime.txt
```

No se te hara dificil encontrar cada uno de los archivos los cuales editaras para introducir nuevas funcionalidades al bot. dentro de src/bot podras encontrar las carpetas que dividen el proyecto en botones, comandos y filtros. mas adelante explico la funcion de cada uno de estos.

que gueva escribir documentacion ya la seguire despues

