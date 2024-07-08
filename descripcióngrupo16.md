# VIRTUAL WALLET
## Descripción del Proyecto
El proyecto VIRTUAL WALLET (Billetera Virtual) en Python es una aplicación que permite a los usuarios gestionar sus movimientos de dinero en una cuenta personal. Ofrece las siguientes funcionalidades: registrar y modificar el perfil, ingresar dinero, realizar transferencias, ver saldo y agendar las facturas de servicios e impuestos. Proporciona persistencia de datos mediante el uso de archivos de texto.
## Objetivo
El objetivo principal del proyecto es brindar una herramienta que permita gestionar las finanzas personales, a partir del registro de ciertos movimientos de dinero y la provisión de una agenda de pagos. Además, busca facilitar el acceso a los datos de otros contactos para realizar transferencias. 
## Público Objetivo
Esta propuesta está dirigida a todas aquellas personas que deseen acceder de manera rápida y sencilla a su estado financiero, ofreciendo la posibilidad de anticipar el mismo de acuerdo a los próximos pagos registrados en la agenda de facturas.
## Requerimientos Funcionales
1. Funcionalidades Básicas
    - Perfil: Permitir al usuario registrar y modificar su nombre completo, correo electrónico y número de celular. También, proporcionarle los datos de su propia cuenta para la realización de transferencias. 
    - Ingresar dinero a cuenta: Permitir al usuario ingresar un monto de dinero a la propia cuenta de VIRTUAL WALLET.
    - Transferir dinero: Permitir al usuario realizar una transferencia a un nuevo contacto o a uno ya existente. Se le proporciona la posibilidad de gestionar sus contactos, a partir de las siguientes funcionalidades: ingresar nuevo contacto (registrando su nombre, DNI, alias y número de CBU), buscar un contacto existente a través de su número de DNI y modificar sus datos, borrar un contacto existente y visualizar los contactos ya guardados.
    - Saldo disponible: Permitir al usuario consultar su saldo actual, teniendo en cuenta los ingresos de dinero y las transferencias realizadas.
    - Agenda de facturas: Permitir al usuario registrar las facturas a pagar (detallando el nombre de la empresa, el servicio al que pertenece, la fecha de vencimiento y el monto a abonar), como así también visualizar los servicios que ya se encuentran cargados.
2. Persistencia de Datos
    - Almacenamiento en Archivos de Texto: Utilizar archivos de texto para guardar y leer los contactos para las transferencias, la agenda de las facturas a pagar y el saldo disponible de acuerdo a los movimientos realizados. 
    - Formato del Archivo: Cada movimiento de dinero (ingresos y transferencias, que alteran el saldo), el registro y modificación de contactos como así también el ingreso de facturas en la agenda, deben almacenarse en un archivo con formato JSON.
3. Interfaz de Usuario
    - Interfaz de Consola: Proporcionar una interfaz de línea de comandos que permita al usuario interactuar con su billetera virtual.
    - Menú Principal: Ofrecer un menú principal desde el cual el usuario pueda seleccionar las diferentes funcionalidades (Perfil, Ingresar dinero a cuenta, Transferir dinero, Saldo disponible y Agenda de facturas).
4.  Validaciones de Datos
    - Entrada de Usuario: Validar la entrada del usuario para asegurar que los montos de dinero sean mayores a $0.
    - Gestión de Errores: Manejar posibles errores, como intentos de ingresar letras en lugar de números u opciones no válidas. También búsqueda de números de DNI que no se encuentran registrados en la billetera virtual. 
5.  Estructura del Código
    - Modularidad: Organizar el código en funciones para mejorar la legibilidad y mantenibilidad.
    - Funciones Principales: Crear funciones específicas para registrar y modificar los datos del perfil; ingresar y transferir dinero; agregar, modificar, borrar y visualizar los contactos para transferencias; y agregar y visualizar las facturas. 
    - Manejo de Archivos: Crear funciones para leer y escribir en los archivos de texto.
6.  Documentación
    - Comentarios en el Código: Incluir comentarios en el código para explicar el propósito y funcionamiento de las diferentes partes.
    - Archivo README: Proporcionar un archivo README que describa el propósito del proyecto, cómo ejecutarlo y cómo utilizar las diferentes funcionalidades.