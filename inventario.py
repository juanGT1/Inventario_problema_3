# Función para calcular la cantidad a pedir
def calcular_pedido(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0


# Matriz: [Código, Nombre, Stock Actual, Stock Mínimo]
articulos = [
    ["A001", "Televisor LG", 5, 10],
    ["A002", "PlayStation 5", 15, 10],
    ["A003", "teclado inalambrico", 3, 8],
    ["A004", "Mouse inalambrico", 7, 7],
    ["A005", "USB", 2, 12]
]

print("=== LISTA DE PEDIDOS ===")

# Recorrer la matriz
for articulo in articulos:
    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    cantidad_pedir = calcular_pedido(stock_actual, stock_minimo)

    print(f"{codigo}: {nombre} | Cantidad a pedir: {cantidad_pedir}")