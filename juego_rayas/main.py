from PySide6.QtWidgets import *
from designer.ps6_juego import Ui_Form
import sys, eventos

class rayas_game(QDialog):
    def __init__(self):
        super(rayas_game, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # ===================
        # ----- Botones -----
        # ===================
        # ----- Juego -----
        self.ui.pb_11.clicked.connect(lambda: self.press_mouse(self.ui.pb_11, "[0][0]"))
        self.ui.pb_12.clicked.connect(lambda: self.press_mouse(self.ui.pb_12, "[0][1]"))
        self.ui.pb_13.clicked.connect(lambda: self.press_mouse(self.ui.pb_13, "[0][2]"))
        self.ui.pb_21.clicked.connect(lambda: self.press_mouse(self.ui.pb_21, "[1][0]"))
        self.ui.pb_22.clicked.connect(lambda: self.press_mouse(self.ui.pb_22, "[1][1]"))
        self.ui.pb_23.clicked.connect(lambda: self.press_mouse(self.ui.pb_23, "[1][2]"))
        self.ui.pb_31.clicked.connect(lambda: self.press_mouse(self.ui.pb_31, "[2][0]"))
        self.ui.pb_32.clicked.connect(lambda: self.press_mouse(self.ui.pb_32, "[2][1]"))
        self.ui.pb_33.clicked.connect(lambda: self.press_mouse(self.ui.pb_33, "[2][2]"))
        # ----- Reiniciar -----
        self.ui.pb_reset.clicked.connect(lambda: self.reset_game())

    # ===================
    # ----- Eventos -----
    # ===================

    # ----- Click mouse -----
    def press_mouse(self, click, posicion):
        eventos.click_mouse(click, posicion, self.ui.l_ganador)

    # ------ Reiniciar juego -----
    def reset_game(self):
        eventos.reset_button([self.ui.pb_11, self.ui.pb_12, self.ui.pb_13,
                                self.ui.pb_21, self.ui.pb_22, self.ui.pb_23,
                                self.ui.pb_31, self.ui.pb_32, self.ui.pb_33], self.ui.l_ganador)

if __name__ == '__main__':
    app = QApplication()
    my_app = rayas_game()
    my_app.show()
    sys.exit(app.exec_())
