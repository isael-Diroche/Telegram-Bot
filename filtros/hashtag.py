# IMPORT MODULES
import filtros.ext.filtro
import comandos

# YOUR CODE HERE

def filtro_hashtag(update, context):
    chat = update.effective_chat
    user = update.effective_user
    message = update.effective_message

    # menu = Menu(update, context)
    funcion = filtros.ext.filtro.Funciones(update, context, chat, user, message)


    get_members = context.bot.get_chat_member(chat_id=chat.id, user_id=user.id)
    puesto = str(get_members.status)

    mensaje = str(message.text).lower()
    text = mensaje.split()

    reply_user_id, reply_message, reply_user_name, reply_message_id = range(4)

    try:
        reply_user_id = message.reply_to_message.from_user.id
        reply_user_name = message.reply_to_message.from_user.first_name
        reply_message = message.reply_to_message.text
        reply_message_id = message.reply_to_message.message_id

    except:
        pass

    def borrar_mensaje():  # Eliminar el mensaje recien enviado por el usuario
        try:
            context.bot.delete_message(chat_id=chat.id, message_id=message.message_id)
        except:
            context.bot.delete_message(chat_id=chat.id, message_id=reply_message_id)

    def mensaje_defecto():  # Funcion para respuesta_rapida este mensaje por defecto en los Hastags
        context.bot.sendMessage(chat_id=chat.id, text=f"aun no puedo hacer nada con este comando, lo siento {user.first_name}")

    def respuesta_rapida(text):  # Funcion para respuesta_rapida mas facilmente simplificando el codigo
        context.bot.sendMessage(chat_id=chat.id, text=text)

    for x in text:

        if x == "#dice":
            respuesta_rapida(text=f"{user.first_name} esta provando su suerte.")
            context.bot.sendDice(chat_id=chat.id)

        elif x == '#promote':
            if puesto == "creator":
                try:
                    context.bot.promote_chat_member(chat_id=chat.id,
                                                    user_id=reply_user_id,
                                                    can_pin_messages=True,
                                                    can_delete_messages=True,
                                                    can_invite_users=True,
                                                    can_promote_members=True,
                                                    can_restrict_members=True,
                                                    can_change_info=True)
                    context.bot.sendMessage(chat_id=chat.id,
                                            text=f"Ahora {reply_user_name} es administrador@, puedes ver tus nuevos privilegios como admin del grupo")

                except:
                    context.bot.sendMessage(chat_id=chat.id, text=f"ocurrio un problema al intentar promover a {reply_user_name} ")

                borrar_mensaje()

            else:
                context.bot.sendMessage(text=f"no tienes permiso para promover, solo el creador del grupo puede usar este comando")

        elif x == '#unpromote':
            mensaje_defecto()
            borrar_mensaje()

        elif x == '#mute':
            tiempo = filtros.ext.filtro.datetime.utcnow() + filtros.ext.filtro.timedelta(minutes=5)

            current = eval(str(context.bot.getChat(chat_id=chat.id).permissions))
            new = {'can_send_messages': False, 'can_send_media_messages': False, 'can_send_polls': False,
                   'can_send_other_messages': False, 'can_add_web_page_previews': False, }

            permissions = {'can_send_messages': None, 'can_send_media_messages': None, 'can_send_polls': None,
                           'can_send_other_messages': None, 'can_add_web_page_previews': None, 'can_change_info': None,
                           'can_invite_users': None, 'can_pin_messages': None}

            permissions.update(current)
            permissions.update(new)

            new_permissions = filtros.ext.filtro.ChatPermissions(**permissions)
            context.bot.restrict_chat_member(chat_id=chat.id, user_id=reply_user_id, permissions=new_permissions, until_date=tiempo)
            context.bot.sendMessage(chat_id=chat.id, text=f"{reply_user_name} ha sido silenciado por 5 minutos")
            borrar_mensaje()

        elif x == '#unmute':
            current = eval(str(context.bot.getChat(chat_id=chat.id).permissions))
            new = {'can_send_messages': True, 'can_send_media_messages': True, 'can_send_polls': True,
                   'can_send_other_messages': True, 'can_add_web_page_previews': True}

            permissions = {'can_send_messages': None, 'can_send_media_messages': None, 'can_send_polls': None,
                           'can_send_other_messages': None, 'can_add_web_page_previews': None, 'can_change_info': None,
                           'can_invite_users': None, 'can_pin_messages': None}

            permissions.update(current)
            permissions.update(new)

            new_permissions = filtros.ext.filtro.ChatPermissions(**permissions)
            context.bot.restrict_chat_member(chat_id=chat.id, user_id=reply_user_id, permissions=new_permissions)
            context.bot.sendMessage(chat_id=chat.id, text=f"Ya puedes hablar {reply_user_name}, {user.first_name} te ha dado el permiso")
            borrar_mensaje()

        elif x == '#ban':
            try:
                context.bot.kick_chat_member(chat_id=chat.id, user_id=reply_user_id)

            except:
                context.bot.sendMessage(chat_id=chat.id, text='A ese no puedo :v')
            borrar_mensaje()

        elif x == '#chiste':
            funcion.recibir_chiste()

        elif x == '#broma':
            funcion.recibir_broma()

        elif x == '#pin':
            context.bot.pin_chat_message(chat_id=chat.id,
                                         message_id=reply_message_id,
                                         disable_notification=False)
            borrar_mensaje()

        elif x == '#meet':
            mensaje_defecto()
            borrar_mensaje()

        elif x == '#guardar':
            context.bot.copy_message(chat_id=-1001601095301,
                                     from_chat_id=chat.id,
                                     message_id=reply_message_id,
                                     caption=f"#{reply_user_name} #guardado")
            borrar_mensaje()

        elif x == '#voice':
            funcion.comando_voice(message)
            borrar_mensaje()

        elif x == '#traduce':
            comandos.ext.comandos.comando_translate(update, context)


        elif x == '#menu':
            menu.menu_isael()
            borrar_mensaje()

        elif x == '#pensum':
            funcion.recibir_imagen("pensum")
            borrar_mensaje()

        elif x == '#horario':
            funcion.recibir_imagen("horario")
            borrar_mensaje()

        elif x == '#recuerda':
            # recordar(mensaje, update, context)
            borrar_mensaje()

        elif x == '#frase':
            mensaje_defecto()
            borrar_mensaje()

        elif x == '@everyone' or x == '#everyone':
            mensaje_defecto()
            borrar_mensaje()

        elif x == '#list':
            mensaje_defecto()
            borrar_mensaje()

        elif x == '#list-new':
            mensaje_defecto()
            borrar_mensaje()

        elif x == '#list-delete':
            mensaje_defecto()
            borrar_mensaje()

        elif x == '#list-delete-all':
            mensaje_defecto()
            borrar_mensaje()

        elif x == "#archivo":
            nombre = mensaje.replace("#archivo", "")
            convertir_archivo(update, context, nombre, reply_message)
            borrar_mensaje()

        else:
            pass