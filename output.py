from utilities import clear
menu={1:"Iniciar sesion", 2:"Registrarse", 3:'Configuracion', 4:"\tSalir"}

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
