# Bot-Firulais 🐶 2.0
> _**Isael Diroche** (Programmer)October 12, 2021_

![Bot Firulais Picture](https://cdn1.telegram-cdn.org/file/OmhIzT8kRO8Om1bh25DGScEbTFnLXHmzJgytb_ush1eXHyq6OcyPB_JOU6139hea4Idlm0b4vlxcTAa59Hj35CmsfNU7R7PdhlErJj0djafjE6dORKV2IOXWyKwS1rRA75B1TQpaopWhju6FcV48kCM9Cg_CBVZDV_9yyYrV14wD_LSefDhXndnkRo0-mZNKouClcfad5EL1F5u5mppYYkjhvb-Eritu3nu21qQC4-zAplTaZ0SWbn48ygK9IGIe037y0n7PD1WBNs1W4FpzJRh5z-qSGtPuyjlPOk3Bppd_FKZ8QmWuA-xzm1KiPSFqmCT2tdn5_am1f2XXu6O0Uw.jpg)
---
Hola, mi nombre es **isael** y este es un **Proyecto** personal hecho para gestionar el grupo de Software (ITLA). Cuando este listo serás libre de poder **contribuir en el codigo**.

Este documento expresa las actualizaciones realizadas en el Bot para la facilitación de algún contenido o acción, no esta sujeta a derechos de autor por lo que no habrá ninguna restricción legal. En este texto se encontrara redactada cada una de las actualizaciones con el nuevo contenido y la manera correcta de como debe de ser utilizado. Es algo nuevo pero no tanto por lo que empezare desde la versión 1.0

[**Entra y prueba a Firulais**](https://t.me/isael_ayuda_bot)


## ➜ Instalación

 Después de tener el intérprete de python y un IDE para programar es instalar las librerías de telegram: 
 1. `pip install telegram` 
 2. `pip install python-telegram-bot`.

## ➜ Indicaciones

- Posteriormente en el archivo bot.py que es donde se encuentran los comandos en este insertas comandos nuevos para el bot.

- El directorio conexion/ es donde se encuentra conexion.py dónde creamos tablas, recibimos e insertamos registros en una base de datos sqlite.

- Filtros para cuando se valla a crear un nuevo filtro con un hastag # o menciones que es cuando te o mencionan a alguien en el grupo @username.

- Botones/ que es para los posibles botones de menús que se creen en el código del bot se llamarán a este archivo que los alojará todos.

- Después de tener el intérprete de python y un IDE para programar es instalar las librerías de telegram: `pip install telegram` y `pip install python-telegram-bot.`

- Por último esta el directorio de comandos/ donde esta una clase con comandos que serán llamados desde la lista de comandos del archivo `bot.py`



## ➜ Documentacion

Prácticamente la versión antigua a esta lo que hacia era lo siguiente:
• Ejecutar el comando /start para que el Bot de una respuesta de inicio.

• Responder a un saludo y a una despedida, específicamente a; hola y adios.

• Responder a "Broma" y a "Traduce"

• Ejecutar un comando /news para recibir ayuda en cuanto a las tareas y clases que tengas en determinado día y determinadas horas.

• Enviar un mensaje de bienvenida a nuevos miembros del grupo y un mensaje al salir algún miembro.

> Nueva actualización! 12/oct/2021  

## v1.0 - Nuevos Comandos y expansión de usuarios

Entre las nuevas funcionalidades se encuentran las siguientes:
• En primer lugar se expandió el comando /news para que Anthony lo pueda llevar a cabo.

• Un nuevo comando /traduce el cual es mas bien una translación de el traduce de los comandos de mensajes hacia un comando propio, funciona para traducir texto de ingles a español y viceversa. La forma de usarlo es la siguiente: 

`/traduce + palabra o oración.`
`#De haber un error el mensaje por parte del bot sera el siguiente:` 
`'No puedo traducir {msg}, lo siento 😢'`

> Nueva actualización! 14/oct/2021  

## v1.1 - Nuevos Comandos

Entre las nuevas funcionalidades se encuentran las siguientes:
• Prácticamente un nuevo y muy útil comando el cual es /voice, su funcionalidad es la de convertir textos a sonido con la mecánica de text-to-speech lo que considero como un objetivo muy bueno. La forma de usarlo es la siguiente: 

`/voice + palabra o oración.`
`#enseguida el bot convertira el texto en una nota de voz y la enviara`
`de haber algun error el mensaje sera 'Ocurrio un error al enviar el audio'`

• Lo siguiente es la translación de el comando de mensaje busca hacia un comando propio para así facilitar su uso y evitar confusión o algún problema.

• Ademas se implemento el uso del nuevo menú, verdad que es emocionante? 

# Esperen por una próxima actualización :D 
para una próxima actualización se me ocurre algo como convertir notas de voz en texto o talvez alguna otra funcionalidad :)