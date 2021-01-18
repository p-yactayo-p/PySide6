# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'juego.ui'
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
        Form.resize(235, 373)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(235)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(235, 373))
        Form.setMaximumSize(QSize(235, 373))
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pb_33 = QPushButton(self.frame_2)
        self.pb_33.setObjectName(u"pb_33")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pb_33.sizePolicy().hasHeightForWidth())
        self.pb_33.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.pb_33.setFont(font)
        self.pb_33.setFocusPolicy(Qt.NoFocus)
        self.pb_33.setFlat(True)

        self.gridLayout_2.addWidget(self.pb_33, 4, 4, 1, 1)

        self.pb_11 = QPushButton(self.frame_2)
        self.pb_11.setObjectName(u"pb_11")
        self.pb_11.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.pb_11.sizePolicy().hasHeightForWidth())
        self.pb_11.setSizePolicy(sizePolicy1)
        self.pb_11.setFont(font)
        self.pb_11.setFocusPolicy(Qt.NoFocus)
        self.pb_11.setIconSize(QSize(20, 20))
        self.pb_11.setCheckable(False)
        self.pb_11.setAutoDefault(False)
        self.pb_11.setFlat(True)

        self.gridLayout_2.addWidget(self.pb_11, 0, 0, 1, 1)

        self.pb_21 = QPushButton(self.frame_2)
        self.pb_21.setObjectName(u"pb_21")
        sizePolicy1.setHeightForWidth(self.pb_21.sizePolicy().hasHeightForWidth())
        self.pb_21.setSizePolicy(sizePolicy1)
        self.pb_21.setFont(font)
        self.pb_21.setFocusPolicy(Qt.NoFocus)
        self.pb_21.setFlat(True)

        self.gridLayout_2.addWidget(self.pb_21, 2, 0, 1, 1)

        self.pb_31 = QPushButton(self.frame_2)
        self.pb_31.setObjectName(u"pb_31")
        sizePolicy1.setHeightForWidth(self.pb_31.sizePolicy().hasHeightForWidth())
        self.pb_31.setSizePolicy(sizePolicy1)
        self.pb_31.setFont(font)
        self.pb_31.setFocusPolicy(Qt.NoFocus)
        self.pb_31.setFlat(True)

        self.gridLayout_2.addWidget(self.pb_31, 4, 0, 1, 1)

        self.pb_12 = QPushButton(self.frame_2)
        self.pb_12.setObjectName(u"pb_12")
        sizePolicy1.setHeightForWidth(self.pb_12.sizePolicy().hasHeightForWidth())
        self.pb_12.setSizePolicy(sizePolicy1)
        self.pb_12.setFont(font)
        self.pb_12.setFocusPolicy(Qt.NoFocus)
        self.pb_12.setFlat(True)

        self.gridLayout_2.addWidget(self.pb_12, 0, 2, 1, 1)

        self.pb_23 = QPushButton(self.frame_2)
        self.pb_23.setObjectName(u"pb_23")
        sizePolicy1.setHeightForWidth(self.pb_23.sizePolicy().hasHeightForWidth())
        self.pb_23.setSizePolicy(sizePolicy1)
        self.pb_23.setFont(font)
        self.pb_23.setFocusPolicy(Qt.NoFocus)
        self.pb_23.setFlat(True)

        self.gridLayout_2.addWidget(self.pb_23, 2, 4, 1, 1)

        self.pb_13 = QPushButton(self.frame_2)
        self.pb_13.setObjectName(u"pb_13")
        sizePolicy1.setHeightForWidth(self.pb_13.sizePolicy().hasHeightForWidth())
        self.pb_13.setSizePolicy(sizePolicy1)
        self.pb_13.setFont(font)
        self.pb_13.setFocusPolicy(Qt.NoFocus)
        self.pb_13.setFlat(True)

        self.gridLayout_2.addWidget(self.pb_13, 0, 4, 1, 1)

        self.pb_32 = QPushButton(self.frame_2)
        self.pb_32.setObjectName(u"pb_32")
        sizePolicy1.setHeightForWidth(self.pb_32.sizePolicy().hasHeightForWidth())
        self.pb_32.setSizePolicy(sizePolicy1)
        self.pb_32.setFont(font)
        self.pb_32.setFocusPolicy(Qt.NoFocus)
        self.pb_32.setFlat(True)

        self.gridLayout_2.addWidget(self.pb_32, 4, 2, 1, 1)

        self.line_4 = QFrame(self.frame_2)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShadow(QFrame.Plain)
        self.line_4.setLineWidth(5)
        self.line_4.setFrameShape(QFrame.HLine)

        self.gridLayout_2.addWidget(self.line_4, 3, 0, 1, 1)

        self.line_3 = QFrame(self.frame_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShadow(QFrame.Plain)
        self.line_3.setLineWidth(5)
        self.line_3.setFrameShape(QFrame.HLine)

        self.gridLayout_2.addWidget(self.line_3, 1, 4, 1, 1)

        self.line_2 = QFrame(self.frame_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShadow(QFrame.Plain)
        self.line_2.setLineWidth(5)
        self.line_2.setFrameShape(QFrame.HLine)

        self.gridLayout_2.addWidget(self.line_2, 1, 2, 1, 1)

        self.line = QFrame(self.frame_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(5)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QFrame.HLine)

        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 1)

        self.line_7 = QFrame(self.frame_2)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShadow(QFrame.Plain)
        self.line_7.setLineWidth(5)
        self.line_7.setFrameShape(QFrame.VLine)

        self.gridLayout_2.addWidget(self.line_7, 0, 1, 1, 1)

        self.line_5 = QFrame(self.frame_2)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShadow(QFrame.Plain)
        self.line_5.setLineWidth(5)
        self.line_5.setFrameShape(QFrame.HLine)

        self.gridLayout_2.addWidget(self.line_5, 3, 2, 1, 1)

        self.line_6 = QFrame(self.frame_2)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShadow(QFrame.Plain)
        self.line_6.setLineWidth(5)
        self.line_6.setFrameShape(QFrame.HLine)

        self.gridLayout_2.addWidget(self.line_6, 3, 4, 1, 1)

        self.pb_22 = QPushButton(self.frame_2)
        self.pb_22.setObjectName(u"pb_22")
        sizePolicy1.setHeightForWidth(self.pb_22.sizePolicy().hasHeightForWidth())
        self.pb_22.setSizePolicy(sizePolicy1)
        self.pb_22.setFont(font)
        self.pb_22.setFocusPolicy(Qt.NoFocus)
        self.pb_22.setFlat(True)

        self.gridLayout_2.addWidget(self.pb_22, 2, 2, 1, 1)

        self.line_8 = QFrame(self.frame_2)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShadow(QFrame.Plain)
        self.line_8.setLineWidth(5)
        self.line_8.setFrameShape(QFrame.VLine)

        self.gridLayout_2.addWidget(self.line_8, 2, 1, 1, 1)

        self.line_9 = QFrame(self.frame_2)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShadow(QFrame.Plain)
        self.line_9.setLineWidth(5)
        self.line_9.setFrameShape(QFrame.VLine)

        self.gridLayout_2.addWidget(self.line_9, 4, 1, 1, 1)

        self.line_10 = QFrame(self.frame_2)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShadow(QFrame.Plain)
        self.line_10.setLineWidth(5)
        self.line_10.setFrameShape(QFrame.VLine)

        self.gridLayout_2.addWidget(self.line_10, 0, 3, 1, 1)

        self.line_11 = QFrame(self.frame_2)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShadow(QFrame.Plain)
        self.line_11.setLineWidth(5)
        self.line_11.setFrameShape(QFrame.VLine)

        self.gridLayout_2.addWidget(self.line_11, 2, 3, 1, 1)

        self.line_12 = QFrame(self.frame_2)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShadow(QFrame.Plain)
        self.line_12.setLineWidth(5)
        self.line_12.setFrameShape(QFrame.VLine)

        self.gridLayout_2.addWidget(self.line_12, 4, 3, 1, 1)


        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.l_name = QLabel(self.frame)
        self.l_name.setObjectName(u"l_name")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.l_name.setFont(font1)
        self.l_name.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.l_name, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pb_reset = QPushButton(self.frame_3)
        self.pb_reset.setObjectName(u"pb_reset")
        self.pb_reset.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_3.addWidget(self.pb_reset, 1, 0, 1, 1)

        self.l_ganador = QLabel(self.frame_3)
        self.l_ganador.setObjectName(u"l_ganador")
        font2 = QFont()
        font2.setPointSize(9)
        font2.setBold(True)
        self.l_ganador.setFont(font2)
        self.l_ganador.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.l_ganador, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_3, 2, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Tres en raya", None))
        self.pb_33.setText("")
        self.pb_11.setText("")
        self.pb_21.setText("")
        self.pb_31.setText("")
        self.pb_12.setText("")
        self.pb_23.setText("")
        self.pb_13.setText("")
        self.pb_32.setText("")
        self.pb_22.setText("")
        self.l_name.setText(QCoreApplication.translate("Form", u"TRES EN RAYA", None))
        self.pb_reset.setText(QCoreApplication.translate("Form", u"Reiniciar juego", None))
        self.l_ganador.setText("")
    # retranslateUi
