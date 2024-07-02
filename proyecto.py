'''
Virtual wallet 
Autores: Causarano Daniela, More Julieta
Fecha: 2024
Version 1.0

''' 
import os 
import colorama
import getpass #para que no se muestre la contraseña mientras estas escribiendo.
import datetime
import json


def limpiarpantalla():
    '''
    Función limpiarpantalla()
    Autores: Causarano Daniela, More Julieta
    Fecha: 2024
    Version 1.0
    Parametros: no requiere
    Retorno: no tiene

    '''
    os.system('cls' if os.name == 'nt' else 'clear')
    return

Usuario="Grupo16"
Clave="CAC2024"
def verificar_persona():
    '''
    Función verificar_persona()
    Autores: Causarano Daniela, More Julieta
    Fecha: 2024
    Version 1.0
    Parametros: no requiere
    Retorno: si retorna, bool (True si la verificación es exitosa, False en caso contrario)

    '''
    global Usuario, Clave
    i=3
    while i > 0:
        usu=input(("Ingrese usuario: ").rjust(65," "))
        clave1=getpass.getpass(("Ingrese contraseña: ").rjust(68," "))

        if usu==Usuario and clave1==Clave:
            return True
        else:
            i-=1
            print()
            print(("Usuario y/o contraseña inválidos".rjust(80," ")))
            print((f"Le quedan {i} intentos").rjust(68," "))
            if i == 0:
                print()
                print(("Ha superado el máximo de intentos permitidos. Salga e intentelo de nuevo").rjust(120," "))
                return False
def menu():
    '''
    Función menu()
    Autores: Causarano Daniela, More Julieta
    Fecha: 2024
    Version 1.0
    Parametros: no requiere
    Retorno: si retorna, la opción seleccionada por el usuario

    '''
    limpiarpantalla()
    print(colorama.Fore.GREEN + "VIRTUAL WALLET".center(45))
    print(colorama.Fore.RESET + "="*45)
    print(colorama.Fore.LIGHTMAGENTA_EX + "1-"+ colorama.Fore.RESET +  "perfil".capitalize())
    print(colorama.Fore.LIGHTMAGENTA_EX + "2-" + colorama.Fore.RESET + "ingresar dinero a cuenta".capitalize())
    print(colorama.Fore.LIGHTMAGENTA_EX + "3-" + colorama.Fore.RESET + "transferir dinero".capitalize().ljust(40," ") )
    print(colorama.Fore.LIGHTMAGENTA_EX + "4-" + colorama.Fore.RESET + "saldo disponible".capitalize() )
    print(colorama.Fore.LIGHTMAGENTA_EX + "5-" + colorama.Fore.RESET + "agenda de facturas".capitalize() )
    print(colorama.Fore.LIGHTMAGENTA_EX + "6-" + colorama.Fore.RESET + "imprimir resumen de cuenta".capitalize() )
    print(colorama.Fore.LIGHTMAGENTA_EX + "7-" + colorama.Fore.RESET + "salir".capitalize() )
    print(colorama.Fore.RESET + "="*45)
    try:
        op=int(input(colorama.Fore.LIGHTYELLOW_EX + "Seleccione una opción: " + colorama.Fore.RESET))
    except ValueError:
        op=0 #lo inicializamos con 0 para asegurarnos de que siempre tenga un valor asignado 
        print("¡ERROR!")
    return op


def perfil():
    '''
    Función Perfil()
    Autores: Causarano Daniela, More Julieta
    Fecha: 2024
    Version 1.0
    Parametros: no requiere 
    Retorno: no

    '''
    limpiarpantalla()
    print()
    print(colorama.Fore.RED + "¡ATENCIÓN! Debe registrarse para poder acceder al menú" + colorama.Fore.RESET)
    print()
    print()

    nomCom=(input("Ingresa tu nombre completo: ").title())
    mail=input("Ingresa tu correo electrónico: ")
    nTel=int(input("Ingresa tu número de célular: "))
    configuracion= {
        "Nombre": nomCom,
        "Correo electrónico": mail,
        "Célular": nTel
    }
    limpiarpantalla()
    print(f"""
¡Bienvenido/a!
Nombre: {nomCom}\nCorreo: {mail}\nCélular: {nTel}""")
    print()
    print()
    print()
    rta=int(input("""
1-Configuración
2-Ver Datos de Transferencia
3- Salir 
""" ))
    while True:
        if rta == 1:
            rta2=(input("""
Elija la opcion que desea modificar: 
    A) Nombre Completo
    B) Correo Electrónico
    C) Número de Célular
    """).upper())
            
            match rta2:
                case "A":
                   nomCom=input("Ingrese el nuevo nombre completo: ")
                   print("¡Nombre completo modificado correctamente!") 
                   configuracion["Nombre"]=nomCom
                   break
                case "B":
                    mail=input("Ingrese el nuevo correo electrónico: ")
                    print("¡Correo electrónico modificado correctamente!")
                    configuracion["Correo electrónico"]=mail
                    break
                case "C":
                    nroTel=int(input("Ingrese el nuevo número de célular: "))
                    print("¡Número de celular modificado correctamente!") 
                    configuracion["Célular"]=nroTel
                    break
                case _: 
                    print("Opción no válida.")
        elif rta == 2:
            limpiarpantalla()
            print(colorama.Fore.BLUE + "CBU: 0040888777532") 
            print(colorama.Fore.BLUE + "Alias: PATO.CONEJO.PERRO")
            input(colorama.Fore.RED + "Presione enter para continuar")
        elif rta == 3:
            break
     
    return
   

def cargar_datosSaldo():
    '''
    Función cargar_datosSaldo()
    Autores: Causarano Daniela, More Julieta
    Fecha: 2024
    Version 1.0
    Parametros: no requiere 
    Retorno: sí retorna, lista vacía

    '''
    try:
        with open("saldo.json","r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def guardar_datosSaldo(saldo):
    '''
    Función guardar_datosSaldo(saldo)
    Autores: Causarano Daniela, More Julieta
    Fecha: 2024
    Version 1.0
    Parametros: sí requiere
    Retorno: no

    '''
    with open("saldo.json","w") as file:
        json.dump(saldo, file, indent=4)
        return

Saldo=[] # lo inicializamos afuera de la función para que no se pierdan los datos y pop funcione correctamente

def ingresar_dinero(dinero1):
    '''
    Función ingresar_dinero()
    Autores: Causarano Daniela, More Julieta
    Fecha: 2024
    Version 1.0
    Parametros: si requiere (1)
    Retorno: no retorna nada

    '''
    
    global saldo
    try:
        dinero1=float(dinero1)
        if dinero1 <= 0:
            print("El monto debe ser mayor a 0")
            print("Vuelva a intentar")
    except ValueError:
        print("Entrada no válida. Por favor ingrese números.")
        return
    
    if dinero1 != 0:
        saldo.append(dinero1)
        print(f"Cantidad: ${dinero1} ")
        while True:
            resp=input("¿Es correcto? s/n: ")
            if resp.lower() == "s":
                print("Dinero Despositado con éxito")
                break
            elif resp.lower() == "n":
                saldo.pop()
                dinero1=float(input("Vuelva a ingresar la cantidad de dinero a depositar: "))
                saldo.append(dinero1)
                print("Dinero depositado con éxito")
        guardar_datosSaldo(saldo)
        return

def cargar_datosContactos():
    '''
    Función cargar_datosContactos()
    Autores: Causarano Daniela, More Julieta
    Fecha: 2024
    Version 1.0
    Parametros: no requiere 
    Retorno: sí retorna, lista vacía

    '''
    try:
        with open("contactos.json","r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def guardar_datosContactos(nuevo_contacto):
    '''
    Función guardar_datosContactos()
    Autores: Causarano Daniela, More Julieta
    Fecha: 2024
    Version 1.0
    Parametros: no requiere 
    Retorno: no 

    '''
    for key in nuevo_contacto:
        if isinstance(nuevo_contacto[key], set):
            nuevo_contacto[key]=list(nuevo_contacto[key])

    with open("contactos.json","w") as file:
        json.dump(nuevo_contacto,file,indent=4)
        return


def transferir_dinero(aliasC, cbuC, dniC, nuevo_contacto):
        '''
    Función transferir_dinero()
    Autores: Causarano Daniela, More Julieta
    Fecha: 2024
    Version 1.0
    Parametros: si requiere (4)
    Retorno: si retorna, contactos

    '''
        print(f" Alias: {aliasC}\n CBU: {cbuC}\n DNI: {dniC}")
        while True:
            resp=input("¿Es correcto? s/n: ")
            if resp.lower() == "s":
                print("Contacto creado con exito!")
                break
            elif resp.lower() == "n":
                rta=int(input("""
    Elija que quiere modificar: 
            1) ALIAS 
            2) CBU 
            3) DNI 
            4) Todos los datos:  """)) 
                if rta == 1:
                    aliasC=input("Ingrese el alias de su contacto:  ")
                    nuevo_contacto["Alias"]=aliasC
                    print("Contacto modificado con exito!")
                    break
                elif rta == 2:
                    cbuC=input("Ingrese el CBU de su contacto: ")
                    nuevo_contacto["CBU"]=cbuC
                    print("Contacto modificado con exito!")
                    break
                elif rta == 3:
                    dniC=int(input("Ingrese el DNI de su contacto: "))
                    nuevo_contacto["DNI"]=dniC
                    print("Contacto modificado con exito!")
                    break
                elif rta == 4:
                    aliasC=input("Ingrese el alias de su contacto:  ")
                    emailC=input("Ingrese el CBU de su contacto: ")
                    dniC=int(input("Ingrese el DNI de su contacto: "))
                    nuevo_contacto["Alias"]=aliasC
                    nuevo_contacto["CBU"]=cbuC
                    nuevo_contacto["DNI"]=dniC
                    print("Contacto modificado con exito!") 
                    break 
                else:
                    print("Opción no válida. Intentelo de nuevo")
            else:
                print("Respuesta no válida.")
        guardar_datosContactos(nuevo_contacto)
        return
# hay que crear una opcion para ver los contactos guardados y seleccionar uno y transferir.
# agregar op para borrar contacto.

def ver_saldo():
    '''
    Función ver_saldo()
    Autores: Causarano Daniela, More Julieta
    Fecha: 2024
    Version 1.0
    Parametros: no requiere 
    Retorno: no retorna

    '''
    limpiarpantalla()
    global saldo
    total_saldo=sum(saldo)
    print(f"Saldo actual: ${total_saldo:.2f}")
    # tenemos que restar lo que se debita para ver el saldo total
    return

def agenda_fras():
    limpiarpantalla()
    Fras1=(input("Ingrese la empresa a la cual pertenece la factura: ").capitalize())    
    Fras2=(input("Ingrese a que servicio pertenece: ").capitalize())
    Fras3=float(input("Ingrese el monto a pagar: "))
    Fras4=input("Ingrese el día que vence: ")
    fras4 = datetime.datetime.strptime(Fras4, '%d/%m/%Y') # Utilizamos datetime.datetime.strptime para convertir la cadena de texto en un objeto datetime
    Facturas={}
    Facturas[Fras2]={
            "Empresa": Fras1,
            "Monto": Fras3,
            "Fecha de vto":fras4
    }
    print(Facturas)
    

#programa principal
agenda_fras()
colorama.init()
saldo=cargar_datosSaldo()
nuevo_contacto=cargar_datosContactos()

while True:
    if not verificar_persona():
        break
    perfil()
# preguntar porque sigue abriendo.

while perfil() == True:
        op = menu()
        if op == 1:
            print("Perfil")
            print("-" * 24)
            perfil()
            input(colorama.Fore.RED + "Presione enter para continuar")
        elif op == 2:
            print("Ingresar dinero a cuenta")
            print("-" * 24)
            dinero1 = float(input("Ingrese la cantidad de dinero a depositar: "))
            ingresar_dinero(dinero1)
            input(colorama.Fore.RED + "Presione enter para continuar")
        elif op == 3:
            print("Transferir dinero")
            print("-" * 24)
            alias=input("Ingrese el alias de su contacto:  ")
            cbu=int(input("Ingrese el CBU de su contacto: "))
            dni=int(input("Ingrese el DNI de su contacto: "))
            nom=input("Ingrese el nombre de su contacto: ")
            nuevo_contacto[nom]={
                       "Alias": alias,
                       "CBU": cbu,
                       "DNI": dni,
                    }
            transferir_dinero(alias, cbu, dni, nuevo_contacto)
            input(colorama.Fore.RED + "Presione enter para continuar")
        elif op == 4:
            print("Ver saldo disponible")
            print("-" * 24)
            ver_saldo()
            input(colorama.Fore.RED + "Presione enter para continuar")
        elif op == 5:
            print("Agenda de Facturas")
            print("-" * 24)
            agenda_fras()
            input(colorama.Fore.RED + "Presione enter para continuar")
        elif op == 6:
            print("Imprimir resumen de cuenta")
            print("-" * 24)
            input(colorama.Fore.RED + "Presione enter para continuar")
        elif op == 7:
            print("Saliendo")
            input(colorama.Fore.RED + "Presione enter para continuar")
            break
        else:
            print("Por favor ingrese una opción válida.")
            input(colorama.Fore.RED + "Presione enter para continuar")