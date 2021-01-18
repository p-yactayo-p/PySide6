# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'primera_app.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from images import pyside6_source

class Ui_widget(object):
    def setupUi(self, widget):
        if not widget.objectName():
            widget.setObjectName(u"widget")
        widget.resize(400, 300)
        self.titulo = QLabel(widget)
        self.titulo.setObjectName(u"titulo")
        self.titulo.setGeometry(QRect(90, 40, 211, 16))
        font = QFont()
        font.setPointSize(12)
        self.titulo.setFont(font)
        self.contador = QLabel(widget)
        self.contador.setObjectName(u"contador")
        self.contador.setGeometry(QRect(170, 80, 55, 51))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.contador.setFont(font1)
        self.contador.setFrameShape(QFrame.Box)
        self.contador.setAlignment(Qt.AlignCenter)
        self.boton = QPushButton(widget)
        self.boton.setObjectName(u"boton")
        self.boton.setGeometry(QRect(150, 160, 93, 28))
        self.image = QLabel(widget)
        self.image.setObjectName(u"image")
        self.image.setGeometry(QRect(160, 210, 71, 71))
        self.image.setPixmap(QPixmap(u":/images/exit.png"))

        self.retranslateUi(widget)

        QMetaObject.connectSlotsByName(widget)
    # setupUi

    def retranslateUi(self, widget):
        widget.setWindowTitle(QCoreApplication.translate("widget", u"Contador de clicks", None))
        self.titulo.setText(QCoreApplication.translate("widget", u"CONTADOR DE CLICKS", None))
        self.contador.setText(QCoreApplication.translate("widget", u"0", None))
        self.boton.setText(QCoreApplication.translate("widget", u"Haz click aqui", None))
        self.image.setText("")
    # retranslateUi
