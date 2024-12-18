## Alfiles

def check_movimiento(player, pos_inicio, pos_final, tablero):
    x_ini, y_ini = pos_inicio
    x_fin, y_fin = pos_final

    if abs(x_ini - x_fin) != abs(y_ini - y_fin):
        return "MOVIMIENTO NO VALIDO, LOS ALFILES SIGUEN LAS DIAGONALES"
    elif (x_ini - x_fin) > 0 and (y_ini - y_fin) > 0:
        print("++")
        for x in range ((x_ini+1), x_fin + 1):
            for y in range ((y_ini+1), y_fin + 1):
                pieza_casilla = tablero[x][y]
                if pieza_casilla != "." and y != y_fin:
                    return "HAY PIEZAS POR EL CAMINO"

    elif (x_ini - x_fin) < 0 and (y_ini - y_fin) < 0:
        print("--")
        for x in range ((x_ini-1), x_fin - 1):
            for y in range ((y_ini-1), y_fin - 1):
                pieza_casilla = tablero[x][y]
                if pieza_casilla != "." and y != y_fin:
                    return "HAY PIEZAS POR EL CAMINO"

    elif (x_ini - x_fin) > 0 and (y_ini - y_fin) < 0:
        print("+-")
        for x in range ((x_ini+1), x_fin + 1):
            for y in range ((y_ini-1), y_fin - 1):
                pieza_casilla = tablero[x][y]
                if pieza_casilla != "." and y != y_fin:
                    return "HAY PIEZAS POR EL CAMINO"

    elif (x_ini - x_fin) < 0 and (y_ini - y_fin) > 0:
        print("-+")
        for x in range ((x_ini-1), x_fin - 1):
            for y in range ((y_ini+1), y_fin + 1):
                pieza_casilla = tablero[x][y]
                if pieza_casilla != "." and y != y_fin:
                    return "HAY PIEZAS POR EL CAMINO"