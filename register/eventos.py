control = [None for x in range(4)]

def mostrar(lista):
    for line in lista:
        objeto = str(line.objectName()[2:])
        print("{}: {}".format(objeto.capitalize(), line.text()))

def validar_texto(entry):
    if entry.text().isalpha() or " " in entry.text():
        entry.setStyleSheet("border: 1px solid green")
        control[0] = True
    else:
        entry.setStyleSheet("border: 1px solid red")
        control[0] = False

def validar_numero(entry):
    for i in entry.text():
        if i in "+-9876543210":
            entry.setStyleSheet("border: 1px solid green")
            control[1] = True
        else:
            entry.setStyleSheet("border: 1px solid red")
            control[1] = False

def validar_direccion(entry):
    if entry.text().isalnum() or " " in entry.text():
        entry.setStyleSheet("border: 1px solid green")
        control[2] = True
    else:
        entry.setStyleSheet("border: 1px solid red")
        control[2] = False

def validar_edad(entry):
    if entry.value() >= 18:
        entry.setStyleSheet("border: 1px solid green")
        control[3] = True
    else:
        entry.setStyleSheet("border: 1px solid red")
        control[3] = False

def validar_registro(lista):
    if control.count(True) == 4:
        lista[5].resultado = True
    else:
        lista[5].resultado = False
