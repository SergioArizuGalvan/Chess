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