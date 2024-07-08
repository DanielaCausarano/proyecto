'''
Virtual wallet 
Autores: Causarano Daniela, More Julieta
Fecha: 2024
Version 1.0

''' 

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


global Usuario
global Clave
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

    i=3
    while i > 0:
        usu=input((colorama.Fore.LIGHTGREEN_EX +"Ingrese usuario: "+ colorama.Fore.RESET).rjust(65," "))
        clave1=getpass.getpass((colorama.Fore.LIGHTMAGENTA_EX +"Ingrese contraseña: " + colorama.Fore.RESET).rjust(73," "))

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
    print(colorama.Fore.LIGHTMAGENTA_EX + "6-" + colorama.Fore.RESET + "salir".capitalize() )
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
    Versión 1.0
    Parámetros: no requiere 
    Retorno: no
    '''
    nomCom = (input(colorama.Fore.LIGHTCYAN_EX + "Ingresa tu nombre completo: "+ colorama.Fore.RESET).title())
    mail = input(colorama.Fore.LIGHTCYAN_EX + "Ingresa tu correo electrónico: "+ colorama.Fore.RESET)
    nTel = int(input(colorama.Fore.LIGHTCYAN_EX + "Ingresa tu número de celular: " + colorama.Fore.RESET))
    configuracion = {
        "Nombre": nomCom,
        "Correo electrónico": mail,
        "Celular": nTel
    }
    
    while True:
        limpiarpantalla()
        print(f"""
¡Bienvenido/a!
Nombre: {nomCom}\nCorreo: {mail}\nCelular: {nTel}""")
        print()
        print()
        print()
        rta = int(input("""
1-Configuración
2-Ver Datos de Transferencia
3- Salir 
"""))
        
        if rta == 1:
            rta2 = input("""
Elija la opción que desea modificar: 
    A) Nombre Completo
    B) Correo Electrónico
    C) Número de Celular
    """).upper()
            
            match rta2:
                case "A":
                    nomCom = input(colorama.Fore.LIGHTCYAN_EX +"Ingrese el nuevo nombre completo: " + colorama.Fore.RESET)
                    print("¡Nombre completo modificado correctamente!") 
                    configuracion["Nombre"] = nomCom
                case "B":
                    mail = input(colorama.Fore.LIGHTCYAN_EX +"Ingrese el nuevo correo electrónico: "+ colorama.Fore.RESET)
                    print("¡Correo electrónico modificado correctamente!")
                    configuracion["Correo electrónico"] = mail
                case "C":
                    nroTel = int(input(colorama.Fore.LIGHTCYAN_EX +"Ingrese el nuevo número de celular: "+ colorama.Fore.RESET))
                    print("¡Número de celular modificado correctamente!") 
                    configuracion["Celular"] = nroTel
                case _: 
                    print("Opción no válida.")
        elif rta == 2:
            limpiarpantalla()
            print("CBU: 0040888777532") 
            print("Alias: PATO.CONEJO.PERRO")
            input("Presione enter para continuar")
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
    
def guardar_datosContactos(lista_contactos):
    '''
    Función guardar_datosContactos()
    Autores: Causarano Daniela, More Julieta
    Fecha: 2024
    Version 1.0
    Parametros: no requiere 
    Retorno: no 

    '''
    with open("contactos.json","w") as file:
        json.dump(lista_contactos,file,indent=4)
        return lista_contactos
    
def ingresarContacto (): 
    '''
    Función ingresarContacto ()
    Autores: Causarano Daniela, More Julieta
    Fecha: 2024
    Version 1.0
    Parametros: no requiere 
    Retorno: sí, lista_contactos

    '''
    nom=input(colorama.Fore.LIGHTCYAN_EX + "Ingrese el nombre de su contacto: "+ colorama.Fore.RESET)
    dni=int(input(colorama.Fore.LIGHTCYAN_EX +"Ingrese el DNI de su contacto: "+ colorama.Fore.RESET))
    alias=input(colorama.Fore.LIGHTCYAN_EX +"Ingrese el alias de su contacto:  "+ colorama.Fore.RESET)
    cbu=int(input(colorama.Fore.LIGHTCYAN_EX +"Ingrese el CBU de su contacto: "+ colorama.Fore.RESET))
    contacto={
        "Nombre": nom,
        "Alias": alias,
        "CBU": cbu,
        "DNI": dni,
    }
    lista_contactos.append(contacto)
    print ("Contacto creado con éxito!!")
    print (f"Usted realizará una transferencia a {contacto["Nombre"]}")
    guardar_datosContactos(lista_contactos)
    return lista_contactos

def opcionesContactos():
    print ("Seleccione")
    print ("1, para transferir a un nuevo contacto")
    print ("2, para transferir a un contacto existente")
    print ("3, para borrar contacto")
    print ("4, ver contactos guardados")
    opcion=input("Indique la opción elegida: ")
    if opcion=="1":
        ingresarContacto() 
        return True
    elif opcion=="2":
        dniC=int(input("Ingrese el N° de DNI del contacto: "))
        for i in range (len(lista_contactos)):
            if lista_contactos[i]["DNI"] == dniC:
                for c,v in lista_contactos[i].items():
                    print (lista_contactos[i])
                    resp=input("¿Los datos son correctos? s/n: ")
                    if resp.lower() == "s":
                        print (f"Usted realizará una transferencia a {lista_contactos[i]["Nombre"]}")
                        return True
                    elif resp.lower() == "n":
                        rta=int(input("""Elija qué quiere modificar:
                        1) NOMBRE
                        2) ALIAS 
                        3) CBU 
                        4) DNI 
                        """))
                        if rta == 1:
                            nom=input("Ingrese el nombre")
                            lista_contactos[i]["Nombre"]=nom
                            print("Nombre modificado con exito!")
                            break
                        elif rta== 2:
                            alias=input("Ingrese el alias de su contacto:  ")
                            lista_contactos["Alias"]=alias
                            print("Contacto modificado con exito!")
                            break
                        elif rta == 3:
                            cbu=input("Ingrese el CBU de su contacto: ")
                            lista_contactos[i]["CBU"]=cbu
                            print("Contacto modificado con exito!")
                            break
                        elif rta == 4:
                            dni=int(input("Ingrese el DNI de su contacto: "))
                            lista_contactos[i]["DNI"]=dni
                            print("Contacto modificado con exito!")
                            break
                        else:
                            print("Opción no válida. Inténtelo de nuevo")
                    guardar_datosContactos(lista_contactos)
                    return True
            else:             
                print ("DNI no encontrado. Regrese al Menú")
                return False
    elif opcion=="3":
        dni=int(input("Ingrese el N° de DNI del contacto: "))
        for i in range (len(lista_contactos)):
            if lista_contactos[i]["DNI"]==dni:
                for c, v in lista_contactos[i].items():
                    print (lista_contactos[i])
                    resp=input("¿Desea borrar el contacto? s/n")
                    if resp.lower() == "s":
                        lista_contactos.remove(lista_contactos[i])
                        print ("Contacto borrado")
                        guardar_datosContactos(lista_contactos)
                        return False
                    elif resp.lower() == "n":
                        print ("Regrese al Menú")
                        return False
            else:
                print ("DNI no encontrado. Regrese al Menú") 
                return False        
    elif opcion=="4":
        print (lista_contactos)
        return False
    else: 
        print ("Opción incorrecta")   
        return False
    
def transferir_dinero(dinero1):
    '''
    Función transferir_dinero()
    Autores: Causarano Daniela, More Julieta
    Fecha: 2024
    Version 1.0
    Parametros: si requiere (1)
    Retorno: si retorna, contactos

    '''
    global saldo
    try:
        dinero1=float(input(colorama.Fore.LIGHTCYAN_EX +"Indique la cantidad de dinero que desea transferir: " + colorama.Fore.RESET))
        if dinero1 <=0: 
            print("Debe ingresar una cantidad mayor a $0")
            print ("Vuelva a intentar")
        elif dinero1!=0:
            print(f"Usted ingresó ${dinero1}")
            dinero1=dinero1*-1 #para convertir dinero en negativo y reste en el saldo
            saldo.append(dinero1)
            while True:
                resp=input(colorama.Fore.LIGHTCYAN_EX +"¿Es correcto? s/n: " + colorama.Fore.RESET)
                if resp.lower() == "s":
                    print("Transferencia realizada con éxito!!")
                    break
                elif resp.lower() == "n":
                    saldo.pop()
                    dinero1=float(input(colorama.Fore.LIGHTCYAN_EX +"Ingrese nuevamente el dinero a transferir: "+ colorama.Fore.RESET))
                    dinero1=dinero1*-1
                    saldo.append(dinero1)
                    print("Transferencia realizada con éxito!!")
            guardar_datosSaldo(saldo)
            return
    except ValueError:
        print("Entrada no válida. Por favor ingrese números.")
        return

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
    input(colorama.Fore.RED + "Presione enter para continuar" + colorama.Fore.RESET)
    return


def cargar_datosAgenda():
    '''
    Función cargar_datosAgenda()
    Autores: Causarano Daniela, More Julieta
    Fecha: 2024
    Version 1.0
    Parametros: no requiere 
    Retorno: sí retorna, lista vacía

    '''
    try:
        with open("agenda.json","r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def guardar_datosAgenda(Facturas):
    '''
    Función guardar_datosAgenda()
    Autores: Causarano Daniela, More Julieta
    Fecha: 2024
    Version 1.0
    Parametros: no requiere 
    Retorno: no 

    '''
    with open("agenda.json","w") as file:
        json.dump(Facturas,file,indent=4)
        return 
    
def agenda_fras():
    '''
    Función agenda_fras()
    Autores: Causarano Daniela, More Julieta
    Fecha: 2024
    Version 1.0
    Parametros: no requiere 
    Retorno: no retorna
    '''
    Facturas = cargar_datosAgenda()  
    print( "1 - Agendar servicios a pagar: ")
    print( "2 - Ver servicios a pagar: " )

    rta = int(input("Seleccione una opción: "))
    if rta == 1:
        while True:
            Fras1 = input(colorama.Fore.LIGHTCYAN_EX +"Ingrese la empresa a la cual pertenece la factura (o 'fin' para salir): "+ colorama.Fore.RESET).capitalize()
            if Fras1.lower() == 'fin':
                break
            Fras2 = input(colorama.Fore.LIGHTCYAN_EX +"Ingrese a qué servicio pertenece: "+ colorama.Fore.RESET).capitalize()
            Fras3 = float(input(colorama.Fore.LIGHTCYAN_EX +"Ingrese el monto a pagar: "+ colorama.Fore.RESET))
            Fras4 = input(colorama.Fore.LIGHTCYAN_EX +"Ingrese el día que vence (DD/MM/AAAA): "+ colorama.Fore.RESET)
            fras4 = datetime.datetime.strptime(Fras4, '%d/%m/%Y').strftime('%d/%m/%Y')
            #Utilizamos datetime.datetime.strptime para convertir la cadena de texto en un objeto datetime
            Facturas[Fras2] = {
                "Empresa": Fras1,
                "Monto": Fras3,
                "Fecha de vto": fras4
            }
            print("¡Factura agendada!")

        guardar_datosAgenda(Facturas) 
    elif rta == 2:
        for servicio, datos in Facturas.items():
            fecha_vto = datetime.datetime.strptime(datos["Fecha de vto"], '%d/%m/%Y') # Convertir de nuevo a datetime
            print(f"Servicio: {servicio}, Empresa: {datos['Empresa']}, Monto: {datos['Monto']}, Fecha de vto: {fecha_vto.strftime('%d/%m/%Y')}")
    else:
        print("Opción no válida.")
    return


    
#programa principal
import os 
import colorama
import getpass #para que no se muestre la contraseña mientras estas escribiendo.
import datetime
import json
colorama.init()
saldo=cargar_datosSaldo()
lista_contactos=cargar_datosContactos()
dinero1=0
Saldo=[] # lo inicializamos afuera de la función para que pop funcione correctamente

while verificar_persona() == True:
        op = menu()
        if op == 1:
            print("Perfil")
            print("-" * 24)
            perfil()
            input(colorama.Fore.RED + "Presione enter para continuar" + colorama.Fore.RESET)
        elif op == 2:
            print("Ingresar dinero a cuenta")
            print("-" * 24)
            dinero1 = float(input(colorama.Fore.LIGHTCYAN_EX +"Ingrese la cantidad de dinero a depositar: " + colorama.Fore.RESET))
            ingresar_dinero(dinero1)
            input(colorama.Fore.RED + "Presione enter para continuar" + colorama.Fore.RESET)
        elif op == 3:
            print("Transferir dinero")
            print("-" * 24)
            limpiarpantalla()
            if opcionesContactos()== True:
                transferir_dinero(dinero1)
            input(colorama.Fore.RED + "Presione enter para continuar" + colorama.Fore.RESET)
        elif op == 4:
            print("Ver saldo disponible")
            print("-" * 24)
            ver_saldo()
            input(colorama.Fore.RED + "Presione enter para continuar" + colorama.Fore.RESET)
        elif op == 5:
            print("Agenda de Facturas")
            print("-" * 24)
            agenda_fras()
            input(colorama.Fore.RED + "Presione enter para continuar" + colorama.Fore.RESET)
        elif op == 6:
            print("Saliendo")
            input(colorama.Fore.RED + "Presione enter para continuar" + colorama.Fore.RESET)
            break
        else:
            print("Por favor ingrese una opción válida.")
            input(colorama.Fore.RED + "Presione enter para continuar" + colorama.Fore.RESET)
