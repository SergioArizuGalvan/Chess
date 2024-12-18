## TORRES

def check_movimiento(player, pos_inicio, pos_final, tablero):
    x_ini, y_ini = pos_inicio
    x_fin, y_fin = pos_final

    if (x_ini != x_fin) and (y_ini != y_fin):
        return "MOVIMIENTO NO VÁLIDO"
    
    # añadir a chess.py :::  (x_ini == x_fin) and (y_ini == y_fin): return "NO SE HA EFECTUADO NINGUN MOVIMINETO"
    # añadir a chess.py :::  comprobacion si en la casilla final hay una pieza del mismo color"

    if (x_ini == x_fin):
        
        for y in range ((y_ini+1), y_fin + 1):
            pieza_casilla = tablero[x_ini][y]
            if pieza_casilla != "." and y != y_fin:
                return "HAY PIEZAS POR EL CAMINO"

    elif (y_ini != y_fin):
        for x in range ((x_ini+1), x_fin + 1):
            pieza_casilla = tablero[x][y_ini]
            if pieza_casilla != "." and x != x_fin:
                return "HAY PIEZAS POR EL CAMINO"


