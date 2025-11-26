import csv

def leer_csv(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        reader = csv.reader(archivo)
        datos = list(reader)
    return datos

def total_clientes(datos):
    return len(datos) - 1

def ingresos_totales(datos):
    total = 0
    for fila in datos:
        for valor in fila:
            if valor.replace('.', '', 1).isdigit():
                total += float(valor)
                break
    return total


def plato_mas_consumido(datos):
    platos = {}
    for fila in datos[1:]:
        plato = fila[2]
        if plato in platos:
            platos[plato] += 1
        else:
            platos[plato] = 1
    plato_mas_consumido = max(platos, key=platos.get)
    return plato_mas_consumido

def total_domicilios(datos):
    total = 0
    for fila in datos[1:]:
        if fila[4] == "Domicilio":
            total += 1
    return total

def total_salon(datos):
    total = 0
    for fila in datos[1:]:
        if fila[4] == "Salon":
            total += 1
    return total

def total_para_llevar(datos):
    total = 0
    for fila in datos[1:]:
        if fila[4] == "Para llevar":
            total += 1
    return total

def menu():
    archivo_limpio = 'dataset6_restaurant_orders_limpio.csv'
    datos = leer_csv(archivo_limpio)

    while True:
        print("\nMenú de opciones:")
        print("1. Total de clientes")
        print("2. Ingresos totales")
        print("3. Plato más consumido")
        print("4. Total de domicilios")
        print("5. Total de salón")
        print("6. Total para llevar")
        print("7. Salir")
        opcion = input("Ingrese su opción: ")

        if opcion == "1":
            print(f"Total de clientes: {total_clientes(datos)}")
        elif opcion == "2":
            print(f"Ingresos totales: {ingresos_totales(datos)}")
        elif opcion == "3":
            print(f"Plato más consumido: {plato_mas_consumido(datos)}")
        elif opcion == "4":
            print(f"Total de domicilios: {total_domicilios(datos)}")
        elif opcion == "5":
            print(f"Total de salón: {total_salon(datos)}")
        elif opcion == "6":
            print(f"Total para llevar: {total_para_llevar(datos)}")
        elif opcion == "7":
            print("Adiós!")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    menu()