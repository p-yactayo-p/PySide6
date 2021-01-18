# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(400, 250)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(400, 250))
        MainWindow.setFocusPolicy(Qt.NoFocus)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.register_box = QGroupBox(self.centralwidget)
        self.register_box.setObjectName(u"register_box")
        sizePolicy.setHeightForWidth(self.register_box.sizePolicy().hasHeightForWidth())
        self.register_box.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(self.register_box)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.frame = QFrame(self.register_box)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setSpacing(5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(5, 5, 5, 5)
        self.e_nombre = QLineEdit(self.frame)
        self.e_nombre.setObjectName(u"e_nombre")
        self.e_nombre.setMaxLength(50)
        self.e_nombre.setClearButtonEnabled(True)

        self.gridLayout_3.addWidget(self.e_nombre, 0, 1, 1, 1)

        self.e_apellido = QLineEdit(self.frame)
        self.e_apellido.setObjectName(u"e_apellido")
        self.e_apellido.setMaxLength(50)
        self.e_apellido.setClearButtonEnabled(True)

        self.gridLayout_3.addWidget(self.e_apellido, 1, 1, 1, 1)

        self.e_direccion = QLineEdit(self.frame)
        self.e_direccion.setObjectName(u"e_direccion")
        self.e_direccion.setMaxLength(75)
        self.e_direccion.setClearButtonEnabled(True)

        self.gridLayout_3.addWidget(self.e_direccion, 2, 1, 1, 1)

        self.e_telefono = QLineEdit(self.frame)
        self.e_telefono.setObjectName(u"e_telefono")
        self.e_telefono.setMaxLength(15)
        self.e_telefono.setClearButtonEnabled(True)

        self.gridLayout_3.addWidget(self.e_telefono, 3, 1, 1, 1)

        self.s_edad = QSpinBox(self.frame)
        self.s_edad.setObjectName(u"s_edad")
        self.s_edad.setMinimum(17)
        self.s_edad.setMaximum(100)

        self.gridLayout_3.addWidget(self.s_edad, 4, 1, 1, 1)

        self.l_direccion = QLabel(self.frame)
        self.l_direccion.setObjectName(u"l_direccion")

        self.gridLayout_3.addWidget(self.l_direccion, 2, 0, 1, 1)

        self.l_nombre = QLabel(self.frame)
        self.l_nombre.setObjectName(u"l_nombre")

        self.gridLayout_3.addWidget(self.l_nombre, 0, 0, 1, 1)

        self.l_apellido = QLabel(self.frame)
        self.l_apellido.setObjectName(u"l_apellido")

        self.gridLayout_3.addWidget(self.l_apellido, 1, 0, 1, 1)

        self.l_edad = QLabel(self.frame)
        self.l_edad.setObjectName(u"l_edad")

        self.gridLayout_3.addWidget(self.l_edad, 4, 0, 1, 1)

        self.l_telefono = QLabel(self.frame)
        self.l_telefono.setObjectName(u"l_telefono")

        self.gridLayout_3.addWidget(self.l_telefono, 3, 0, 1, 1)

        self.pb_registrarse = QPushButton(self.frame)
        self.pb_registrarse.setObjectName(u"pb_registrarse")

        self.gridLayout_3.addWidget(self.pb_registrarse, 5, 1, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.register_box, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Registro de usuario", None))
        self.register_box.setTitle(QCoreApplication.translate("MainWindow", u"Formulario de registro", None))
        self.e_nombre.setText("")
        self.e_nombre.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese sus nombres", None))
        self.e_apellido.setText("")
        self.e_apellido.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese sus apellidos", None))
        self.e_direccion.setText("")
        self.e_direccion.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese su direcci\u00f3n", None))
        self.e_telefono.setText("")
        self.e_telefono.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese su tel\u00e9fono", None))
        self.s_edad.setSpecialValueText(QCoreApplication.translate("MainWindow", u"Ingrese su edad (mayores de 18 a\u00f1os)", None))
        self.l_direccion.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n", None))
        self.l_nombre.setText(QCoreApplication.translate("MainWindow", u"Nombres", None))
        self.l_apellido.setText(QCoreApplication.translate("MainWindow", u"Apellidos", None))
        self.l_edad.setText(QCoreApplication.translate("MainWindow", u"Edad", None))
        self.l_telefono.setText(QCoreApplication.translate("MainWindow", u"Tel\u00e9fono", None))
        self.pb_registrarse.setText(QCoreApplication.translate("MainWindow", u"Registrarse", None))
    # retranslateUi

