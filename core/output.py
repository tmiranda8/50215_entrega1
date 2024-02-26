from core.utilities import clear
import json

menu={1:"Iniciar sesion", 2:"Registrarse", 3:'Opciones', 4:"\tSalir", 5:"Base de datos"}

def div():
    print('------------------------------------------------------------------------------------------')

def main_menu():
    clear()
    div()
    print("""        
                                    Bienvenido al Sistema
                                -----------------------------
                                
        Para continuar, inicie sesion. Si ud. no posee un usuario, puede crear uno.
        
        
    
                                    1. Iniciar sesion
    
    
                                     2. Registrarse
    
    
                                     3. Configuracion
                                        
                                        
                                        4. Salir
    """)
    div()

def config_menu():
        print("""        
                                Menu de Configuracion
                            -----------------------------
                            
                        Para continuar, seleccione una opcion.




                                1. Reiniciar contraseña


                        2. Modificar limite de intentos y errores


                            3. Visualizar toda la base de datos


                              4. Volver al menu principal

    """)
        div()
        try:
            choice = int(input("\t\t\t\tSeleccione una opcion: "))
        except:
            pass
        else:
            return choice

def option_title(option):
    clear()
    div()
    print(f"\t\t\t   Opcion:\t\t {menu[option]}")
    div()

def exit():
    div()
    print('\t\t\t   Muchas gracias por usar el sistema')
    div()
    return False

def success():
    div()
    print("\t\t\t     Ha iniciado sesión correctamente!")
    div()

def menu_error():
    div()
    print("\t    Ha superado el límite de intentos. Vuelva a intentarlo mas tarde")
    div()
    return False

def signup_error(mode):
    if mode == 0:
        div()
        print('\t\tEl usuario ingresado ya existe. Elija otro nombre de usuario.\n')
        print('\t\t\tSi olvido su contraseña, puede restablecerla.\n')
        print('\t\tEn caso contrario, pongase en contacto con el administrador.')
        div()
    elif mode == 1:
        div()
        print('\t\tEl usuario ingresado ya existe. Elija otro nombre de usuario.\n')
        print("\t\t\t  Esta por alcanzar el limite de intentos.")
        div()
    elif mode == 2:
        div()
        print("\t    Ha superado el límite de intentos. Vuelva a intentarlo mas tarde")
        div()

def login_error(mode):
    if mode == 0:
        div()
        print("\tHa ingresado una contraseña incorrecta, por favor vuelva a intentarlo")
        div()
    elif mode == 1:
        div()
        print("\t\tNo existe el usuario ingresado. Por favor vuelva a intentarlo")
        div()
    elif mode == 2:
        div()
        print("\t\t\tEsta por alcanzar el limite de intentos.")
        div()
    elif mode == 'try_limit':
        div()
        print("\t    Ha superado el límite de intentos. Vuelva a intentarlo mas tarde")
        div()
    elif mode == 'error_limit':
        div()
        print("     Ha superado la cantidad de errores permitidos. Vuelva a intentarlo mas tarde")
        div()

def config_error(mode):
    if mode == 'error_limit':
        div()
        print("     Ha superado la cantidad de errores permitidos. Vuelva a intentarlo mas tarde")
        div()