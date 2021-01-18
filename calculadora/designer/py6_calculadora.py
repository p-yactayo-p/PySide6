# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculadora.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(300, 425)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(300, 425))
        Form.setMaximumSize(QSize(300, 425))
        Form.setFocusPolicy(Qt.StrongFocus)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.f_botones = QFrame(Form)
        self.f_botones.setObjectName(u"f_botones")
        sizePolicy1 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.f_botones.sizePolicy().hasHeightForWidth())
        self.f_botones.setSizePolicy(sizePolicy1)
        self.f_botones.setFrameShape(QFrame.StyledPanel)
        self.f_botones.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.f_botones)
        self.gridLayout_3.setSpacing(5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(5, 5, 5, 5)
        self.btn_cierra = QPushButton(self.f_botones)
        self.btn_cierra.setObjectName(u"btn_cierra")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_cierra.sizePolicy().hasHeightForWidth())
        self.btn_cierra.setSizePolicy(sizePolicy2)
        self.btn_cierra.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_3.addWidget(self.btn_cierra, 0, 2, 1, 1)

        self.btn_C = QPushButton(self.f_botones)
        self.btn_C.setObjectName(u"btn_C")
        sizePolicy2.setHeightForWidth(self.btn_C.sizePolicy().hasHeightForWidth())
        self.btn_C.setSizePolicy(sizePolicy2)
        self.btn_C.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_3.addWidget(self.btn_C, 0, 0, 1, 1)

        self.btn_7 = QPushButton(self.f_botones)
        self.btn_7.setObjectName(u"btn_7")
        sizePolicy2.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy2)
        self.btn_7.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_3.addWidget(self.btn_7, 1, 0, 1, 1)

        self.btn_4 = QPushButton(self.f_botones)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy2.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy2)
        self.btn_4.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_3.addWidget(self.btn_4, 2, 0, 1, 1)

        self.btn_punto = QPushButton(self.f_botones)
        self.btn_punto.setObjectName(u"btn_punto")
        sizePolicy2.setHeightForWidth(self.btn_punto.sizePolicy().hasHeightForWidth())
        self.btn_punto.setSizePolicy(sizePolicy2)
        self.btn_punto.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_3.addWidget(self.btn_punto, 4, 0, 1, 1)

        self.btn_abre = QPushButton(self.f_botones)
        self.btn_abre.setObjectName(u"btn_abre")
        sizePolicy2.setHeightForWidth(self.btn_abre.sizePolicy().hasHeightForWidth())
        self.btn_abre.setSizePolicy(sizePolicy2)
        self.btn_abre.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_3.addWidget(self.btn_abre, 0, 1, 1, 1)

        self.btn_1 = QPushButton(self.f_botones)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy2.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy2)
        self.btn_1.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_3.addWidget(self.btn_1, 3, 0, 1, 1)

        self.btn_por = QPushButton(self.f_botones)
        self.btn_por.setObjectName(u"btn_por")
        sizePolicy2.setHeightForWidth(self.btn_por.sizePolicy().hasHeightForWidth())
        self.btn_por.setSizePolicy(sizePolicy2)
        self.btn_por.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_3.addWidget(self.btn_por, 0, 3, 1, 1)

        self.btn_8 = QPushButton(self.f_botones)
        self.btn_8.setObjectName(u"btn_8")
        sizePolicy2.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy2)
        self.btn_8.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_3.addWidget(self.btn_8, 1, 1, 1, 1)

        self.btn_5 = QPushButton(self.f_botones)
        self.btn_5.setObjectName(u"btn_5")
        sizePolicy2.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy2)
        self.btn_5.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_3.addWidget(self.btn_5, 2, 1, 1, 1)

        self.btn_2 = QPushButton(self.f_botones)
        self.btn_2.setObjectName(u"btn_2")
        sizePolicy2.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy2)
        self.btn_2.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_3.addWidget(self.btn_2, 3, 1, 1, 1)

        self.btn_0 = QPushButton(self.f_botones)
        self.btn_0.setObjectName(u"btn_0")
        sizePolicy2.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy2)
        self.btn_0.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_3.addWidget(self.btn_0, 4, 1, 1, 1)

        self.btn_9 = QPushButton(self.f_botones)
        self.btn_9.setObjectName(u"btn_9")
        sizePolicy2.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy2)
        self.btn_9.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_3.addWidget(self.btn_9, 1, 2, 1, 1)

        self.btn_6 = QPushButton(self.f_botones)
        self.btn_6.setObjectName(u"btn_6")
        sizePolicy2.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy2)
        self.btn_6.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_3.addWidget(self.btn_6, 2, 2, 1, 1)

        self.btn_3 = QPushButton(self.f_botones)
        self.btn_3.setObjectName(u"btn_3")
        sizePolicy2.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy2)
        self.btn_3.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_3.addWidget(self.btn_3, 3, 2, 1, 1)

        self.btn_porcentaje = QPushButton(self.f_botones)
        self.btn_porcentaje.setObjectName(u"btn_porcentaje")
        sizePolicy2.setHeightForWidth(self.btn_porcentaje.sizePolicy().hasHeightForWidth())
        self.btn_porcentaje.setSizePolicy(sizePolicy2)
        self.btn_porcentaje.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_3.addWidget(self.btn_porcentaje, 1, 3, 1, 1)

        self.btn_menos = QPushButton(self.f_botones)
        self.btn_menos.setObjectName(u"btn_menos")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_menos.sizePolicy().hasHeightForWidth())
        self.btn_menos.setSizePolicy(sizePolicy3)
        self.btn_menos.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_3.addWidget(self.btn_menos, 2, 3, 1, 1)

        self.btn_mas = QPushButton(self.f_botones)
        self.btn_mas.setObjectName(u"btn_mas")
        sizePolicy2.setHeightForWidth(self.btn_mas.sizePolicy().hasHeightForWidth())
        self.btn_mas.setSizePolicy(sizePolicy2)
        self.btn_mas.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_3.addWidget(self.btn_mas, 3, 3, 1, 1)

        self.btn_igual = QPushButton(self.f_botones)
        self.btn_igual.setObjectName(u"btn_igual")
        sizePolicy2.setHeightForWidth(self.btn_igual.sizePolicy().hasHeightForWidth())
        self.btn_igual.setSizePolicy(sizePolicy2)
        self.btn_igual.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_3.addWidget(self.btn_igual, 4, 2, 1, 2)


        self.gridLayout.addWidget(self.f_botones, 1, 0, 1, 1)

        self.f_visor = QFrame(Form)
        self.f_visor.setObjectName(u"f_visor")
        self.f_visor.setFrameShape(QFrame.StyledPanel)
        self.f_visor.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.f_visor)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(5)
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.le_entrada = QLineEdit(self.f_visor)
        self.le_entrada.setObjectName(u"le_entrada")
        font = QFont()
        font.setPointSize(12)
        self.le_entrada.setFont(font)
        self.le_entrada.setFocusPolicy(Qt.NoFocus)
        self.le_entrada.setLayoutDirection(Qt.LeftToRight)
        self.le_entrada.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.le_entrada, 1, 0, 1, 1)

        self.label = QLabel(self.f_visor)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.f_visor, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Calculadora", None))
        self.btn_cierra.setText(QCoreApplication.translate("Form", u")", None))
        self.btn_C.setText(QCoreApplication.translate("Form", u"C", None))
        self.btn_7.setText(QCoreApplication.translate("Form", u"7", None))
        self.btn_4.setText(QCoreApplication.translate("Form", u"4", None))
        self.btn_punto.setText(QCoreApplication.translate("Form", u".", None))
        self.btn_abre.setText(QCoreApplication.translate("Form", u"(", None))
        self.btn_1.setText(QCoreApplication.translate("Form", u"1", None))
        self.btn_por.setText(QCoreApplication.translate("Form", u"*", None))
        self.btn_8.setText(QCoreApplication.translate("Form", u"8", None))
        self.btn_5.setText(QCoreApplication.translate("Form", u"5", None))
        self.btn_2.setText(QCoreApplication.translate("Form", u"2", None))
        self.btn_0.setText(QCoreApplication.translate("Form", u"0", None))
        self.btn_9.setText(QCoreApplication.translate("Form", u"9", None))
        self.btn_6.setText(QCoreApplication.translate("Form", u"6", None))
        self.btn_3.setText(QCoreApplication.translate("Form", u"3", None))
        self.btn_porcentaje.setText(QCoreApplication.translate("Form", u"%", None))
        self.btn_menos.setText(QCoreApplication.translate("Form", u"-", None))
        self.btn_mas.setText(QCoreApplication.translate("Form", u"+", None))
        self.btn_igual.setText(QCoreApplication.translate("Form", u"=", None))
        self.label.setText(QCoreApplication.translate("Form", u"Calculadora", None))
    # retranslateUi

