from output import *
from utilities import path, startup, database_init
from modules import login

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
            option_title(option)
            if login(dir,settings):
                success()
                break
        elif option == 2:
            ...
        elif option == 3:
            ...
        elif option == 4:
            option_title(option)
            settings.outer_loop=exit()