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