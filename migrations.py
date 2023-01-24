from bot import *

def migrate() -> None:
    # conexion = Conexion()

    try:  # PRIMERO traer todos los usuarios desde la nuve

        result = firebase.get('https://pythonbdtest-50a94-default-rtdb.firebaseio.com/usuarios', '')

        nombre = []
        apellido = []
        lenguaje = []
        es_bot = []
        username = []
        user_id = []

        for key in result:
            nombre.append(result[key]['nombre'])
            apellido.append(result[key]['apellido'])
            lenguaje.append(result[key]['lenguaje'])
            es_bot.append(result[key]['es_bot'])
            username.append(result[key]['username'])
            user_id.append(result[key]['user_id'])

        insertar(longitud=len(nombre),
                 id_user=user_id,
                 languaje_code=lenguaje,
                 is_bot=es_bot,
                 user_name=username,
                 first_name=nombre,
                 last_name=apellido)

        print("Success!")
    except Exception as ex:
        print("No se pudieron migrar los datos de los usuarios debido al siguiente error ", ex)

    try:  # Segundo traer todas las materias desde la nube
        result_materias = firebase.get('https://pythonbdtest-50a94-default-rtdb.firebaseio.com/materias', '')

        materia_id = []
        materia_nombre = []
        codigo = []
        image = []

        for key in result_materias:
            materia_id.append(result_materias[key]['id'])
            materia_nombre.append(result_materias[key]['nombre'])
            codigo.append(result_materias[key]['codigo'])
            image.append(result_materias[key]['image'])

        insertar_materia(longitud=len(materia_nombre),
                         id_materia=materia_id,
                         nombre=materia_nombre,
                         codigo=codigo,
                         image=image)

        print("Success!")
    except Exception as ex:
        print("no se pudieron migrar los registros de las materias", ex)

    try:  # TERCERO traer todas las tareas desde la nuve

        result_tareas = firebase.get('https://pythonbdtest-50a94-default-rtdb.firebaseio.com/gestion_tareas', '')

        id_tarea = []
        titulo = []
        id_materia = []
        id_file = []
        id_usuario = []
        file_link = []
        id_unique = []

        for key in result_tareas:
            id_tarea.append(result_tareas[key]['id'])
            titulo.append(result_tareas[key]['titulo'])
            id_file.append(result_tareas[key]['fileid'])
            id_materia.append(result_tareas[key]['idMateria'])
            id_usuario.append(result_tareas[key]['idUsuario'])
            file_link.append(result_tareas[key]['fileLink'])
            id_unique.append(result_tareas[key]['idUnique'])

        insertar_tarea(longitud=len(titulo),
                       id_tarea=id_tarea,
                       titulo=titulo,
                       id_materia=id_materia,
                       id_file=id_file,
                       id_usuario=id_usuario,
                       filelink=file_link,
                       id_unique=id_unique)

        print("Success!")
    except Exception as ex:
        print("No se pudo realizar el registro de las tareas debido al siguiente error: ", ex)

    # Finalmente imprimir
    print("Los datos han sido migrados")
