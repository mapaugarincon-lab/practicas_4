import csv

class Leer_Archivo:

    @staticmethod
    def leer_csv(nombre_archivo):
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            reader = csv.reader(archivo)
            datos = list(reader)
        return datos

    @staticmethod
    def menu():
        archivo_limpio = "practicas_4/dataset6_restaurant_orders_limpio.csv"
        datos = Leer_Archivo.leer_csv(archivo_limpio)
        return datos
