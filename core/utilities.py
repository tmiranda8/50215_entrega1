import os, json
import core.settings as setting_tools
import core.output

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def path():
    path = os.getcwd()
    path = path.replace('\\','/')
    return path

def database_init(path):
    if os.path.exists(path + '/database.json'):
        return True
    else:
        try:
            with open(path + '/database.json', 'x') as db:
                init={"clientes": {"admin": {"pw": "admin", "name":"administrador", "surname":"", "age":"", "email":"", "recovery": None},}}
                json.dump(init, db)
        except:
            print ('    Se produjo un error inesperado (database). Consulte con el administrador')
            return False
        else:
            return True

def startup(path):
    settings = setting_tools.Policy()
    if os.path.exists(path + '/settings.json'):
        try:
            with open(path + '/settings.json') as settings_file:
                copy = json.load(settings_file)
                settings.error_limit = copy['error_limit']
                settings.try_limit = copy['try_limit']
        except:
            print ('    Se produjo un error inesperado (settings). Consulte con el administrador')
    else:
        with open(path + '/settings.json', 'x') as settings_file:
            limits = {'error_limit':0,'try_limit':0}
            json.dump(limits, settings_file)
        settings.set_error_policy(path)
        core.output.div()
        settings.set_try_policy(path)
    return settings

