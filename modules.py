import json
from output import *

def login(path, settings):
    settings.inner_loop = True
    with open(path + '/database.json') as database:
        db = json.load(database)
    while settings.inner_loop == True:
        user_data = credentials()
        find = user_data[0] in db['clientes']
        if find == True:
            if user_data[1] == db['clientes'][user_data[0]]['pw']:
                settings.inner_loop = False
                return True
            else:
                settings.tries+=1
                if settings.tries < settings.try_limit:
                    div()
                    print("\tHa ingresado una contrasenia incorrecta, por favor vuelva a intentarlo")
                    div()
                    goback = input("\t\t\tDesea volver al menu principal? (y/n): ")
                    if goback == 'y':
                        settings.inner_loop = False
                    
                else:
                    clear()
                    div()
                    print(f"Ha superado el límite de intentos. Vuelva a intentarlo mas tarde")
                    settings.inner_loop = False
        else:
            settings.errors+=1
            if settings.errors < settings.error_limit:
                div()
                print("\t\tNo existe el usuario ingresado. Por favor vuelva a intentarlo")
                div()
                goback=input("\t\t\tDesea volver al menu principal? (y/n): ")
                if goback == 'y':
                    settings.inner_loop = False
                div()
            else:
                print(f"Ha superado el límite de intentos. Vuelva a intentarlo mas tarde")
                settings.inner_loop = False

def signup():
    ...

def reset_password():
    ...

def credentials():
    user=str(input("Ingrese nombre de usuario: "))
    pw = str(input("Ingrese password: "))
    return [user, pw]