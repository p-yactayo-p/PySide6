def teclas(tecla, label, line):
    texto = label.text()
    if 37 <= tecla.key() <= 61: # Numbers
        label.setText(texto + tecla.text())
    elif tecla.key() == 16777219: # Delete
        label.setText(texto[:-1])
    elif tecla.key() == 16777223: # Delete All
        line.clear()
        label.setText("Calculadora")
    elif 16777220 <= tecla.key() <= 16777221: # Enter
        line.clear()
        try:
            line.insert(str(eval(texto)))
        except:
            line.insert("Math Error")
