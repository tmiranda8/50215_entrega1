import json

class Policy:
    def __init__(self, init = 0):
        self.errors = init
        self.tries = init
        self.error_limit = init
        self.try_limit = init
        self.inner_loop = init
        self.outer_loop = init
    def set_error_policy(self, path):
        try:
            limit = int(input('\n\t\tPor favor, defina la cantidad limite de errores permitidos: '))
        except:
            print('\t\t\tSe produjo un error con el caracter presionado')
        else:
            self.error_limit = limit
            with open(path + '/settings.json') as settings_file:
                copy = json.load(settings_file)
                copy['error_limit'] = self.error_limit
            with open(path + '/settings.json', 'w') as settings_file:
                json.dump(copy, settings_file)
            return True
    def set_try_policy(self, path):
        try:
            limit = int(input("\n    Por favor, defina la cantidad limite de intentos permitidos al iniciar sesion: "))
        except:
            print('\t\t\tSe produjo un error con el caracter presionado')
        else:
            self.try_limit = limit
            with open(path + '/settings.json') as settings_file:
                copy = json.load(settings_file)
                copy['try_limit'] = self.try_limit
            with open(path + '/settings.json', 'w') as settings_file:
                json.dump(copy, settings_file)
            return True


