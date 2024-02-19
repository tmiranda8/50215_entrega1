import json
from core.output import *

def credentials(mode = True):
    if mode:
        user=str(input("Ingrese nombre de usuario: "))
        pw = str(input("Ingrese password: "))
        return [user, pw]
    else:
        user=str(input("Ingrese nombre de usuario: "))
        return user

def go_back(settings):
    choice = str(input("\t\t\tDesea volver al menu principal? (y/n): "))
    print(choice)
    if choice == 'y':
        settings.errors = 0
        settings.tries = 0
        return True
    else:
        return False

def reset_feature():
    div()
    print('\tPara habilitar los reinicios de constraseña, debe agregar un dato adicional.')
    choice = str(input('\t\tEsta opción no es obligatoria. Desea activarla? (y/n): '))
    if choice == 'y':
        div()
        return True

def login(path, settings, option):
    with open(path + '/database.json') as database:
        db = json.load(database)
        settings.inner_loop = True
    while settings.inner_loop == True:
        option_title(option)
        user_data = credentials()
        find = user_data[0] in db['clientes']
        if find == True:
            if user_data[1] == db['clientes'][user_data[0]]['pw']:
                settings.inner_loop = False
                return True
            else:
                settings.tries+=1
                if settings.tries < (settings.try_limit - 1):
                    div()
                    print("\tHa ingresado una contraseña incorrecta, por favor vuelva a intentarlo")
                    div()
                    if go_back(settings):
                        settings.inner_loop = False
                elif settings.tries == (settings.try_limit - 1):
                    div()
                    print("\t\t\tEsta por alcanzar el limite de intentos.")
                    div()
                    if go_back(settings):
                        settings.inner_loop = False
                else:
                    div()
                    settings.inner_loop = False
                    return 'try_limit'
        else:
            settings.errors+=1
            if settings.errors < (settings.error_limit - 1):
                div()
                print("\t\tNo existe el usuario ingresado. Por favor vuelva a intentarlo")
                div()
                if go_back(settings):
                    settings.inner_loop = False
            elif settings.errors == (settings.error_limit - 1):
                div()
                print("\t\t\tEsta por alcanzar el limite de intentos.")
                div()
                if go_back(settings):
                    settings.inner_loop = False
            else:
                div()
                settings.inner_loop = False
                return 'error_limit'

def signup(path, settings, option):
    with open(path + '/database.json') as database:
        db = json.load(database)
        settings.inner_loop = True
    while settings.inner_loop == True:
        option_title(option)
        user_data = credentials()
        user_check = user_data[0] in db['clientes']
        if user_check == False:
            if reset_feature():
                print('\t\t\tEl dato de recuperacion debe ser un valor alfanumerico')
                auth = str(input('\t\t\tIngrese su dato de recuperacion: '))
                div()
                user_data.append(auth)
                with open(path + '/database.json', 'w') as database:
                    db['clientes'].update({user_data[0]:{'pw':user_data[1], 'recovery':user_data[2]}})
                    json.dump(db, database)
                    settings.inner_loop = False 
            else:
                div()
                with open(path + '/database.json', 'w') as database:
                    db['clientes'].update({user_data[0]:{'pw':user_data[1]}})
                    json.dump(db, database)
                    settings.inner_loop = False 
        else:
            settings.tries+=1
            if settings.tries < (settings.try_limit - 1):
                div()
                print('\t\tEl usuario ingresado ya existe. Elija otro nombre de usuario.\n')
                print('\t\t\tSi olvido su contraseña, puede restablecerla.\n')
                print('\t\tEn caso contrario, pongase en contacto con el administrador.')
                div()
                if go_back(settings):
                    settings.inner_loop = False                
            elif settings.tries == (settings.try_limit - 1):
                div()
                print('\t\tEl usuario ingresado ya existe. Elija otro nombre de usuario.\n')
                print("\t\t\t  Esta por alcanzar el limite de intentos.")
                div()
                if go_back(settings):
                    settings.inner_loop = False
            else:
                div()
                settings.inner_loop = False
                return True

def config(path, settings, option):
    option_title(option)
    choice = config_menu()
    if choice == 1:
        clear()
        div()
        user_data = credentials(False)
        return reset_password(path, settings, user_data)
    elif choice == 2:
        clear()
        div()
        if settings.set_error_policy(path):
            div()
            if settings.set_try_policy(path):
                return True
            else:
                return False
        else:
            return False
    elif choice == 3:
        clear()
        option_title(5)
        database(path, settings)
        div()
        if go_back(settings):
            return True
        else: 
            return False
    else:
        return True

def reset_password(path, settings, user_data):
    with open(path + '/database.json') as database:
        db = json.load(database)
        settings.inner_loop = True
    if settings.inner_loop == True:
        find = user_data in db['clientes']
        if find:
            auth = str(input('\n\t\t\tIngrese su dato de recuperacion: '))
            if auth == db['clientes'][user_data]['recovery']:
                new_password = str(input('Ingrese su nueva contraseña: '))
                with open(path + '/database.json', 'w') as database:
                    db['clientes'][user_data].update({'pw':new_password,'recovery':auth})
                    json.dump(db, database)
                return True
            else:
                div()
                print("\t  Su dato de recuperacion es incorrecto. Vuelva a intentarlo mas tarde")
                return False
        else:
            div()
            print('\t\t\t\tEl usuario ingresado no existe')
            return False


