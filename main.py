import core
from core.output import *
from core.utilities import path, startup, database_init
from core.modules import login, signup, config
from core.manage import load_users, save_users

dir = path()
settings = startup(dir)
objects = load_users(dir)
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
            settings.errors+=1
            if settings.errors == settings.error_limit:
                div()
                print("\t\t\t\t    Opcion invalida")
                settings.outer_loop = menu_error()
                break
        elif option == 1:
            settings.tries = 0 ; settings.errors = 0
            results = login(settings, option, objects)
            if results == True:
                success()
                break
            elif results == False:
                break
        elif option == 2:
            settings.tries = 0 ; settings.errors = 0
            results = signup(settings, option, objects)
            if results == True:
                save_users(dir, objects)
            elif results == False:
                break
        elif option == 3:
            settings.tries = 0 ; settings.errors = 0
            results = config(dir, settings, option, objects)
            if results == False:
                break
        elif option == 4:
            save_users(dir, objects)
            option_title(option)
            settings.outer_loop = exit()
        else:
            settings.tries+=1
            if settings.tries == settings.try_limit:
                settings.outer_loop = menu_error()
        settings.inner_loop = False

# cd C:\Users\RTX\Desktop\python\50215\entregas\
# py main.py