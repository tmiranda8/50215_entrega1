import json
from core.output import *
from core.helpers import *
from core.manage import *

def login(settings, option, objects):
    settings.inner_loop = True
    while settings.inner_loop == True:
        option_title(option)
        user_data = credentials()
        try:
            user_check = user_data[0] in objects
        except:
            return False
        else:
            if user_check:
                address = objects[user_data[0]]
                if user_data[1] == address._Clients__pw:
                    settings.inner_loop = False
                    return True
                else:
                    settings.tries+=1
                    if settings.tries < (settings.try_limit - 1):
                        login_error(0)
                        if go_back(settings):
                            settings.inner_loop = False
                    elif settings.tries == (settings.try_limit - 1):
                        login_error(2)
                        if go_back(settings):
                            settings.inner_loop = False
                    else:
                        login_error('try_limit')
                        settings.inner_loop = False
                        return False
            else:
                settings.errors+=1
                if settings.errors < (settings.error_limit - 1):
                    login_error(1)
                    if go_back(settings):
                        settings.inner_loop = False
                elif settings.errors == (settings.error_limit - 1):
                    login_error(2)
                    if go_back(settings):
                        settings.inner_loop = False
                else:
                    login_error('error_limit')
                    settings.inner_loop = False
                    return False

def signup(settings, option, objects):
    settings.inner_loop = True
    while settings.inner_loop == True:
        option_title(option)
        user_data = credentials()
        try:
            user_check = user_data[0] in objects
        except:
            return False
        else:
            if user_check == False:
                    if reset_feature():
                        recovery = auth_factor()
                        data = personal_info(user_data, recovery)
                    else:
                        div()
                        data = personal_info(user_data, recovery = None)
                    add_user(data, objects)
                    settings.inner_loop = False
                    return True
            else:
                settings.tries+=1
                if settings.tries < (settings.try_limit - 1):
                    signup_error(0)
                    if go_back(settings):
                        settings.inner_loop = False                
                elif settings.tries == (settings.try_limit - 1):
                    signup_error(1)
                    if go_back(settings):
                        settings.inner_loop = False
                else:
                    signup_error(2)
                    settings.inner_loop = False
                    return False

def config(path, settings, option, objects):
    settings.inner_loop = True
    while settings.inner_loop == True:
        option_title(option)
        choice = config_menu()
        if choice == 1:
            clear()
            div()
            user_data = credentials(False)
            div()
            return reset_password(path, user_data, objects)
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
            database(objects)
            div()
            if go_back(settings):
                return True
            else: 
                div()
                return False
        elif choice == 4:
            return True
        else:
            settings.errors+=1
            if settings.errors == settings.error_limit:
                config_error('error_limit')
                settings.inner_loop = False
                return False
