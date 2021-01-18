from PySide6.QtWidgets import *
from designer.ps6_calculadora import Ui_Form
import sys, eventos

class calculadora_app(QDialog):
    def __init__(self):
        super(calculadora_app, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # ----- Boton clicked -----
        self.ui.btn_0.clicked.connect(lambda: self.boton_clicked("0"))
        self.ui.btn_1.clicked.connect(lambda: self.boton_clicked("1"))
        self.ui.btn_2.clicked.connect(lambda: self.boton_clicked("2"))
        self.ui.btn_3.clicked.connect(lambda: self.boton_clicked("3"))
        self.ui.btn_4.clicked.connect(lambda: self.boton_clicked("4"))
        self.ui.btn_5.clicked.connect(lambda: self.boton_clicked("5"))
        self.ui.btn_6.clicked.connect(lambda: self.boton_clicked("6"))
        self.ui.btn_7.clicked.connect(lambda: self.boton_clicked("7"))
        self.ui.btn_8.clicked.connect(lambda: self.boton_clicked("8"))
        self.ui.btn_9.clicked.connect(lambda: self.boton_clicked("9"))
        self.ui.btn_C.clicked.connect(lambda: self.boton_clicked("C"))
        self.ui.btn_abre.clicked.connect(lambda: self.boton_clicked("("))
        self.ui.btn_cierra.clicked.connect(lambda: self.boton_clicked(")"))
        self.ui.btn_igual.clicked.connect(lambda: self.boton_clicked("="))
        self.ui.btn_mas.clicked.connect(lambda: self.boton_clicked("+"))
        self.ui.btn_menos.clicked.connect(lambda: self.boton_clicked("-"))
        self.ui.btn_por.clicked.connect(lambda: self.boton_clicked("*"))
        self.ui.btn_porcentaje.clicked.connect(lambda: self.boton_clicked("%"))
        self.ui.btn_punto.clicked.connect(lambda: self.boton_clicked("."))

    # ===================
    # ----- Eventos -----
    # ===================

    # ----- Por teclado -----
    def keyPressEvent(self, event):
        if self.ui.label.text() == "Calculadora":
            self.ui.label.setText("")
        eventos.teclas(event, self.ui.label, self.ui.le_entrada)

    # ----- Por consola -----
    def boton_clicked(self, boton):
        if self.ui.label.text() == "Calculadora":
            self.ui.label.setText("")
        texto = self.ui.label.text()
        if boton != "C" and boton != "=":
            self.ui.label.setText(texto + boton)
        elif boton == "C":
            self.ui.label.setText("Calculadora")
            self.ui.le_entrada.clear()
        else:
            self.ui.le_entrada.clear()
            try:
                self.ui.le_entrada.insert(str(eval(texto)))
            except:
                self.ui.le_entrada.insert("Math Error")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_app = calculadora_app()
    my_app.show()
    sys.exit(app.exec_())
