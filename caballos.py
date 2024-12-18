## CABALLOS

def check_movimiento(player, pos_inicio, pos_final, tablero):
    x_ini, y_ini = pos_inicio
    x_fin, y_fin = pos_final

    if abs(x_ini - x_fin) != 2 and abs(y_ini - y_fin) != 1:
        return "MOVIMIENTO NO VALIDO, LOS CABALLOS HACEN 'L'"
    elif abs(x_ini - x_fin) != 1 and abs(y_ini - y_fin) != 2:
        return "MOVIMIENTO NO VALIDO, LOS CABALLOS HACEN 'L'"