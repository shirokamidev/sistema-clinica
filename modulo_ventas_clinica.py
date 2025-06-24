episodios = {}
pacientes = {}
productos = {}
farmacos = {}
insumos = {}
prestaciones = {}

titulo_menu_ventas = "--- MÓDULO DE VENTAS Y ATENCIÓN ---"
lista_ops = []
lista_ops.append("1.- Crear episodio de atención")
lista_ops.append("2.- Asignar atención al paciente")
lista_ops.append("3.- Calcular precio de atención")
lista_ops.append("4.- Reporte de ventas por período")
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

def crear_episodio():
    print(">>> Crear Episodio")
    codigo = input("Código del episodio: ").strip()
    if codigo in episodios:
        print("Ya existe un episodio con ese código.")
    else:
        paciente = input("Código del paciente: ").strip()
        if paciente not in pacientes:
            print("Paciente no registrado.")
        else:
            fecha = input("Fecha de atención (dd-mm-aaaa): ").strip()
            episodios[codigo] = {
                "paciente": paciente,
                "fecha": fecha,
                "productos": [],
                "farmacos": [],
                "insumos": [],
                "prestaciones": [],
                "costo_total": 0,
                "precio_venta": 0,
                "margen": 0
            }
            print("Episodio creado.")

def asignar_atencion():
    print(">>> Asignar Atención")
    codigo = input("Código del episodio: ").strip()
    if codigo not in episodios:
        print("Episodio no encontrado.")
    else:
        seguir = True
        while seguir == True:
            print("1. Producto terminado\n2. Fármaco\n3. Insumo clínico\n4. Prestación médica\n5. Salir")
            tipo = validar_opcion(5)

            if tipo == 1:
                ref = input("Código del producto terminado: ").strip()
                if ref in productos:
                    costo = float(input("Costo del producto: "))
                    episodios[codigo]["productos"].append({"codigo": ref, "costo": costo})
                    print("Producto registrado.")
                else:
                    print("No existe ese producto.")
            elif tipo == 2:
                ref = input("Código del fármaco: ").strip()
                if ref in farmacos:
                    costo = float(input("Costo del fármaco: "))
                    episodios[codigo]["farmacos"].append({"codigo": ref, "costo": costo})
                    print("Fármaco registrado.")
                else:
                    print("No existe ese fármaco.")
            elif tipo == 3:
                ref = input("Código del insumo: ").strip()
                if ref in insumos:
                    costo = float(input("Costo del insumo: "))
                    episodios[codigo]["insumos"].append({"codigo": ref, "costo": costo})
                    print("Insumo registrado.")
                else:
                    print("No existe ese insumo.")
            elif tipo == 4:
                ref = input("Código de la prestación: ").strip()
                if ref in prestaciones:
                    costo = float(input("Costo de la prestación: "))
                    episodios[codigo]["prestaciones"].append({"codigo": ref, "costo": costo})
                    print("Prestación registrada.")
                else:
                    print("No existe esa prestación.")
            elif tipo == 5:
                seguir = False

def calcular_precio_atencion():
    print(">>> Calcular Precio de Atención")
    codigo = input("Código del episodio: ").strip()
    if codigo not in episodios:
        print("Episodio no existe.")
    else:
        total = 0
        venta = 0

        for item in episodios[codigo]["productos"]:
            total += item["costo"]
            venta += item["costo"] * 1.6
        for item in episodios[codigo]["farmacos"]:
            total += item["costo"]
            venta += item["costo"] * 1.5
        for item in episodios[codigo]["insumos"]:
            total += item["costo"]
            venta += item["costo"] * 1.4
        for item in episodios[codigo]["prestaciones"]:
            total += item["costo"]
            venta += item["costo"] * 1.55

        margen = venta - total
        episodios[codigo]["costo_total"] = round(total, 2)
        episodios[codigo]["precio_venta"] = round(venta, 2)
        episodios[codigo]["margen"] = round(margen, 2)

        print(f"Costo total: ${round(total, 2)}")
        print(f"Precio de venta: ${round(venta, 2)}")
        print(f"Margen generado: ${round(margen, 2)}")

def reporte_ventas():
    print(">>> Reporte de Ventas")
    if len(episodios) == 0:
        print("No hay episodios registrados.")
    else:
        for codigo, datos in episodios.items():
            paciente = datos["paciente"]
            fecha = datos["fecha"]
            costo = datos["costo_total"]
            venta = datos["precio_venta"]
            margen = datos["margen"]
            print(f"\nEpisodio: {codigo} | Paciente: {paciente} | Fecha: {fecha}")
            print(f"Costo: ${round(costo, 2)} | Venta: ${round(venta, 2)} | Margen: ${round(margen, 2)}")

salir_ventas = False
while salir_ventas == False:
    ver_menu(titulo_menu_ventas, lista_ops)
    opcion = validar_opcion(len(lista_ops))

    if opcion == 1:
        crear_episodio()
    elif opcion == 2:
        asignar_atencion()
    elif opcion == 3:
        calcular_precio_atencion()
    elif opcion == 4:
        reporte_ventas()
    elif opcion == 5:
        salir_ventas = True