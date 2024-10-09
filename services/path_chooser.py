import sys #libreria para saber los argumentos
import os
import config
#opciones con las que contamos
OPCIONES = config.OPCIONES
DECRIPTION= config.DECRIPTION

def get_opcion_from_args():
    """Obtiene la primera opción válida de los argumentos de línea de comandos.

    Devuelve:
        str: La opción encontrada, o None si no se encuentra ninguna.
    """
    opciones = [option for option in OPCIONES if option in sys.argv]
    if len(opciones) > 1:
        print("Error: Se han proporcionado múltiples opciones. Solo se permite una opción.")
        return None
    return opciones[0] if opciones else None

def get_ruta_from_args():
    """Obtiene la ruta del archivo si se ha proporcionado.

    Devuelve:
        str: La ruta del archivo, o None si no se ha proporcionado.
    """
    if len(sys.argv) > 2:
        if validate_route(sys.argv[2]):
            return sys.argv[2]
    return None

def handler_get_option_and_route():
    
    option = get_opcion_from_args()
    ruta = get_ruta_from_args()
    """Verificar si cada existe"""
    if option != None and ruta != None:
        print(f"Tu opcion es -> {option}\n Tu ruta es -> {ruta}")
        return option,ruta
    else:
        '''Busca las opciones y la ruta desde un menu en pantalla'''
        option = get_option_from_menu()
        ruta = get_route_from_menu()
        return option,ruta         

def validate_route(route:str):
    return os.path.exists(route)

def get_route_from_menu():
    route = input('Escribe la ruta del Fichero para hash: ')
    if validate_route(route):
        print(f"Se ha selecionado la ruta {route}")
        return route
    else:
        print("La ruta no es valida o no existe, porfavor")
        get_route_from_menu()

def print_options():
    print("Seleciona una de esta opciones:")
    for opcion, descripcion in zip(OPCIONES, DECRIPTION):
        print(f'➡️  {opcion} \t {descripcion}')
    
def get_option_from_menu():
    print_options()
    option = input("Escribe una opcion: ")
    if validate_option(option):
        print("Se ha seleccionado la opcion ➡️ ",option)
        return option
    else:
        print("Selecion incorrecta, porfavor")
        get_option_from_menu()

def validate_option(option:str):
    return option in OPCIONES

