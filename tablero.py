def es_posicion_valida(fila, columna):
    return 0 <= fila < 8 and 0 <= columna < 8

def obtener_movimientos_validos(fila, columna, tablero):
    movimientos_validos = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
    movimientos = []

    for df, dc in movimientos_validos:
        nueva_fila = fila + df
        nueva_columna = columna + dc

        if es_posicion_valida(nueva_fila, nueva_columna) and tablero[nueva_fila][nueva_columna] == 0:
            movimientos.append((nueva_fila, nueva_columna))

    return movimientos

def obtenerInicial(fila, columna):
    if es_posicion_valida(fila, columna):
        tablero = [[0 for _ in range(8)] for _ in range(8)]
        tablero[fila][columna] = 1
        return tablero
    else:
        return "Coordenadas iniciales fuera de rango"

def recorrer_tablero(fila_inicial, columna_inicial):
    tablero = obtenerInicial(fila_inicial, columna_inicial)
    if isinstance(tablero, str):
        yield tablero
        return

    movimientos_totales = 8 * 8
    fila, columna = fila_inicial, columna_inicial

    # Inicializa la matriz para el recorrido
    recorrido = [[0 for _ in range(8)] for _ in range(8)]

    recorrido[fila][columna] = 1
    yield recorrido

    for _ in range(1, movimientos_totales):
        movimientos_validos = obtener_movimientos_validos(fila, columna, tablero)

        if not movimientos_validos:
            break

        # Encuentra el movimiento que lleva a una posición con menos movimientos válidos
        movimientos_validos.sort(key=lambda move: len(obtener_movimientos_validos(move[0], move[1], tablero)))

        siguiente_fila, siguiente_columna = movimientos_validos[0]
        tablero[siguiente_fila][siguiente_columna] = 1
        fila, columna = siguiente_fila, siguiente_columna

        # Actualiza la matriz de recorrido
        recorrido[fila][columna] = _ + 1  # Usamos _ + 1 para marcar el número de movimiento

        yield recorrido
#coordenadas inicales se pueden cambiar por otras 
fila_inicial = 0
columna_inicial = 1

recorrido_final = None  # Inicializa la matriz de recorrido final

for recorrido in recorrer_tablero(fila_inicial, columna_inicial):
    if isinstance(recorrido, str):
        print(recorrido)
    else:
        recorrido_final = recorrido  # Actualiza la matriz de recorrido final

# Imprime la matriz de recorrido final con el formato deseado
for fila in recorrido_final:
    for valor in fila:
        print(f"{valor:2d}", end="\t")
    print()
