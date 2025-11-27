import csv
import unicodedata
import re

class ProcesarCSV:
    def __init__(self, ruta_entrada, ruta_salida):
        self.ruta_entrada = ruta_entrada
        self.ruta_salida = ruta_salida
        self.datos = []

    def quitar_tildes(self, texto):
        return ''.join(
            c for c in unicodedata.normalize('NFD', texto)
            if unicodedata.category(c) != 'Mn')

    def formatear_miles(self, valor):
        if not valor:
            return ""
        v = str(valor).strip()
        v = re.sub(r"[^0-9.,-]", "", v) 
        if "," in v and "." not in v:
            v = v.replace(",", ".")
        if "," in v and "." in v:
            v = v.replace(",", "")
        try:
            numero = float(v)
            return f"{numero:,.2f}"
        except:
            return valor
    def leer(self):
        with open(self.ruta_entrada, 'r', encoding='utf-8') as archivo:
            reader = csv.reader(archivo)
            self.datos = list(reader)
        return self.datos

    def limpiar(self):
        datos_limpios = []
        for fila in self.datos:
            nueva = []
            for celda in fila:
                if celda is None or celda.strip() == "" or celda == "None":
                    nueva.append("")
                else:
                    nueva.append(self.quitar_tildes(celda))
            datos_limpios.append(nueva)
        self.datos = datos_limpios
        return self.datos
    def guardar(self):
        with open(self.ruta_salida, 'w', newline='', encoding='utf-8') as archivo:
            writer = csv.writer(archivo)
            writer.writerows(self.datos)
    def imprimir(self):
        for fila in self.datos:
            print(",".join(fila))
def leer_csv(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        reader = csv.reader(archivo)
        datos = list(reader)
    return datos
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

