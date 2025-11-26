class Elemento:
    def __init__(self, ruta_csv):
        self.ruta_csv = ruta_csv
        self.lista = []
    
    def limpiar(self):
        limpio = []
        with open(self.ruta_csv, "r", encoding="utf-8") as f:
            lineas = f.read().strip().split("\n")

        for linea in lineas:
            campos = linea.split(",")
            campos_limpios = [campo.strip() for campo in campos]
            limpio.append(campos_limpios)

        self.lista = limpio
        return limpio

    def imprimir(self):
        for fila in self.lista:
            print(",".join(fila))

r = r"C:\Users\FORMACION\Documents\Practicas(jh)\practicas_4\dataset6_restaurant_orders.csv"

obj = Elemento(r)
obj.limpiar()
obj.imprimir()



