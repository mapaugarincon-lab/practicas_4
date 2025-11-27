class Limpiar_los_datos: 
    def limpiar_none(fila):
        for clave, valor in fila.items():
            if valor == "NA":
                fila[clave] = None
            return fila
