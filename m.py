from leer import Leer_Archivo
from funciones import Gestion_menu, ingresos_totales, plato_mas_consumido, pedidos_por_categoria, ventas_por_canal, empleado_mas_ventas, empleado_con_mas_pedidos

datos = Leer_Archivo.menu()

while True:
    print("-- MENÚ PRINCIPAL ---")
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
        print(f"Total de clientes: {Gestion_menu.total_clientes(datos)}")

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
        print("Opción inválida. Intente otra vez.")
