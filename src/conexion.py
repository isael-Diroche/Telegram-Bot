# IMPORT MODULES

from bot import firebase, sqlite3

# YOUR CODE HERE

firebase = firebase.FirebaseApplication("https://pythonbdtest-50a94-default-rtdb.firebaseio.com/", None)

def conexion(database):
    try:
        mi_conexion = sqlite3.connect(database)
        print("Conected to database!")
        return mi_conexion

    except Exception as ex:
        print(ex)


def tareasid():
    sql = """SELECT idUnique FROM gestion_tareas"""
    nueva_conexion = conexion("database/data.sqlite3")

    cursor = nueva_conexion.cursor()
    cursor.execute(sql)

    rows = cursor.fetchall()

    nueva_conexion.commit()
    nueva_conexion.close()

    return rows


def insertar(id_user, languaje_code, is_bot, user_name, first_name, last_name, longitud=1):
    nueva_conexion = conexion("./database/data.sqlite3")
    cursor = nueva_conexion.cursor()

    if longitud == 1:
        for x in range(longitud):
            sql = f"""INSERT INTO usuarios (user_id, lenguaje, es_bot, username, nombre, apellido) 
            VALUES
            ({id_user}, '{languaje_code}', {is_bot}, '{user_name}', '{first_name}', '{last_name}')
            """
            print("insertado el usuario", user_name)
            cursor.executescript(sql)

    else:
        for x in range(longitud):
            sql = f"""
            INSERT INTO usuarios (user_id, lenguaje, es_bot, username, nombre, apellido) 
            VALUES
            ({id_user[x]}, '{languaje_code[x]}', {is_bot[x]}, '{user_name[x]}', '{first_name[x]}', '{last_name[x]}')
            """
            print("insertado el usuario", user_name[x])
            cursor.executescript(sql)

    nueva_conexion.commit()
    nueva_conexion.close()


def insertar_materia(longitud, id_materia, nombre, codigo, image):
    nueva_conexion = conexion("./database/data.sqlite3")
    cursor = nueva_conexion.cursor()
    for x in range(int(longitud)):
        sql = f"""
        INSERT INTO materias (id, nombre, codigo, image) 
        VALUES
        ({id_materia[x]}, '{nombre[x]}', '{codigo[x]}', '{image[x]}')
        """
        print("insertado la materia", nombre[x])

        cursor.executescript(sql)

    nueva_conexion.commit()
    nueva_conexion.close()


def actualizar_tarea(self, idMateria):
    sql = """SELECT id
    FROM gestion_tareas
    ORDER BY id DESC """

    nueva_conexion = self.conexion("database/data.sqlite3")

    cursor = nueva_conexion.cursor()
    cursor.execute(sql)

    rows = cursor.fetchone()

    # print(f"rows = {rows}")
    idprincipal = rows[0]

    # ------------------------------------------------------------------ #

    query = f"""UPDATE gestion_tareas
            SET idMateria = {idMateria}
            WHERE
            id = {idprincipal} """

    cursor.executescript(query)

    nueva_conexion.commit()
    nueva_conexion.close()


def insertar_tarea(id_tarea, titulo, id_materia, id_file, id_usuario, filelink, id_unique, longitud = 1):
    nueva_conexion = conexion("./database/data.sqlite3")
    cursor = nueva_conexion.cursor()

    if longitud == 1:
        for x in range(longitud):
            sql = """INSERT INTO gestion_tareas (id, titulo, fileid, idMateria, idUsuario, fileLink, idUnique) 
            VALUES 
            ({}, '{}', '{}', {}, {}, '{}', '{}')""".format(id_tarea, titulo, id_file, id_materia, id_usuario, filelink, id_unique)

            cursor.executescript(sql)

    else:
        for x in range(int(longitud)):
            sql = f"""
            INSERT INTO gestion_tareas (id, titulo, fileid, idMateria, idUsuario, fileLink, idUnique) 
            VALUES
            ({id_tarea[x]}, '{titulo[x]}', {id_materia[x]}, '{id_file[x]}', {id_usuario[x]},'{filelink[x]}', '{id_unique[x]}')"""

            print("insertado la tarea", titulo[x])

            cursor.executescript(sql)

    nueva_conexion.commit()
    nueva_conexion.close()


def get_file_link():
    sql = """SELECT id
        FROM gestion_tareas
        ORDER BY id DESC """

    nueva_conexion = conexion("database/data.sqlite3")

    cursor = nueva_conexion.cursor()
    cursor.execute(sql)

    rows = cursor.fetchone()

    idprincipal = rows[0]

    # ------------------------------------------------------------------ #

    query = f"""SELECT fileLink FROM gestion_tareas WHERE id = {idprincipal} """

    cursor.execute(query)

    file_links = cursor.fetchone()
    file_link = file_links[0]

    nueva_conexion.commit()
    nueva_conexion.close()

    return file_link


def registrar_usuario_firebase(datos) -> None:
    registro = {
        'user_id': datos.id,
        'es_bot': datos.is_bot,
        'lenguaje': datos.language_code,
        'nombre': datos.first_name,
        'apellido': datos.last_name,
        'username': datos.username
    }
    firebase.post('https://pythonbdtest-50a94-default-rtdb.firebaseio.com/usuarios', registro)

    insertar(id_user=registro['user_id'],
             languaje_code=registro['lenguaje'],
             is_bot=registro['es_bot'],
             user_name=registro['username'],
             first_name=registro['nombre'],
             last_name=registro['apellido'])

    print(f"Registrado nuevo usuario: {registro['nombre']}")


def registrar_tarea_firebase(datos) -> None:
    registro = datos
    firebase.post('https://pythonbdtest-50a94-default-rtdb.firebaseio.com/gestion_tareas', registro)

    insertar_tarea(id_tarea=registro['id'],
                   titulo=registro['titulo'],
                   id_materia=registro['idMateria'],
                   id_file=registro['fileid'],
                   id_usuario=registro['idUsuario'],
                   filelink=registro['fileLink'],
                   id_unique=registro['idUnique'],)

    print(f"Registrada nueva tarea: {registro['titulo']}")

# firebase.get('https://pythonbdtest-50a94-default-rtdb.firebaseio.com/usuarios', '')
# firebase.post('https://pythonbdtest-50a94-default-rtdb.firebaseio.com/usuarios', datos)
# firebase.delete('https://pythonbdtest-50a94-default-rtdb.firebaseio.com/usuarios', '')
