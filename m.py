
def total_clientes(datos):
    return len(datos) - 1 if len(datos) > 0 else 0
def ingresos_totales(datos, indice_valor=None):
    total = 0.0

    if not datos or len(datos) < 2:
        return total
    encabezado = datos[0]
    if indice_valor is not None and 0 <= indice_valor < len(encabezado):
        for fila in datos[1:]:
            try:
                celda = fila[indice_valor].strip()
                celda_limpia = re.sub(r"[^0-9.,-]", "", celda)
                if celda_limpia:
                    if "," in celda_limpia and "." not in celda_limpia:
                        celda_limpia = celda_limpia.replace(",", ".")
                    valor = float(celda_limpia)
                    total += valor
            except (ValueError, IndexError):
                continue
    else:

        for fila in datos[1:]:
            for celda in fila:
                celda = celda.strip()
                celda_limpia = re.sub(r"[^0-9.,-]", "", celda)
                if not celda_limpia:
                    continue
                if "," in celda_limpia and "." not in celda_limpia:
                    celda_limpia = celda_limpia.replace(",", ".")
                try:
                    valor = float(celda_limpia)
                    total += valor
                    break 
                except ValueError:
                    continue
    return total
def plato_mas_consumido(datos, indice_plato=2):
  
    if not datos or len(datos) < 2:
        return None, 0

    contador = {}
    for fila in datos[1:]:
        if len(fila) <= indice_plato:
            continue
        plato = fila[indice_plato].strip()
        if not plato:
            continue
        contador[plato] = contador.get(plato, 0) + 1

    if not contador:
        return None, 0

    plato_top = max(contador, key=contador.get)
    return plato_top, contador[plato_top]

def menu():
    archivo_limpio = r'C:\Users\Aprendiz\Music\maria\27\dataset6_restaurant_orders_limpio.csv'
    datos = leer_csv(archivo_limpio)

    while True:
        print("\nMenú de opciones:")
        print("1. Total de clientes")
        print("2. Ingresos totales")
        print("3. Plato más consumido")
        print("4. Salir")
        opcion = input("Ingrese su opción: ")

        if opcion == "1":
            print(f"Total de clientes: {total_clientes(datos)}")
        elif opcion == "2":
            ingresos = ingresos_totales(datos)
            print(f"Ingresos totales: {ingresos:,.2f}")
        elif opcion == "3":
            nombre_plato, cantidad = plato_mas_consumido(datos, indice_plato=2)
            if nombre_plato:
                print(f"Plato más consumido: '{nombre_plato}' — {cantidad} pedidos")
            else:
                print("No se encontró ningún plato consumido.")
        elif opcion == "4":
            print("saliendo...")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    menu()

