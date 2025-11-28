import csv
import re

def leer_csv(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        reader = csv.reader(archivo)
        datos = list(reader)
    return datos

def total_clientes(datos):
    return len(datos) - 1 if len(datos) > 0 else 0

def ingresos_totales(datos, indice_total=8):
    total = 0.0
    for fila in datos[1:]:
        try:
            celda = fila[indice_total].strip()
            celda_limpia = re.sub(r"[^0-9.,-]", "", celda)
            celda_limpia = celda_limpia.replace(",", ".")
            total += float(celda_limpia)
        except:
            pass
    return total

def plato_mas_consumido(datos, indice_plato=4):
    contador = {}
    for fila in datos[1:]:
        if len(fila) <= indice_plato:
            continue
        plato = fila[indice_plato].strip()
        if plato:
            contador[plato] = contador.get(plato, 0) + 1
    
    if not contador:
        return None
    return max(contador, key=contador.get)  

def pedidos_por_categoria(datos, indice_categoria=5):
    categorias = {}
    for fila in datos[1:]:
        if len(fila) <= indice_categoria:
            continue
        cat = fila[indice_categoria].strip()
        if cat:
            categorias[cat] = categorias.get(cat, 0) + 1
    return categorias

def ventas_por_canal(datos, indice_canal=3, indice_total=8):
    canales = {}
    for fila in datos[1:]:
        if len(fila) <= indice_total:
            continue
        canal = fila[indice_canal].strip()
        celda = fila[indice_total].strip()
        celda_limpia = re.sub(r"[^0-9.,-]", "", celda).replace(",", ".")
        try:
            valor = float(celda_limpia)
        except:
            valor = 0
        canales[canal] = canales.get(canal, 0) + valor
    return canales

def empleado_mas_ventas(datos, indice_mesero=9, indice_total=8):
    empleados = {}
    for fila in datos[1:]:
        empleado = fila[indice_mesero].strip()
        total = float(re.sub(r"[^0-9.,-]", "", fila[indice_total]).replace(",", "."))
        empleados[empleado] = empleados.get(empleado, 0) + total
    return max(empleados, key=empleados.get)

def empleado_con_mas_pedidos(datos, indice_mesero=9):
    empleados = {}
    for fila in datos[1:]:
        emp = fila[indice_mesero].strip()
        empleados[emp] = empleados.get(emp, 0) + 1
    return max(empleados, key=empleados.get)

def menu():
    archivo_limpio = "practicas_4/dataset6_restaurant_orders_limpio.csv"
    datos = leer_csv(archivo_limpio)

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Total de clientes")
        print("2. Ingresos totales")
        print("3. Plato más consumido")
        print("4. Pedidos por categoría")
        print("5. Ventas por canal")
        print("6. Empleado con más ventas")
        print("7. Empleado con más pedidos")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print(f"Total de clientes: {total_clientes(datos)}")

        elif opcion == "2":
            ingresos = ingresos_totales(datos)
            print(f"Ingresos totales: ${ingresos:,.2f}")

        elif opcion == "3":
            plato = plato_mas_consumido(datos)
            print(f"Plato más consumido: {plato}")

        elif opcion == "4":
            categorias = pedidos_por_categoria(datos)
            print("Pedidos por categoría:")
            for cat, cant in categorias.items():
                print(f" - {cat}: {cant} pedidos")

        elif opcion == "5":
            canales = ventas_por_canal(datos)
            print("Ventas por canal:")
            for canal, valor in canales.items():
                print(f" - {canal}: ${valor:,.2f}")

        elif opcion == "6":
            emp = empleado_mas_ventas(datos)
            print(f"Empleado con más ventas: {emp}")

        elif opcion == "7":
            emp = empleado_con_mas_pedidos(datos)
            print(f"Empleado con más pedidos atendidos: {emp}")

        elif opcion == "8":
            print("Saliendo del menú...")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()

