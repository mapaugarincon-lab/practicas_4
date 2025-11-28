import re 
class Gestion_menu:
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
