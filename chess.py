def tablero_fun():
    tablero_ini=[
        ["t","c","a","q","k","a","c","t"],
        ["p","p","p","p","p","p","p","p"],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        ["P","P","P","P","P","P","P","P"],
        ["T","C","A","Q","K","A","C","T"]
        ]
    return tablero_ini


def printar_tablero(tablero):
    for columna in tablero:
        print(" ".join(columna))

printar_tablero(tablero_fun())



def turno(player):
    if player == "black":
        return "white"
    else:
        return "black"


def tus_piezas(player, pos_inicio, pos_final, tablero):
    x_ini, y_ini = pos_inicio
    x_fin, y_fin = pos_final
    pieza=tablero[x_ini][y_ini]

    if pieza == ".":
        return "NO HAY NINGUNA PIEZA"

    if (pieza.isupper() and player != "white") or (pieza.islowe() and player != "black"):
        return "NO ES TU TURNO"

    # DE MOMENTO TODO PERMITIDO, hay que programar los movimientos de cada pieza
    tablero[x_ini][y_ini]="."
    tablero[x_fin][y_fin]=pieza
    return "MOVIMIENTO EXITOSO"


def user_input(movimineto):
    inicio, final = movimiento.split()
    x_ini = ord(inicio[0]) - 97
    x_fin = ord(final[0]) - 97

    y_ini= int(inicio[1])
    y_fin= int(final[1])

    if (x_ini >=0 and x_ini <= 7 ) and (y_ini >=0 and y_ini <= 7 ) and (x_fin >=0 and x_fin <= 7 )and (y_fin >=0 and y_fin <= 7 ):
        return (x_ini,y_ini),(x_fin,y_fin)
    else:
        return "CORDENADAS NO VALIDAS"