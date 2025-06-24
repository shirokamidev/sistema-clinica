productos = {}
composiciones = {}
ordenes_produccion = []
inventario = {}

titulo_menu_produccion = "--- MÓDULO DE PRODUCCIÓN ---"
lista_ops = []
lista_ops.append("1.- Crear composición de producto terminado")
lista_ops.append("2.- Crear orden de producción")
lista_ops.append("3.- Ejecutar fabricación")
lista_ops.append("4.- Reporte de stock de productos terminados")
lista_ops.append("5.- Volver al menú principal")

def ver_menu(titulo_menu, opciones):
    print("\n" + titulo_menu)
    for item in opciones:
        print(item)

def validar_opcion(total_opciones):
    valido = False
    while valido == False:
        try:
            seleccion = int(input("Selecciona una opción: "))
            if seleccion <= 0 or seleccion > total_opciones:
                print("Opción no válida.")
            else:
                valido = True
                return seleccion
        except ValueError:
            print("Debe ingresar un número válido.")

def crear_composicion():
    print(">>> Crear Composición de Producto Terminado")
    codigo = input("Código del producto terminado: ").strip()
    descripcion = input("Descripción: ").strip()

    productos[codigo] = {"descripcion": descripcion, "stock": 0}
    composiciones[codigo] = []

    agregar_insumos = True
    while agregar_insumos == True:
        insumo = input("Código del insumo/fármaco: ").strip()
        cantidad_valida = False
        while cantidad_valida == False:
            try:
                cantidad = int(input("Cantidad necesaria: "))
                if cantidad <= 0:
                    print("Debe ser mayor a cero.")
                else:
                    cantidad_valida = True
            except ValueError:
                print("Ingrese número válido.")

        composiciones[codigo].append({"codigo": insumo, "cantidad": cantidad})
        continuar = input("¿Agregar otro insumo? (s/n): ").lower()
        if continuar != "s":
            agregar_insumos = False

    print("Composición registrada con éxito.")

def crear_orden_produccion():
    print(">>> Crear Orden de Producción")
    codigo = input("Código del producto terminado: ").strip()
    if codigo not in composiciones:
        print("Ese producto no tiene una composición registrada.")
    else:
        cantidad_valida = False
        while cantidad_valida == False:
            try:
                cantidad = int(input("Cantidad a producir: "))
                if cantidad <= 0:
                    print("Debe ser mayor a cero.")
                else:
                    cantidad_valida = True
            except ValueError:
                print("Ingrese número válido.")

        ordenes_produccion.append({"producto": codigo, "cantidad": cantidad})
        print("Orden de producción registrada.")

def ejecutar_fabricacion():
    print(">>> Ejecutar Fabricación")
    if len(ordenes_produccion) == 0:
        print("No hay órdenes registradas.")
    else:
        for i in range(len(ordenes_produccion)):
            orden = ordenes_produccion[i]
            codigo = orden["producto"]
            cantidad = orden["cantidad"]
            print(f"{i + 1}. Producto: {codigo} | Cantidad: {cantidad}")

        seleccion_valida = False
        while seleccion_valida == False:
            try:
                seleccion = int(input("Seleccione el número de la orden a ejecutar: "))
                if seleccion <= 0 or seleccion > len(ordenes_produccion):
                    print("Número fuera de rango.")
                else:
                    seleccion_valida = True
            except ValueError:
                print("Ingrese un número válido.")

        orden = ordenes_produccion[seleccion - 1]
        codigo_prod = orden["producto"]
        cantidad_prod = orden["cantidad"]
        insumos_necesarios = composiciones[codigo_prod]

        faltante = False
        for item in insumos_necesarios:
            insumo = item["codigo"]
            requerido = item["cantidad"] * cantidad_prod
            if insumo not in inventario or inventario[insumo]["stock"] < requerido:
                print(f"No hay suficiente stock de {insumo}. Se necesitan {requerido}.")
                faltante = True

        if faltante == False:
            for item in insumos_necesarios:
                insumo = item["codigo"]
                requerido = item["cantidad"] * cantidad_prod
                inventario[insumo]["stock"] -= requerido

            productos[codigo_prod]["stock"] += cantidad_prod
            print("Fabricación completada.")
        else:
            print("La orden no puede ejecutarse por falta de insumos.")

def reporte_productos_terminados():
    print("--- STOCK DE PRODUCTOS TERMINADOS ---")
    if len(productos) == 0:
        print("No hay productos registrados.")
    else:
        for codigo, datos in productos.items():
            print(f"{codigo}: {datos['descripcion']} | Stock: {datos['stock']}")

salir_produccion = False
while salir_produccion == False:
    ver_menu(titulo_menu_produccion, lista_ops)
    opcion = validar_opcion(len(lista_ops))

    if opcion == 1:
        crear_composicion()
    elif opcion == 2:
        crear_orden_produccion()
    elif opcion == 3:
        ejecutar_fabricacion()
    elif opcion == 4:
        reporte_productos_terminados()
    elif opcion == 5:
        salir_produccion = True