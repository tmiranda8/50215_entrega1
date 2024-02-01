from output import *
from utilities import path, startup, database_init
from modules import login,signup

dir = path()
settings = startup(dir)
db_check = database_init(dir)
settings.outer_loop = db_check

while settings.outer_loop ==  True:
    main_menu()
    try:
        option = int(input("\t\t\t\tSeleccione una opcion: "))
    except:
        option = 0
    finally:
        if option == 0:
            ...
        elif option == 1:
            results = login(dir, settings, option)
            if results == True:
                success()
                break
            elif results == 'try_limit':
                print(f"\t Ha superado el límite de intentos ({settings.tries}). Vuelva a intentarlo mas tarde")
                div()
                break
            elif results == 'error_limit':
                print(f"     Ha superado la cantidad de errores permitidos ({settings.errors}). Vuelva a intentarlo mas tarde")
                div()
                break
        elif option == 2:
            results = signup(dir, settings, option)
            if results == True:
                print(f"\t Ha superado el límite de intentos ({settings.tries}). Vuelva a intentarlo mas tarde")
                div()
                break
        elif option == 3:
            ...
        elif option == 4:
            option_title(option)
            settings.outer_loop=exit()
        settings.inner_loop = False

# cd C:\Users\RTX\Desktop\python\50215\entrega_1\
# py main.py