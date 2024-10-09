import os
import subprocess
import config as config
from services.path_chooser import handler_get_option_and_route

def execute_process():
    '''Se llaman a los procesos y se crea la ruta donde se copiarán los archivos con los hash.'''
    # Crear la ruta si no existe
    try:
        os.makedirs(config.PATH_INITIAL_FOR_COPY, exist_ok=True)
        print(f"Directorio creado para copias: {config.PATH_INITIAL_FOR_COPY}")
    except Exception as e:
        print(f"Error al crear el directorio de copias: {e}")
        return
    
    '''Muestra por pantalla el menu y se encarga de obtener las opciones y rutas validas'''
    option, route = handler_get_option_and_route()
    
    if option == config.OPCIONES[0]:
        process_1(route)
    elif option == config.OPCIONES[1]:
        process_c(route)
    elif option == config.OPCIONES[3]:
        process_t(route)    

def process_1(archivo):
    '''Se obtiene el hash y se muestra por consola.'''
    hash_value = get_hash(archivo)
    print(f"✅ Se ha creado el Hash ➡️  {hash_value} para la ruta {archivo}.")

def process_c(archivo: str):
    '''Guarda el hash del archivo en un nuevo archivo con la extensión .md5.'''
    initial_path = config.PATH_INITIAL_FOR_COPY
    hash_value = get_hash(archivo)
    
    file_name, index_point = get_file_name(archivo)
    
    new_file = os.path.join(initial_path, file_name[:index_point] + config.EXTENSION)
    
    try:
        with open(new_file, "w") as nuevo_archivo:
            nuevo_archivo.write(hash_value)
        print(f"✅ Se ha creado el fichero {new_file} escribiendo el hash ➡️  {hash_value}")
    except Exception as e:
        print(f"❌ Error al crear el archivo: {e}")

def process_t(archivo: str):
    '''Compara el hash del archivo original con el hash almacenado en .md5.'''
    file_name, index_point = get_file_name(archivo)
    new_file_name = file_name[:index_point] + config.EXTENSION
    route_new_file = os.path.join(config.PATH_INITIAL_FOR_COPY, new_file_name)
    
    if file_exists(config.PATH_INITIAL_FOR_COPY, new_file_name):
        new_file_hash = get_hash(archivo)
        
        with open(route_new_file, "r") as archivo_hash:
            old_hash = archivo_hash.readline().strip()
        
        if new_file_hash != old_hash:
            print(f"❌ El valor del nuevo hash ➡️  {new_file_hash}\nno es igual al valor del antiguo ➡️   {old_hash}.\nEn el fichero ➡️   {route_new_file}.")
        else:
            print(f"✅ El hash nuevo y antiguo son los mismos ➡️  {new_file_hash}.")
    else:
        print(f"❌ No se ha creado una copia con el hash de {archivo}.")

def get_hash(archivo, algoritmo="MD5"):
    cmd = f'certutil -hashfile "{archivo}" {algoritmo}'
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
        # Extraer el hash de la salida
        lineas = result.stdout.split('\n')
        return lineas[1].strip()
    except subprocess.CalledProcessError as e:
        print(f"❌ Error al calcular el hash: {e}")

def get_file_name(route: str):
    '''Devuelve el nombre del archivo y su índice de punto.'''
    routes = route.split('\\')
    index = routes[-1].find(".")
    if index != -1:
        return routes[-1], index
    raise ValueError("No se ha pasado un archivo válido.")

def file_exists(folder_path: str, filename: str) -> bool:
    '''Verifica si un archivo existe en la carpeta dada.'''
    return filename in os.listdir(folder_path)
