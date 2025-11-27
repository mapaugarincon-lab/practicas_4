import csv
import unicodedata

def quitar_tildes(texto):
    return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')

def leer_csv(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        reader = csv.reader(archivo)
        datos = list(reader)
    return datos

def guardar_csv(nombre_archivo, datos):
    with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo:
        writer = csv.writer(archivo)
        writer.writerows(datos)

def main():
    archivo_original = 'dataset6_restaurant_orders.csv'
    archivo_limpio = 'dataset6_restaurant_orders_limpio.csv'

    datos = leer_csv(archivo_original)
    datos_limpios = [[quitar_tildes(celda) for celda in fila] for fila in datos]
    guardar_csv(archivo_limpio, datos_limpios)
    print(f"Archivo limpio guardado como: {archivo_limpio}")

if __name__ == "__main__":
    main()
