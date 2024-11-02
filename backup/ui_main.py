# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadastro.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1174, 807)
        Form.setStyleSheet(u"background-color: rgb(40, 43, 51);\n")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_menu = QFrame(Form)
        self.left_menu.setObjectName(u"left_menu")
        self.left_menu.setMinimumSize(QSize(0, 0))
        self.left_menu.setMaximumSize(QSize(9, 16777215))
        self.left_menu.setStyleSheet(u"*{\n"
"border: none;\n"
"color:white;\n"
"background-color: rgb(33, 37, 43);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"Qlabel{\n"
"  color: withe;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    Height: 30px;	\n"
"    background-color: rgb(44, 49, 58);\n"
"    border-right: 1px solid black;\n"
"    transition: border-color 0.9s ease;\n"
"    border-right-color: rgb(114, 61, 135);\n"
"\n"
"}\n"
"\n"
"")
        self.left_menu.setFrameShape(QFrame.StyledPanel)
        self.verticalLayout_2 = QVBoxLayout(self.left_menu)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_5 = QFrame(self.left_menu)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(240, 0))
        self.frame_5.setMaximumSize(QSize(280, 16777215))
        self.frame_5.setStyleSheet(u"border-radius:0px;\n"
"background-color: rgb(44, 49, 58);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_5 = QPushButton(self.frame_5)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(30, 30))
        self.pushButton_5.setMaximumSize(QSize(33, 30))
        self.pushButton_5.setSizeIncrement(QSize(50, 0))
        self.pushButton_5.setBaseSize(QSize(50, 0))
        font = QFont()
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet(u"\n"
"\n"
"QPushButton:hover{\n"
"    Height: 30px;	\n"
"    background-color: rgb(44, 49, 58);\n"
"    border-left: 2px solid black;\n"
"    border-right: 3px solid black;\n"
"    border-bottom: 3px solid black;\n"
"    border-top:2px solid black;\n"
"    border-left-color: rgb(114, 61, 135);\n"
"    border-bottom-color: rgb(114, 61, 135);\n"
"    border-right-color: rgb(114, 61, 135);\n"
"    border-top-color: rgb(114, 61, 135);\n"
"   border-radius:15px;\n"
"}")
        icon = QIcon()
        icon.addFile(u"../Users/lucas/Downloads/perfil.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setIconSize(QSize(30, 30))
        self.pushButton_5.setAutoRepeatInterval(300)

        self.horizontalLayout_4.addWidget(self.pushButton_5)

        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4, 0, Qt.AlignRight)

        self.label_20 = QLabel(self.frame_5)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"color: rgb(192, 149, 251);\n"
"")

        self.horizontalLayout_4.addWidget(self.label_20)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.left_menu)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(280, 0))
        self.frame_6.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.verticalLayout_3 = QVBoxLayout(self.frame_6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_9 = QPushButton(self.frame_6)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setPointSize(9)
        self.pushButton_9.setFont(font1)
        self.pushButton_9.setStyleSheet(u"QPushButton{\n"
"border-radius:0px;\n"
"text-align: left;\n"
"}\n"
"QPushButton:hover{\n"
"    Height: 30px;	\n"
"    background-color: rgb(44, 49, 58);\n"
"    border-right: 2px solid black;\n"
"    transition: border-color 1.0s ease;\n"
"    border-right-color: rgb(114, 61, 135);\n"
"    \n"
"   \n"
"\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"icons/casa.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_9.setIcon(icon1)
        self.pushButton_9.setIconSize(QSize(20, 20))
        self.pushButton_9.setCheckable(False)
        self.pushButton_9.setAutoRepeat(False)

        self.verticalLayout_3.addWidget(self.pushButton_9)

        self.pushButton_8 = QPushButton(self.frame_6)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(0, 30))
        self.pushButton_8.setFont(font1)
        self.pushButton_8.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_8.setStyleSheet(u"QPushButton:hover{\n"
"    Height: 30px;	\n"
"    background-color: rgb(44, 49, 58);\n"
"    border-right: 2px solid black;\n"
"    transition: border-color 1.0s ease;\n"
"    border-right-color: rgb(114, 61, 135);\n"
"   \n"
"\n"
"}\n"
"QPushButton{\n"
"border-radius:0px;\n"
"text-align: left;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"icons/novo-documento.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_8.setIcon(icon2)
        self.pushButton_8.setIconSize(QSize(20, 20))

        self.verticalLayout_3.addWidget(self.pushButton_8)

        self.pushButton_7 = QPushButton(self.frame_6)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(0, 30))
        self.pushButton_7.setFont(font1)
        self.pushButton_7.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_7.setStyleSheet(u"QPushButton:hover{\n"
"    Height: 30px;	\n"
"    background-color: rgb(44, 49, 58);\n"
"    border-right: 2px solid black;\n"
"    transition: border-color 1.0s ease;\n"
"    border-right-color: rgb(114, 61, 135);\n"
"   \n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"border-radius:0px;\n"
"text-align: left;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"icons/sair (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_7.setIcon(icon3)
        self.pushButton_7.setIconSize(QSize(20, 20))

        self.verticalLayout_3.addWidget(self.pushButton_7)


        self.verticalLayout_2.addWidget(self.frame_6, 0, Qt.AlignLeft)

        self.frame_8 = QFrame(self.left_menu)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setMinimumSize(QSize(240, 0))
        self.frame_8.setMaximumSize(QSize(230, 16777215))
        self.frame_8.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_8)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_16 = QFrame(self.frame_8)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMaximumSize(QSize(16777215, 0))
        self.frame_16.setStyleSheet(u"background-color: rgb(44, 49, 58);")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(self.frame_16)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_6.addWidget(self.label_5)

        self.pushButton = QPushButton(self.frame_16)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(20, 20))
        self.pushButton.setStyleSheet(u"QPushButton:hover{\n"
"    Height: 30px;	\n"
"    background-color: rgb(44, 49, 58);\n"
"    border-left: 1px solid black;\n"
"    border-bottom: 1px solid black;\n"
"    border-top: 1px solid black;\n"
"    transition: border-color 0.9s ease;\n"
"    border-left-color: rgb(114, 61, 135);\n"
"    border-top-color: rgb(114, 61, 135);\n"
"    border-bottom-color: rgb(114, 61, 135);\n"
"}\n"
"QPushButton{\n"
"border-radius:10px;\n"
"}")

        self.horizontalLayout_6.addWidget(self.pushButton)

        self.pushButton_11 = QPushButton(self.frame_16)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(0, 20))
        self.pushButton_11.setStyleSheet(u"QPushButton:hover{\n"
"    Height: 30px;	\n"
"    background-color: rgb(44, 49, 58);\n"
"    border-left: 1px solid black;\n"
"    border-bottom: 1px solid black;\n"
"    border-top: 1px solid black;\n"
"    transition: border-color 0.9s ease;\n"
"    border-left-color: rgb(114, 61, 135);\n"
"    border-top-color: rgb(114, 61, 135);\n"
"    border-bottom-color: rgb(114, 61, 135);\n"
"}\n"
"QPushButton{\n"
"border-radius:10px;\n"
"}")

        self.horizontalLayout_6.addWidget(self.pushButton_11)


        self.verticalLayout_4.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_8)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.frame_17)


        self.verticalLayout_2.addWidget(self.frame_8)

        self.frame_7 = QFrame(self.left_menu)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 20))
        self.frame_7.setMaximumSize(QSize(16777215, 30))
        font2 = QFont()
        font2.setPointSize(6)
        self.frame_7.setFont(font2)
        self.frame_7.setStyleSheet(u"border-radius:0px;\n"
"background-color: rgb(44, 49, 58);")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_6 = QPushButton(self.frame_7)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(0, 30))
        self.pushButton_6.setStyleSheet(u"\n"
"*{text-align: left;\n"
" margin-bottom:17px;\n"
"border-radius:0px;\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u"../Users/lucas/OneDrive/\u00c1rea de Trabalho/PROJETO GESTAO/img/interface-do-usuario.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_6.setIcon(icon4)

        self.horizontalLayout_5.addWidget(self.pushButton_6)


        self.verticalLayout_2.addWidget(self.frame_7)


        self.horizontalLayout.addWidget(self.left_menu)

        self.frame_9 = QFrame(Form)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_9)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"*{\n"
"border-radius:10px;\n"
"border: none;\n"
"background-color: rgb(33, 37, 43);\n"
"}\n"
"\n"
"Qlabel{\n"
"  color: withe;\n"
"}\n"
"\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border-radius:none;\n"
"background-color: rgb(44, 49, 58);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_10 = QPushButton(self.frame)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(40, 30))
        self.pushButton_10.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_10.setStyleSheet(u"QPushButton:hover{\n"
"    background-color: rgb(44, 49, 58);\n"
"    border-left: 1px solid black;\n"
"    border-right: 1px solid black;\n"
"    border-top: 1px solid black;\n"
"    border-bottom: 1px solid black;\n"
"    border-left-color: rgb(114, 61, 135);\n"
"    border-bottom-color: rgb(114, 61, 135);\n"
"    border-right-color: rgb(114, 61, 135);\n"
" 	border-top-color: rgb(114, 61, 135);\n"
"   border-radius:10px;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"icons/menu-aberto.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_10.setIcon(icon5)

        self.horizontalLayout_2.addWidget(self.pushButton_10)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(192, 149, 251);\n"
"")

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"\n"
"QPushButton:hover {\n"
"    color: red;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"icons/minimizar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon6)

        self.horizontalLayout_2.addWidget(self.pushButton_2, 0, Qt.AlignRight)

        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon7 = QIcon()
        icon7.addFile(u"../Users/lucas/Downloads/maximizar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon7)

        self.horizontalLayout_2.addWidget(self.pushButton_3, 0, Qt.AlignRight)

        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon8 = QIcon()
        icon8.addFile(u"icons/botao-fechar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_4.setIcon(icon8)

        self.horizontalLayout_2.addWidget(self.pushButton_4, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.frame)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setStyleSheet(u"background-color: rgb(44, 49, 58);\n"
"border-radius:10px")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.paginas = QStackedWidget(self.frame_3)
        self.paginas.setObjectName(u"paginas")
        self.paginas.setStyleSheet(u"background-color: rgb(44, 49, 58);\n"
"")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.paginas.addWidget(self.home)
        self.cadastro = QWidget()
        self.cadastro.setObjectName(u"cadastro")
        self.verticalLayout_7 = QVBoxLayout(self.cadastro)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_10 = QFrame(self.cadastro)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(600, 0))
        self.frame_10.setMaximumSize(QSize(16777215, 16777215))
        self.frame_10.setStyleSheet(u" background-color: rgb(33, 37, 43);\n"
"border-radius:10px;\n"
"text-align:center;\n"
"margin-top:7px")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_13 = QLabel(self.frame_10)
        self.label_13.setObjectName(u"label_13")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Black"])
        font3.setPointSize(12)
        self.label_13.setFont(font3)
        self.label_13.setStyleSheet(u"text-align:center;\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_8.addWidget(self.label_13, 0, Qt.AlignHCenter)


        self.verticalLayout_7.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.cadastro)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy)
        self.frame_11.setStyleSheet(u"QLineEdit{\n"
"    border-radius:10px;\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"*{\n"
"   color:white;\n"
"   background-color: rgb(33, 37, 43);\n"
"   border-radius:10px;\n"
"}\n"
"")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_11)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_13 = QFrame(self.frame_11)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"QLineEdit:hover{\n"
"    Height: 30px;\n"
"    border-top: 1px solid black;	\n"
"    border-left: 1px solid black;\n"
"    border-right: 1px solid black;\n"
"    border-bottom: 1px solid black;\n"
"    transition: border-color 0.9s ease;\n"
"    border-left-color: rgb(114, 61, 135);\n"
"    border-bottom-color: rgb(114, 61, 135);\n"
"    border-right-color: rgb(114, 61, 135);\n"
"   border-top-color: rgb(114, 61, 135);\n"
"   \n"
"}\n"
"")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_14 = QLabel(self.frame_13)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_9.addWidget(self.label_14)

        self.lineEdit = QLineEdit(self.frame_13)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(60, 16777215))
        self.lineEdit.setStyleSheet(u"*{ color:black;}\n"
"    QLineEdit:hover{\n"
"    Height: 30px;\n"
"    border-top: 1px solid black;	\n"
"    border-left: 1px solid black;\n"
"    border-rigth: 1px solid black;\n"
"    border-bottom: 1px solid black;\n"
"    transition: border-color 0.9s ease;\n"
"    border-left-color: rgb(114, 61, 135);\n"
"    border-bottom-color: rgb(114, 61, 135);\n"
"    border-rigth-color: rgb(114, 61, 135);\n"
"   border-top-color: rgb(114, 61, 135);\n"
"   \n"
"}\n"
"")

        self.horizontalLayout_9.addWidget(self.lineEdit)

        self.label_15 = QLabel(self.frame_13)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_9.addWidget(self.label_15)

        self.lineEdit_2 = QLineEdit(self.frame_13)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"*{ color:black;}\n"
"    QLineEdit:hover{\n"
"    Height: 30px;\n"
"    border-top: 1px solid black;	\n"
"    border-left: 1px solid black;\n"
"    border-rigth: 1px solid black;\n"
"    border-bottom: 1px solid black;\n"
"    transition: border-color 0.9s ease;\n"
"    border-left-color: rgb(114, 61, 135);\n"
"    border-bottom-color: rgb(114, 61, 135);\n"
"    border-rigth-color: rgb(114, 61, 135);\n"
"   border-top-color: rgb(114, 61, 135);\n"
"   \n"
"}\n"
"")

        self.horizontalLayout_9.addWidget(self.lineEdit_2)

        self.label_16 = QLabel(self.frame_13)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_9.addWidget(self.label_16)

        self.lineEdit_3 = QLineEdit(self.frame_13)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMaximumSize(QSize(80, 16777215))
        self.lineEdit_3.setStyleSheet(u"QLineEdit{ color:black;}\n"
"QLineEdit:hover{\n"
"    Height: 30px;\n"
"    border-top: 1px solid black;	\n"
"    border-left: 1px solid black;\n"
"    border-right: 1px solid black;\n"
"    border-bottom: 1px solid black;\n"
"    transition: border-color 0.9s ease;\n"
"    border-left-color: rgb(114, 61, 135);\n"
"    border-bottom-color: rgb(114, 61, 135);\n"
"    border-right-color: rgb(114, 61, 135);\n"
"   border-top-color: rgb(114, 61, 135);\n"
"   \n"
"}\n"
"")

        self.horizontalLayout_9.addWidget(self.lineEdit_3)


        self.verticalLayout_9.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_11)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setStyleSheet(u"QLineEdit{ color:black;}\n"
"QLineEdit:hover{\n"
"    Height: 30px;\n"
"    border-top: 1px solid black;	\n"
"    border-left: 1px solid black;\n"
"    border-right: 1px solid black;\n"
"    border-bottom: 1px solid black;\n"
"    transition: border-color 0.9s ease;\n"
"    border-left-color: rgb(114, 61, 135);\n"
"    border-bottom-color: rgb(114, 61, 135);\n"
"    border-right-color: rgb(114, 61, 135);\n"
"   border-top-color: rgb(114, 61, 135);\n"
"   \n"
"}\n"
"")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_17 = QLabel(self.frame_14)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"QLineEdit:hover{\n"
"    Height: 30px;\n"
"    border-top: 1px solid black;	\n"
"    border-left: 1px solid black;\n"
"    border-rigth: 1px solid black;\n"
"    border-bottom: 1px solid black;\n"
"    transition: border-color 0.9s ease;\n"
"    border-left-color: rgb(114, 61, 135);\n"
"    border-bottom-color: rgb(114, 61, 135);\n"
"    border-rigth-color: rgb(114, 61, 135);\n"
"   border-top-color: rgb(114, 61, 135);\n"
"   \n"
"}\n"
"")

        self.horizontalLayout_10.addWidget(self.label_17)

        self.lineEdit_4 = QLineEdit(self.frame_14)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(50, 0))
        self.lineEdit_4.setStyleSheet(u"QLineEdit:hover{\n"
"    Height: 30px;\n"
"    border-top: 1px solid black;	\n"
"    border-left: 1px solid black;\n"
"    border-right: 1px solid black;\n"
"    border-bottom: 1px solid black;\n"
"    transition: border-color 0.9s ease;\n"
"    border-left-color: rgb(114, 61, 135);\n"
"    border-bottom-color: rgb(114, 61, 135);\n"
"    border-right-color: rgb(114, 61, 135);\n"
"   border-top-color: rgb(114, 61, 135);\n"
"   \n"
"}\n"
"")

        self.horizontalLayout_10.addWidget(self.lineEdit_4)

        self.label_18 = QLabel(self.frame_14)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_10.addWidget(self.label_18)

        self.lineEdit_5 = QLineEdit(self.frame_14)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(40, 0))
        self.lineEdit_5.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.lineEdit_5.setStyleSheet(u"QLineEdit:hover{\n"
"    Height: 30px;\n"
"    border-top: 1px solid black;	\n"
"    border-left: 1px solid black;\n"
"    border-right: 1px solid black;\n"
"    border-bottom: 1px solid black;\n"
"    transition: border-color 0.9s ease;\n"
"    border-left-color: rgb(114, 61, 135);\n"
"    border-bottom-color: rgb(114, 61, 135);\n"
"    border-right-color: rgb(114, 61, 135);\n"
"   border-top-color: rgb(114, 61, 135);\n"
"   \n"
"}\n"
"")

        self.horizontalLayout_10.addWidget(self.lineEdit_5)

        self.label_19 = QLabel(self.frame_14)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_10.addWidget(self.label_19)

        self.comboBox = QComboBox(self.frame_14)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(30, 0))
        self.comboBox.setMaximumSize(QSize(9000, 30))
        self.comboBox.setSizeIncrement(QSize(200, 0))
        font4 = QFont()
        font4.setPointSize(8)
        self.comboBox.setFont(font4)

        self.horizontalLayout_10.addWidget(self.comboBox)


        self.verticalLayout_9.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.frame_11)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy)
        self.frame_15.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.tableWidget = QTableWidget(self.frame_15)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"color: black;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:20px;\n"
"text-align:center;\n"
"\n"
"")

        self.horizontalLayout_11.addWidget(self.tableWidget)


        self.verticalLayout_9.addWidget(self.frame_15)


        self.verticalLayout_7.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.cadastro)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"*{\n"
"   color:white;\n"
"   background-color: rgb(33, 37, 43);\n"
"   border-radius:10px;\n"
"}\n"
"")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pushButton_13 = QPushButton(self.frame_12)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMinimumSize(QSize(0, 20))
        self.pushButton_13.setSizeIncrement(QSize(0, 0))
        self.pushButton_13.setFont(font4)
        self.pushButton_13.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_13.setStyleSheet(u"QPushButton:hover{\n"
"    Height: 30px;	\n"
"    background-color: rgb(44, 49, 58);\n"
"    border-left: 1px solid black;\n"
"    border-bottom: 1px solid black;\n"
"    transition: border-color 0.9s ease;\n"
"    border-left-color: rgb(114, 61, 135);\n"
"    border-bottom-color: rgb(114, 61, 135);\n"
"}")

        self.horizontalLayout_8.addWidget(self.pushButton_13)

        self.pushButton_14 = QPushButton(self.frame_12)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMinimumSize(QSize(0, 20))
        self.pushButton_14.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_14.setStyleSheet(u"QPushButton:hover{\n"
"    Height: 30px;	\n"
"    background-color: rgb(44, 49, 58);\n"
"    border-left: 1px solid black;\n"
"    border-bottom: 1px solid black;\n"
"    transition: border-color 0.9s ease;\n"
"    border-left-color: rgb(114, 61, 135);\n"
"    border-bottom-color: rgb(114, 61, 135);\n"
"}")

        self.horizontalLayout_8.addWidget(self.pushButton_14)

        self.pushButton_16 = QPushButton(self.frame_12)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setMinimumSize(QSize(0, 20))
        self.pushButton_16.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_16.setStyleSheet(u"QPushButton:hover{\n"
"    Height: 30px;	\n"
"    background-color: rgb(44, 49, 58);\n"
"    border-left: 1px solid black;\n"
"    border-bottom: 1px solid black;\n"
"    transition: border-color 0.9s ease;\n"
"    border-left-color: rgb(114, 61, 135);\n"
"    border-bottom-color: rgb(114, 61, 135);\n"
"}")

        self.horizontalLayout_8.addWidget(self.pushButton_16)


        self.verticalLayout_7.addWidget(self.frame_12)

        self.paginas.addWidget(self.cadastro)
        self.pesquisa_produtos = QWidget()
        self.pesquisa_produtos.setObjectName(u"pesquisa_produtos")
        self.paginas.addWidget(self.pesquisa_produtos)

        self.horizontalLayout_7.addWidget(self.paginas)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"border-radius:none;\n"
"background-color: rgb(44, 49, 58);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(192, 149, 251);\n"
"")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(192, 149, 251);\n"
"")

        self.horizontalLayout_3.addWidget(self.label_2, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.frame_4)


        self.horizontalLayout.addWidget(self.frame_2)


        self.retranslateUi(Form)

        self.paginas.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_5.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"Bem vindo", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"Lucas", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"Home", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"Novo", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"Sair", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Deseja sair?", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Sim", None))
        self.pushButton_11.setText(QCoreApplication.translate("Form", u"N\u00e3o", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"Configura\u00e7\u00f5es", None))
        self.pushButton_10.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"Theme Default color based on dark  mode", None))
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.label_13.setText(QCoreApplication.translate("Form", u"Cadastro de Produtos", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Cod:", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Descri\u00e7\u00e3o do Produto:", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Quantidade:", None))
        self.lineEdit_3.setText(QCoreApplication.translate("Form", u"", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"Pre\u00e7o de Compra", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"Pre\u00e7o de Venda", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"Fornecedor:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"Amaggi", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"Amazon", None))

        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Codigo", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Descri\u00e7ao", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Quantidade", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Fornecedor", None));
        self.pushButton_13.setText(QCoreApplication.translate("Form", u"Novo", None))
        self.pushButton_14.setText(QCoreApplication.translate("Form", u"Salvar", None))
        self.pushButton_16.setText(QCoreApplication.translate("Form", u"Cancelar", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"By: Lucas A. Anchieta", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"v1.0.0", None))
    # retranslateUi

