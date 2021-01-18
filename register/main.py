from PySide6.QtWidgets import *
from designer.ps6_register import Ui_MainWindow
import eventos
import sys

class register_app(QMainWindow):
    def __init__(self):
        super(register_app, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.validate = None

        # ===================
        #       Eventos
        # ===================
        # ----- Mostrar info -----
        lista_entry = [self.ui.e_nombre, self.ui.e_apellido, self.ui.e_direccion, self.ui.e_telefono, self.ui.s_edad]
        self.ui.pb_registrarse.clicked.connect(lambda: eventos.mostrar(lista_entry))
        # ----- Validar info -----
        self.ui.e_nombre.textChanged.connect(lambda: eventos.validar_texto(self.ui.e_nombre))
        self.ui.e_apellido.textChanged.connect(lambda: eventos.validar_texto(self.ui.e_apellido))
        self.ui.e_direccion.textChanged.connect(lambda: eventos.validar_direccion(self.ui.e_direccion))
        self.ui.e_telefono.textChanged.connect(lambda: eventos.validar_numero(self.ui.e_telefono))
        self.ui.s_edad.textChanged.connect(lambda: eventos.validar_edad(self.ui.s_edad))
        # ----- Validar registro -----
        lista_validate = lista_entry + [self]
        self.ui.pb_registrarse.clicked.connect(lambda: eventos.validar_registro(lista_validate))
        self.ui.pb_registrarse.clicked.connect(self.alerta)

    def alerta(self):
        message_box = QMessageBox()
        message_box.setWindowTitle("Alerta")
        if self.resultado:
            message_box.setText("Usuario registrado con exito")
        else:
            message_box.setText("Verifica los campos")
        message_box.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_app = register_app()
    my_app.show()
    sys.exit(app.exec_())
