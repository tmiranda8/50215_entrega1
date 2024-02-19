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
        option = int(input("\t\t\t\tSeleccione una opcion: "))
        return option

def database(path, settings):
    with open(path + '/database.json') as database:
        db = json.load(database)
        settings.inner_loop = True
    if settings.inner_loop == True:
        i=0
        for clients in db['clientes']:
            i+=1
            print(f"      |\t\t Usuario {i}: {clients} \t | \t Contraseña: {db['clientes'][clients]['pw']}\t\t|")

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
