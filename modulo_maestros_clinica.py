#aaaa
pacientes = {}
farmacos = {}
insumos = {}
productos = {}
prestaciones = {}
proveedores = {}

titulo_menu = "--- MANTENCIÓN DE MAESTROS ---"
lista_ops = []
lista_ops.append("1.- Gestionar Pacientes")
lista_ops.append("2.- Gestionar Fármacos")
lista_ops.append("3.- Gestionar Insumos Clínicos")
lista_ops.append("4.- Gestionar Productos Terminados")
lista_ops.append("5.- Gestionar Prestaciones Médicas")
lista_ops.append("6.- Gestionar Proveedores")
lista_ops.append("7.- Volver al menú principal")

def ver_menu(titulo_menu, opciones):
    print("\n" + titulo_menu)
    for item in opciones:
        print(item)

def validar_opcion(total_opciones):
    opcion_valida = False
    while opcion_valida == False:
        try:
            seleccion = int(input("Selecciona una opción: "))
            if seleccion <= 0 or seleccion > total_opciones:
                print(f"Opción no válida. Introduzca un número del 1 al {total_opciones}.")
            else:
                opcion_valida = True
                return seleccion
        except ValueError:
            print("Opción no válida. El valor ingresado debe ser numérico.")

def crear_registro(diccionario):
    codigo_valido = False
    while codigo_valido == False:
        codigo = input("Ingrese código: ").strip()
        if codigo == "" or " " in codigo:
            print("Código inválido. No puede estar vacío ni contener espacios.")
        elif codigo in diccionario:
            print("Ese código ya está registrado.")
        else:
            codigo_valido = True

    descripcion_valida = False
    while descripcion_valida == False:
        descripcion = input("Ingrese descripción: ").strip()
        if descripcion == "":
            print("La descripción no puede estar vacía.")
        else:
            descripcion_valida = True

    diccionario[codigo] = {"descripcion": descripcion, "estado": "activo"}
    print("Registro creado correctamente.")

def modificar_registro(diccionario):
    codigo = input("Ingrese código a modificar: ").strip()
    if codigo in diccionario:
        nueva_descripcion_valida = False
        while nueva_descripcion_valida == False:
            nueva = input("Nueva descripción: ").strip()
            if nueva == "":
                print("La descripción no puede estar vacía.")
            else:
                nueva_descripcion_valida = True
        diccionario[codigo]["descripcion"] = nueva
        print("Registro actualizado.")
    else:
        print("Código no encontrado.")

def bloquear_registro(diccionario):
    codigo = input("Ingrese código a bloquear: ").strip()
    if codigo in diccionario:
        diccionario[codigo]["estado"] = "bloqueado"
        print("Registro bloqueado.")
    else:
        print("Código no encontrado.")

def listar_registros(diccionario):
    if len(diccionario) == 0:
        print("No hay registros para mostrar.")
    else:
        for cod, datos in diccionario.items():
            print(f"Código: {cod} | Descripción: {datos['descripcion']} | Estado: {datos['estado']}")

def menu_gestion(diccionario, titulo):
    lista_sub = []
    lista_sub.append("1.- Crear")
    lista_sub.append("2.- Modificar")
    lista_sub.append("3.- Bloquear")
    lista_sub.append("4.- Listar")
    lista_sub.append("5.- Volver")

    salir = False
    while salir == False:
        ver_menu(titulo, lista_sub)
        opcion = validar_opcion(len(lista_sub))

        if opcion == 1:
            crear_registro(diccionario)
        elif opcion == 2:
            modificar_registro(diccionario)
        elif opcion == 3:
            bloquear_registro(diccionario)
        elif opcion == 4:
            listar_registros(diccionario)
        elif opcion == 5:
            salir = True

salir_maestros = False
while salir_maestros == False:
    ver_menu(titulo_menu, lista_ops)
    opcion = validar_opcion(len(lista_ops))

    if opcion == 1:
        menu_gestion(pacientes, "--- GESTIÓN DE PACIENTES ---")
    elif opcion == 2:
        menu_gestion(farmacos, "--- GESTIÓN DE FÁRMACOS ---")
    elif opcion == 3:
        menu_gestion(insumos, "--- GESTIÓN DE INSUMOS CLÍNICOS ---")
    elif opcion == 4:
        menu_gestion(productos, "--- GESTIÓN DE PRODUCTOS TERMINADOS ---")
    elif opcion == 5:
        menu_gestion(prestaciones, "--- GESTIÓN DE PRESTACIONES MÉDICAS ---")
    elif opcion == 6:
        menu_gestion(proveedores, "--- GESTIÓN DE PROVEEDORES ---")
    elif opcion == 7:
        salir_maestros = True