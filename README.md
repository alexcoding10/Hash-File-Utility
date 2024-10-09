# Hash File Utility

## Funcionamiento del Programa

Este programa permite calcular y gestionar el hash MD5 de archivos, brindando diferentes opciones según las necesidades del usuario. A continuación, se detalla el funcionamiento del programa de acuerdo con el siguiente enunciado:

***Crea un programa al que se le pase una opción y un nombre de fichero. Si la opción es -1, debe mostrar el hash md5 del fichero, obtenido con el comando:
`certutil -hashfile "ruta_completa_del_archivo" MD5`. Si la opción es -c, debe guardar el hash md5 del fichero en un fichero con el mismo nombre, y añadir al final `.md5`. Para esta última opción, hay que redirigir la salida del proceso hacia un fichero. Si el fichero existe, se reescribirán sus contenidos. Si la opción es -t y existe un fichero como el que se genera con la opción -c, debe calcularse el valor del hash md5 y compararlo con los contenidos del fichero. Si coinciden, no debe decirse nada, pero si no coinciden (normalmente porque el contenido del fichero se cambió después de generar el fichero que contiene el hash md5), debe indicarse que el valor del hash no corresponde con los contenidos del fichero.***

### Requisitos

- Python 3.x
- Sistema operativo Windows (debido al uso del comando `certutil`).

### Estructura del Proyecto

- **config.py**: Contiene configuraciones del programa, incluyendo la ruta donde se generarán los archivos con la extensión `.md5`.
  
- **path_chooser.py**: Se encarga de mostrar y obtener del usuario la ruta del archivo que quiere hashear y las opciones. Se puede ejecutar el script directamente:
  ```bash
  python main.py [opcion] [ruta_archivo]
  ```

- **process.py**: Contiene todas las funciones necesarias para ejecutar los procesos correspondientes a cada opción.

### Opciones Disponibles

1. **Opción `-1`**:
   - Muestra el hash MD5 del archivo especificado en la ruta.
   - Utiliza el siguiente comando para calcular el hash:
     ```bash
     certutil -hashfile "ruta_completa_del_archivo" MD5
     ```

2. **Opción `-c`**:
   - Guarda el hash MD5 del archivo en un nuevo archivo que tendrá el mismo nombre y la extensión `.md5`.
   - Si el archivo ya existe, se sobrescribirá.

3. **Opción `-t`**:
   - Compara el hash MD5 del archivo original con el hash almacenado en el archivo `.md5`.
   - Si los hashes coinciden, no se mostrará ningún mensaje. Si no coinciden, se indicará que el valor del hash no corresponde con el contenido del archivo.

### Ejemplo de Uso

Para utilizar el programa, puedes ejecutar uno de los siguientes comandos:

- Para calcular y mostrar el hash MD5 de un archivo:
  ```bash
  python main.py -1 "C:\ruta\al\archivo.txt"
  ```

- Para guardar el hash MD5 en un archivo:
  ```bash
  python main.py -c "C:\ruta\al\archivo.txt"
  ```

- Para verificar el hash MD5 contra un archivo existente:
  ```bash
  python main.py -t "C:\ruta\al\archivo.txt"
  ```

### Notas Adicionales

- Asegúrate de que la ruta especificada sea correcta y que el archivo exista para evitar errores durante la ejecución.
- El programa manejará errores comunes, como la falta de archivos o problemas al crear archivos de salida.

## Contribuciones

Si deseas contribuir al proyecto, por favor crea un fork del repositorio y envía un pull request con tus mejoras o correcciones.

## Licencia

Este proyecto está bajo la licencia MIT. Para más detalles, consulta el archivo LICENSE.

---
