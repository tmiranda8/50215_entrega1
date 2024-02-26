# Entregas
Este repositorio corresponde a la primer y segunda actividad del curso "Python" dictado en **Coderhouse** Digital School.

## Primera pre-entrega del proyecto final
### Objetivo
Hacer uso de funciones. Diseñar la estructura de un programa dedicado al registro de usuarios.

### Consigna
Crear un programa que permita el registro y almacenamiento de usuarios en una base de datos, siguiendo los siguientes requisitos:
 - Una función para almacenamiento de datos
 - Almacenar las credenciales utilizando diccionarios, bajo el formato **key:value**
 - Una función para consulta de datos
 - Una función para realizar inicios de sesión

## Segunda pre-entrega del proyecto final
### Objetivo
Poner en  práctica los conceptos de POO.
### Consigna
Crear un programa que permita el modelamiento de Clientes en una página de compras.
- Se evaluará el correcto uso de atributos y métodos
   - La clase debe tener, como mínimo, 4 atributos y 2 métodos
   - El uso de herencias es opcional
   - Utilizar Dunder Methods como por ejemplo `__str__()`
- Crear un paquete redistribuible que contenga el programa
   - Agregar al paquete el archivo de la primer pre-entrega
## Implementación
El diseño de lo solicitado se llevó a cabo en un programa modular y utilizando objetos. 

Se añadieron las siguientes funcionalidades:
 - Interfaz gráfica rudimentaria
 - Reinicio de contraseña, mediante un (1) factor de seguridad que le permita al usuario habilitar dicha funcionalidad
 - Políticas de manejo en la cantidad de intentos y/o errores cometidos, configurable por el usuario.
    - Se define por única vez en el primer arranque
    - Los valores elegidos se almacenan en un archivo
    - Luego se cargan cada vez que se ejecute el programa
 - Menú de configuraciones, que permite:
    - Reiniciar la contraseña de determinado usuario
    - Configurar el límite de intentos y errores permitidos

### Estructura del programa
El script principal del sistema es `main.py`, encargado de orquestar el arranque y funcionamiento del menu. El resto de código se divide como sigue:
| Funcionalidades             | Script                |
| ----------------- | ------------------ |
|Opciones del menu y funcionalidades asociadas|`modules.py`|
|Funciones de impresión de pantalla|`output.py`| 
|Objeto que administra el manejo del sistema |`settings.py`|
|Inicialización del sistema, variables y bases de datos|`utilities.py`|
||``|
||``|







