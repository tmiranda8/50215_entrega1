import json
from core.output import *
from core.manage import save_users

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
    if choice == 'y':
        settings.errors = 0
        settings.tries = 0
        return True
    else:
        return False

def database(objects):
    for users in objects:
        if objects[users].surname != '':
            print(f"      |\t\t Usuario {objects[users]._ID__internal_ID}: {objects[users].user} \t | \t Nombre completo: {objects[users].name} {objects[users].surname}\t\t|")
        else:
            print(f"      |\t\t Usuario {objects[users]._ID__internal_ID}: {objects[users].user} \t | \t Nombre completo: {objects[users].name}\t\t|")

def reset_feature():
    div()
    print('\tPara habilitar los reinicios de constraseña, debe agregar un dato adicional.')
    choice = str(input('\t\tEsta opción no es obligatoria. Desea activarla? (y/n): '))
    if choice == 'y':
        div()
        return True

def reset_password(path, user_data, objects):
    try:
        user_check = user_data in objects
    except:
        ...
    else:
        if user_check:
            address = objects[user_data]
            if address.recovery != None:
                div()
                auth = str(input('\n\t\t\tIngrese su dato de recuperacion: '))
                div()
                if auth == address.recovery:
                    new_password = str(input('Ingrese su nueva contraseña: '))
                    address._Clients__pw = new_password
                    save_users(path, objects)
                    return True
                else:
                    div()
                    print("\t  Su dato de recuperacion es incorrecto. Vuelva a intentarlo mas tarde")
                    return False
            else:
                div()
                print("\t\t  El usuario no tiene esta funcionalidad activa.")
                div()
                return False
        else:
            div()
            print('\t\t\t\tEl usuario ingresado no existe')
            return False
        
def auth_factor():
    print('\t\t\tEl dato de recuperacion debe ser un valor alfanumerico')
    auth = str(input('\t\t\tIngrese su dato de recuperacion: '))
    div()
    return auth

def personal_info(credentials, recovery):
    choice = str(input("\t\t\tDesea completar su perfil? (y/n): "))
    if choice == 'y':
        print('Ingrese:\n')
        credentials.append(str(input("nombre: ") or ''))
        credentials.append(str(input("apellido: ") or ''))
        credentials.append(int(input("su edad: ") or ''))
        credentials.append(str(input("email: ") or ''))
        return (credentials[0], {"pw": credentials[1], "name":credentials[2], "surname":credentials[3], "age":credentials[4], "email":credentials[5], "recovery":recovery})
    else:
        return (credentials[0], {"pw": credentials[1], "name":"", "surname":"", "age":"", "email":"", "recovery": recovery})