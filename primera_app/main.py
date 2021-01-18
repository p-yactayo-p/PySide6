from PySide6.QtWidgets import *
from pyside6_primera import Ui_widget
import sys

cont = 0

class primera_app(QDialog):
    def __init__(self):
        super(primera_app, self).__init__()
        self.primera_app = Ui_widget()
        self.primera_app.setupUi(self)
        self.primera_app.boton.clicked.connect(self.click)

    def click(self):
        global cont
        cont += 1
        self.primera_app.contador.setText((str(cont)))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_app = primera_app()
    my_app.show()
    sys.exit(app.exec_())
