inventario = {}

titulo_menu_inventario = "--- MÓDULO DE INVENTARIO CLÍNICO ---"
lista_ops = []
lista_ops.append("1.- Registrar pedido a proveedor")
lista_ops.append("2.- Recepción de fármacos e insumos clínicos")
lista_ops.append("3.- Ver stock actual")
lista_ops.append("4.- Reporte de ítems bajo stock mínimo")
lista_ops.append("5.- Volver al menú principal")

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

def registrar_pedido():
    print(">>> Registrar Pedido a Proveedor")
    codigo_valido = False
    while codigo_valido == False:
        codigo = input("Código del fármaco o insumo: ").strip()
        if codigo == "":
            print("Código no puede estar vacío.")
        else:
            codigo_valido = True

    proveedor = input("Nombre del proveedor: ").strip()
    cantidad_valida = False
    while cantidad_valida == False:
        try:
            cantidad = int(input("Cantidad solicitada: "))
            if cantidad <= 0:
                print("Cantidad debe ser mayor a cero.")
            else:
                cantidad_valida = True
        except ValueError:
            print("Debe ingresar un número válido.")

    print("Pedido registrado (simulado). Se espera la recepción para ingreso en stock.")

def recepcion_productos():
    print(">>> Recepción de Productos")
    codigo = input("Código del producto recibido: ").strip()
    descripcion = input("Descripción: ").strip()

    cantidad_valida = False
    while cantidad_valida == False:
        try:
            cantidad = int(input("Cantidad recibida: "))
            if cantidad <= 0:
                print("Cantidad debe ser mayor a cero.")
            else:
                cantidad_valida = True
        except ValueError:
            print("Debe ingresar un número válido.")

    costo_valido = False
    while costo_valido == False:
        try:
            costo = float(input("Costo unitario: "))
            if costo <= 0:
                print("El costo debe ser positivo.")
            else:
                costo_valido = True
        except ValueError:
            print("Debe ingresar un valor numérico válido.")

    minimo_valido = False
    while minimo_valido == False:
        try:
            minimo = int(input("Stock mínimo para este producto: "))
            if minimo < 0:
                print("El stock mínimo no puede ser negativo.")
            else:
                minimo_valido = True
        except ValueError:
            print("Debe ingresar un número entero válido.")

    if codigo not in inventario:
        inventario[codigo] = {
            "descripcion": descripcion,
            "stock": cantidad,
            "costo": costo,
            "minimo": minimo
        }
    else:
        inventario[codigo]["stock"] += cantidad
        inventario[codigo]["costo"] = costo
        inventario[codigo]["minimo"] = minimo

    print("Producto ingresado al inventario correctamente.")

def ver_stock():
    print("--- STOCK ACTUAL DE FÁRMACOS E INSUMOS CLÍNICOS ---")
    if len(inventario) == 0:
        print("Inventario vacío.")
    else:
        for codigo, datos in inventario.items():
            print(f"{codigo}: {datos['descripcion']} | Stock: {datos['stock']} | Costo: ${datos['costo']:.2f}")

def reporte_stock_minimo():
    print("--- REPORTE DE STOCK POR DEBAJO DEL MÍNIMO ---")
    alguno_bajo = False
    for codigo, datos in inventario.items():
        if datos["stock"] < datos["minimo"]:
            print(f"{codigo}: {datos['descripcion']} | Stock: {datos['stock']} < Mínimo: {datos['minimo']}")
            alguno_bajo = True
    if not alguno_bajo:
        print("Todo el inventario está por sobre el mínimo establecido.")

salir_inventario = False
while salir_inventario == False:
    ver_menu(titulo_menu_inventario, lista_ops)
    opcion = validar_opcion(len(lista_ops))

    if opcion == 1:
        registrar_pedido()
    elif opcion == 2:
        recepcion_productos()
    elif opcion == 3:
        ver_stock()
    elif opcion == 4:
        reporte_stock_minimo()
    elif opcion == 5:
        salir_inventario = True