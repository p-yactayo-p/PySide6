cont = 1
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def winner(posicion, valor, label):
    global matriz
    exec("matriz" + posicion + " = " + valor)
    player = {"X": 1, "O": 2}
    if matriz[0][0] == matriz[0][1] == matriz[0][2]:
        label.setText("GANADOR: JUGADOR {}".format(player[str(matriz[0][0])]))
    elif matriz[1][0] == matriz[1][1] == matriz[1][2]:
        label.setText("GANADOR: JUGADOR {}".format(player[str(matriz[1][0])]))
    elif matriz[2][0] == matriz[2][1] == matriz[2][2]:
        label.setText("GANADOR: JUGADOR {}".format(player[str(matriz[2][0])]))
    elif matriz[0][0] == matriz[1][0] == matriz[2][0]:
        label.setText("GANADOR: JUGADOR {}".format(player[str(matriz[0][0])]))
    elif matriz[0][1] == matriz[1][1] == matriz[2][1]:
        label.setText("GANADOR: JUGADOR {}".format(player[str(matriz[0][1])]))
    elif matriz[0][2] == matriz[1][2] == matriz[2][2]:
        label.setText("GANADOR: JUGADOR {}".format(player[str(matriz[0][2])]))
    elif matriz[0][0] == matriz[1][1] == matriz[2][2]:
        label.setText("GANADOR: JUGADOR {}".format(player[str(matriz[0][0])]))
    elif matriz[0][2] == matriz[1][1] == matriz[2][0]:
        label.setText("GANADOR: JUGADOR {}".format(player[str(matriz[0][2])]))

def click_mouse(click, posicion, label):
    global cont, matriz
    if cont % 2 != 0 and click.text() == '':
        click.setText("X")
        winner(posicion, "'X'", label)
    elif cont % 2 == 0 and click.text() == '':
        click.setText("O")
        winner(posicion, "'O'", label)
    cont += 1

def reset_button(lista, label):
    global cont, matriz
    for button in lista:
        if button.text() == "X" or button.text() == "O":
            button.setText("")
    label.setText("")
    cont = 1
    matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
