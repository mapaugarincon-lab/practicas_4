import csv

class ProcesarCSV:

    def __init__(self, ruta_entrada, ruta_salida):
        self.ruta_entrada = ruta_entrada
        self.ruta_salida = ruta_salida
        self.datos = []

    def quitar_tildes(self, texto):
        if not isinstance(texto, str):
            return ""
        reemplazos = {
            "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u",
            "Á": "A", "É": "E", "Í": "I", "Ó": "O", "Ú": "U",
            "ñ": "n", "Ñ": "N"
        }
        return ''.join(reemplazos.get(c, c) for c in texto)

    def leer(self):
        try:
            with open(self.ruta_entrada, 'r', encoding='utf-8') as archivo:
                reader = csv.reader(archivo)
                self.datos = list(reader)
            return self.datos
        except Exception as e:
            print(f"Error leyendo archivo: {e}")
            return []

    def limpiar(self):
        datos_limpios = []
        for fila in self.datos:
            nueva_fila = []
            for celda in fila:
                if celda in (None, "", "None"):
                    nueva_fila.append("")
                else:
                    nueva_fila.append(self.quitar_tildes(celda))
            datos_limpios.append(nueva_fila)
        self.datos = datos_limpios
        return datos_limpios

    def guardar(self):
        try:
            with open(self.ruta_salida, 'w', newline='', encoding='utf-8') as archivo:
                writer = csv.writer(archivo)
                writer.writerows(self.datos)
        except Exception as e:
            print(f"Error guardando archivo: {e}")

    def imprimir(self):
        for fila in self.datos:
            print(",".join(fila))


def main():
    archivo_original = "practicas_4/dataset6_restaurant_orders (3).csv"
    archivo_limpio = "practicas_4/dataset6_restaurant_orders_limpio.csv"

    procesador = ProcesarCSV(archivo_original, archivo_limpio)

    procesador.leer()
    procesador.limpiar()
    procesador.guardar()

    print(f"Archivo limpio guardado como: {archivo_limpio}\n")
    procesador.imprimir()


if __name__ == "__main__":
    main()
