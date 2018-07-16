# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'posclient.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_VisitorWindow(object):
    def setupUi(self, VisitorWindow):
        VisitorWindow.setObjectName(_fromUtf8("VisitorWindow"))
        VisitorWindow.resize(909, 717)
        VisitorWindow.setAutoFillBackground(False)
        VisitorWindow.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(VisitorWindow)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.lineEdit_2 = QtGui.QLineEdit(VisitorWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setStyleSheet(_fromUtf8("border:none;\n"
"background-color:rgb(0, 71, 102);\n"
"color: rgb(255, 255, 255);\n"
"font-size:24px;\n"
""))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout_5.addWidget(self.lineEdit_2)
        self.label = QtGui.QLabel(VisitorWindow)
        self.label.setStyleSheet(_fromUtf8("color: rgb(0, 71, 102);\n"
"font-size:16px;\n"
""))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_5.addWidget(self.label)
        self.label_2 = QtGui.QLabel(VisitorWindow)
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font-size:18px;\n"
"font-type: italic;\n"
"halign: right;"))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_5.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(VisitorWindow)
        self.label_3.setMinimumSize(QtCore.QSize(24, 24))
        self.label_3.setMaximumSize(QtCore.QSize(24, 24))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_5.addWidget(self.label_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.listOrder = QtGui.QListWidget(VisitorWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listOrder.sizePolicy().hasHeightForWidth())
        self.listOrder.setSizePolicy(sizePolicy)
        self.listOrder.setStyleSheet(_fromUtf8("QListWidget#listOrder{\n"
"    background-color:rgb(255,255,255);\n"
"}\n"
"\n"
"QListWidget#listOrder#OrderItem:selected{\n"
"    background-color:rgb(255, 0, 0);\n"
"}\n"
""))
        self.listOrder.setTabKeyNavigation(False)
        self.listOrder.setObjectName(_fromUtf8("listOrder"))
        self.verticalLayout_3.addWidget(self.listOrder)
        self.lineEdit = QtGui.QLineEdit(VisitorWindow)
        self.lineEdit.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(64)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(_fromUtf8("background-color:rgb(255, 255, 255);\n"
"color:rgb(0, 71, 102);"))
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout_3.addWidget(self.lineEdit)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setMargin(4)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.pbUp = QtGui.QPushButton(VisitorWindow)
        self.pbUp.setMinimumSize(QtCore.QSize(75, 75))
        self.pbUp.setMaximumSize(QtCore.QSize(75, 75))
        self.pbUp.setObjectName(_fromUtf8("pbUp"))
        self.horizontalLayout_4.addWidget(self.pbUp)
        self.pbDown = QtGui.QPushButton(VisitorWindow)
        self.pbDown.setMinimumSize(QtCore.QSize(75, 75))
        self.pbDown.setMaximumSize(QtCore.QSize(75, 75))
        self.pbDown.setObjectName(_fromUtf8("pbDown"))
        self.horizontalLayout_4.addWidget(self.pbDown)
        self.pbQty = QtGui.QPushButton(VisitorWindow)
        self.pbQty.setMinimumSize(QtCore.QSize(75, 75))
        self.pbQty.setMaximumSize(QtCore.QSize(75, 75))
        self.pbQty.setObjectName(_fromUtf8("pbQty"))
        self.horizontalLayout_4.addWidget(self.pbQty)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.gridLayout.setMargin(2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pbEight = QtGui.QPushButton(VisitorWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbEight.sizePolicy().hasHeightForWidth())
        self.pbEight.setSizePolicy(sizePolicy)
        self.pbEight.setMinimumSize(QtCore.QSize(75, 75))
        self.pbEight.setMaximumSize(QtCore.QSize(75, 75))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pbEight.setFont(font)
        self.pbEight.setStyleSheet(_fromUtf8("QPushButton#pbEight{\n"
"background-color: rgb(0, 71, 102); \n"
"border: 2px;\n"
"border-color: black;\n"
"color: white;\n"
"padding: 15px 32px;\n"
"text-align: center;\n"
"text-decoration: none;\n"
"display: inline-block;\n"
"font-size: 16px;\n"
"}\n"
"QPushButton#pbEight:pressed {\n"
"background-color: rgb(0, 140, 200); \n"
"}"))
        self.pbEight.setObjectName(_fromUtf8("pbEight"))
        self.gridLayout.addWidget(self.pbEight, 0, 1, 1, 1)
        self.pbDot = QtGui.QPushButton(VisitorWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbDot.sizePolicy().hasHeightForWidth())
        self.pbDot.setSizePolicy(sizePolicy)
        self.pbDot.setMinimumSize(QtCore.QSize(75, 75))
        self.pbDot.setMaximumSize(QtCore.QSize(75, 75))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pbDot.setFont(font)
        self.pbDot.setStyleSheet(_fromUtf8("QPushButton#pbDot{\n"
"background-color: rgb(0, 71, 102); \n"
"border: 2px;\n"
"border-color: black;\n"
"color: white;\n"
"padding: 15px 32px;\n"
"text-align: center;\n"
"text-decoration: none;\n"
"display: inline-block;\n"
"font-size: 16px;\n"
"}\n"
"QPushButton#pbDot:pressed {\n"
"background-color: rgb(0, 140, 200); \n"
"}"))
        self.pbDot.setObjectName(_fromUtf8("pbDot"))
        self.gridLayout.addWidget(self.pbDot, 3, 0, 1, 1)
        self.pbSix = QtGui.QPushButton(VisitorWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbSix.sizePolicy().hasHeightForWidth())
        self.pbSix.setSizePolicy(sizePolicy)
        self.pbSix.setMinimumSize(QtCore.QSize(75, 75))
        self.pbSix.setMaximumSize(QtCore.QSize(75, 75))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pbSix.setFont(font)
        self.pbSix.setStyleSheet(_fromUtf8("QPushButton#pbSix{\n"
"background-color: rgb(0, 71, 102); \n"
"border: 2px;\n"
"border-color: black;\n"
"color: white;\n"
"padding: 15px 32px;\n"
"text-align: center;\n"
"text-decoration: none;\n"
"display: inline-block;\n"
"font-size: 16px;\n"
"}\n"
"QPushButton#pbSix:pressed {\n"
"background-color: rgb(0, 140, 200); \n"
"}"))
        self.pbSix.setObjectName(_fromUtf8("pbSix"))
        self.gridLayout.addWidget(self.pbSix, 1, 2, 1, 1)
        self.pbTwo = QtGui.QPushButton(VisitorWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbTwo.sizePolicy().hasHeightForWidth())
        self.pbTwo.setSizePolicy(sizePolicy)
        self.pbTwo.setMinimumSize(QtCore.QSize(75, 75))
        self.pbTwo.setMaximumSize(QtCore.QSize(75, 75))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pbTwo.setFont(font)
        self.pbTwo.setStyleSheet(_fromUtf8("QPushButton#pbTwo{\n"
"background-color: rgb(0, 71, 102); \n"
"border: 2px;\n"
"border-color: black;\n"
"color: white;\n"
"padding: 15px 32px;\n"
"text-align: center;\n"
"text-decoration: none;\n"
"display: inline-block;\n"
"font-size: 16px;\n"
"}\n"
"QPushButton#pbTwo:pressed {\n"
"background-color: rgb(0, 140, 200); \n"
"}"))
        self.pbTwo.setObjectName(_fromUtf8("pbTwo"))
        self.gridLayout.addWidget(self.pbTwo, 2, 1, 1, 1)
        self.pbNine = QtGui.QPushButton(VisitorWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbNine.sizePolicy().hasHeightForWidth())
        self.pbNine.setSizePolicy(sizePolicy)
        self.pbNine.setMinimumSize(QtCore.QSize(75, 75))
        self.pbNine.setMaximumSize(QtCore.QSize(75, 75))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pbNine.setFont(font)
        self.pbNine.setStyleSheet(_fromUtf8("QPushButton#pbNine{\n"
"background-color: rgb(0, 71, 102); \n"
"border: 2px;\n"
"border-color: black;\n"
"color: white;\n"
"padding: 15px 32px;\n"
"text-align: center;\n"
"text-decoration: none;\n"
"display: inline-block;\n"
"font-size: 16px;\n"
"}\n"
"QPushButton#pbNine:pressed {\n"
"background-color: rgb(0, 140, 200); \n"
"}"))
        self.pbNine.setObjectName(_fromUtf8("pbNine"))
        self.gridLayout.addWidget(self.pbNine, 0, 2, 1, 1)
        self.pbZero = QtGui.QPushButton(VisitorWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbZero.sizePolicy().hasHeightForWidth())
        self.pbZero.setSizePolicy(sizePolicy)
        self.pbZero.setMinimumSize(QtCore.QSize(75, 75))
        self.pbZero.setMaximumSize(QtCore.QSize(75, 75))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pbZero.setFont(font)
        self.pbZero.setStyleSheet(_fromUtf8("QPushButton#pbZero{\n"
"background-color: rgb(0, 71, 102); \n"
"border: 2px;\n"
"border-color: black;\n"
"color: white;\n"
"padding: 15px 32px;\n"
"text-align: center;\n"
"text-decoration: none;\n"
"display: inline-block;\n"
"font-size: 16px;\n"
"}\n"
"QPushButton#pbZero:pressed {\n"
"background-color: rgb(0, 140, 200); \n"
"}"))
        self.pbZero.setObjectName(_fromUtf8("pbZero"))
        self.gridLayout.addWidget(self.pbZero, 3, 1, 1, 1)
        self.pbHundred = QtGui.QPushButton(VisitorWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbHundred.sizePolicy().hasHeightForWidth())
        self.pbHundred.setSizePolicy(sizePolicy)
        self.pbHundred.setMinimumSize(QtCore.QSize(75, 75))
        self.pbHundred.setMaximumSize(QtCore.QSize(75, 75))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pbHundred.setFont(font)
        self.pbHundred.setStyleSheet(_fromUtf8("QPushButton#pbHundred{\n"
"background-color: rgb(0, 71, 102); \n"
"border: 2px;\n"
"border-color: black;\n"
"color: white;\n"
"padding: 15px 32px;\n"
"text-align: center;\n"
"text-decoration: none;\n"
"display: inline-block;\n"
"font-size: 16px;\n"
"}\n"
"QPushButton#pbHundred:pressed {\n"
"background-color: rgb(0, 140, 200); \n"
"}"))
        self.pbHundred.setObjectName(_fromUtf8("pbHundred"))
        self.gridLayout.addWidget(self.pbHundred, 3, 2, 1, 1)
        self.pbOne = QtGui.QPushButton(VisitorWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbOne.sizePolicy().hasHeightForWidth())
        self.pbOne.setSizePolicy(sizePolicy)
        self.pbOne.setMinimumSize(QtCore.QSize(75, 75))
        self.pbOne.setMaximumSize(QtCore.QSize(75, 75))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pbOne.setFont(font)
        self.pbOne.setStyleSheet(_fromUtf8("QPushButton#pbOne{\n"
"background-color: rgb(0, 71, 102); \n"
"border: 2px;\n"
"border-color: black;\n"
"color: white;\n"
"padding: 15px 32px;\n"
"text-align: center;\n"
"text-decoration: none;\n"
"display: inline-block;\n"
"font-size: 16px;\n"
"}\n"
"QPushButton#pbOne:pressed {\n"
"background-color: rgb(0, 140, 200); \n"
"}"))
        self.pbOne.setObjectName(_fromUtf8("pbOne"))
        self.gridLayout.addWidget(self.pbOne, 2, 0, 1, 1)
        self.pbFour = QtGui.QPushButton(VisitorWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbFour.sizePolicy().hasHeightForWidth())
        self.pbFour.setSizePolicy(sizePolicy)
        self.pbFour.setMinimumSize(QtCore.QSize(75, 75))
        self.pbFour.setMaximumSize(QtCore.QSize(75, 75))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pbFour.setFont(font)
        self.pbFour.setStyleSheet(_fromUtf8("QPushButton#pbFour{\n"
"background-color: rgb(0, 71, 102); \n"
"border: 2px;\n"
"border-color: black;\n"
"color: white;\n"
"padding: 15px 32px;\n"
"text-align: center;\n"
"text-decoration: none;\n"
"display: inline-block;\n"
"font-size: 16px;\n"
"}\n"
"QPushButton#pbFour:pressed {\n"
"background-color: rgb(0, 140, 200); \n"
"}"))
        self.pbFour.setObjectName(_fromUtf8("pbFour"))
        self.gridLayout.addWidget(self.pbFour, 1, 0, 1, 1)
        self.pbThree = QtGui.QPushButton(VisitorWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbThree.sizePolicy().hasHeightForWidth())
        self.pbThree.setSizePolicy(sizePolicy)
        self.pbThree.setMinimumSize(QtCore.QSize(75, 75))
        self.pbThree.setMaximumSize(QtCore.QSize(75, 75))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pbThree.setFont(font)
        self.pbThree.setStyleSheet(_fromUtf8("QPushButton#pbThree{\n"
"background-color: rgb(0, 71, 102); \n"
"border: 2px;\n"
"border-color: black;\n"
"color: white;\n"
"padding: 15px 32px;\n"
"text-align: center;\n"
"text-decoration: none;\n"
"display: inline-block;\n"
"font-size: 16px;\n"
"}\n"
"QPushButton#pbThree:pressed {\n"
"background-color: rgb(0, 140, 200); \n"
"}"))
        self.pbThree.setObjectName(_fromUtf8("pbThree"))
        self.gridLayout.addWidget(self.pbThree, 2, 2, 1, 1)
        self.pbFive = QtGui.QPushButton(VisitorWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbFive.sizePolicy().hasHeightForWidth())
        self.pbFive.setSizePolicy(sizePolicy)
        self.pbFive.setMinimumSize(QtCore.QSize(75, 75))
        self.pbFive.setMaximumSize(QtCore.QSize(75, 75))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pbFive.setFont(font)
        self.pbFive.setStyleSheet(_fromUtf8("QPushButton#pbFive{\n"
"background-color: rgb(0, 71, 102); \n"
"border: 2px;\n"
"border-color: black;\n"
"color: white;\n"
"padding: 15px 32px;\n"
"text-align: center;\n"
"text-decoration: none;\n"
"display: inline-block;\n"
"font-size: 16px;\n"
"}\n"
"QPushButton#pbFive:pressed {\n"
"background-color: rgb(0, 140, 200); \n"
"}"))
        self.pbFive.setObjectName(_fromUtf8("pbFive"))
        self.gridLayout.addWidget(self.pbFive, 1, 1, 1, 1)
        self.pbSeven = QtGui.QPushButton(VisitorWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbSeven.sizePolicy().hasHeightForWidth())
        self.pbSeven.setSizePolicy(sizePolicy)
        self.pbSeven.setMinimumSize(QtCore.QSize(75, 75))
        self.pbSeven.setMaximumSize(QtCore.QSize(75, 75))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pbSeven.setFont(font)
        self.pbSeven.setStyleSheet(_fromUtf8("QPushButton#pbSeven{\n"
"background-color: rgb(0, 71, 102); \n"
"border: 2px;\n"
"border-color: black;\n"
"color: white;\n"
"padding: 15px 32px;\n"
"text-align: center;\n"
"text-decoration: none;\n"
"display: inline-block;\n"
"font-size: 16px;\n"
"}\n"
"QPushButton#pbSeven:pressed {\n"
"background-color: rgb(0, 140, 200); \n"
"border: 2px;\n"
"color: white;\n"
"padding: 15px 32px;\n"
"text-align: center;\n"
"text-decoration: none;\n"
"display: inline-block;\n"
"font-size: 16px;\n"
"}"))
        self.pbSeven.setFlat(True)
        self.pbSeven.setObjectName(_fromUtf8("pbSeven"))
        self.gridLayout.addWidget(self.pbSeven, 0, 0, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.pbEnter = QtGui.QPushButton(VisitorWindow)
        self.pbEnter.setMinimumSize(QtCore.QSize(0, 75))
        self.pbEnter.setMaximumSize(QtCore.QSize(16777215, 75))
        self.pbEnter.setStyleSheet(_fromUtf8("QPushButton#pbEnter{\n"
"background-color:rgb(79, 159, 0);\n"
"color:rgb(255,255,255);\n"
"border:none;\n"
"padding: 15px 32px;\n"
"text-align: center;\n"
"text-decoration: none;\n"
"display: inline-block;\n"
"font-size: 16px;\n"
"}\n"
""))
        self.pbEnter.setObjectName(_fromUtf8("pbEnter"))
        self.horizontalLayout_7.addWidget(self.pbEnter)
        self.pbCancel = QtGui.QPushButton(VisitorWindow)
        self.pbCancel.setMinimumSize(QtCore.QSize(0, 75))
        self.pbCancel.setMaximumSize(QtCore.QSize(16777215, 75))
        self.pbCancel.setStyleSheet(_fromUtf8("QPushButton#pbCancel{\n"
"background-color:rgb(198, 66, 0);\n"
"color:rgb(255,255,255);\n"
"border:none;\n"
"padding: 15px 32px;\n"
"text-align: center;\n"
"text-decoration: none;\n"
"display: inline-block;\n"
"font-size: 16px;\n"
"}\n"
""))
        self.pbCancel.setObjectName(_fromUtf8("pbCancel"))
        self.horizontalLayout_7.addWidget(self.pbCancel)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem1)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.pushButton_17 = QtGui.QPushButton(VisitorWindow)
        self.pushButton_17.setMinimumSize(QtCore.QSize(100, 75))
        self.pushButton_17.setMaximumSize(QtCore.QSize(100, 75))
        self.pushButton_17.setObjectName(_fromUtf8("pushButton_17"))
        self.gridLayout_2.addWidget(self.pushButton_17, 0, 0, 1, 1)
        self.pushButton_19 = QtGui.QPushButton(VisitorWindow)
        self.pushButton_19.setMinimumSize(QtCore.QSize(100, 75))
        self.pushButton_19.setMaximumSize(QtCore.QSize(100, 75))
        self.pushButton_19.setObjectName(_fromUtf8("pushButton_19"))
        self.gridLayout_2.addWidget(self.pushButton_19, 0, 1, 1, 1)
        self.pushButton_20 = QtGui.QPushButton(VisitorWindow)
        self.pushButton_20.setMinimumSize(QtCore.QSize(100, 75))
        self.pushButton_20.setMaximumSize(QtCore.QSize(100, 75))
        self.pushButton_20.setObjectName(_fromUtf8("pushButton_20"))
        self.gridLayout_2.addWidget(self.pushButton_20, 1, 1, 1, 1)
        self.pushButton_18 = QtGui.QPushButton(VisitorWindow)
        self.pushButton_18.setMinimumSize(QtCore.QSize(100, 75))
        self.pushButton_18.setMaximumSize(QtCore.QSize(100, 75))
        self.pushButton_18.setObjectName(_fromUtf8("pushButton_18"))
        self.gridLayout_2.addWidget(self.pushButton_18, 1, 0, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout_2)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setMargin(4)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.pushButton_5 = QtGui.QPushButton(VisitorWindow)
        self.pushButton_5.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.horizontalLayout_6.addWidget(self.pushButton_5)
        self.pushButton_4 = QtGui.QPushButton(VisitorWindow)
        self.pushButton_4.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout_6.addWidget(self.pushButton_4)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(VisitorWindow)
        QtCore.QMetaObject.connectSlotsByName(VisitorWindow)

    def retranslateUi(self, VisitorWindow):
        VisitorWindow.setWindowTitle(_translate("VisitorWindow", "Form", None))
        self.lineEdit_2.setPlaceholderText(_translate("VisitorWindow", "Barcode", None))
        self.label.setText(_translate("VisitorWindow", "01/01/2018 00:00:00", None))
        self.label_2.setText(_translate("VisitorWindow", "TextLabel", None))
        self.listOrder.setSortingEnabled(False)
        self.lineEdit.setPlaceholderText(_translate("VisitorWindow", "Total", None))
        self.pbUp.setText(_translate("VisitorWindow", "UP", None))
        self.pbDown.setText(_translate("VisitorWindow", "DOWN", None))
        self.pbQty.setText(_translate("VisitorWindow", "QTY", None))
        self.pbEight.setText(_translate("VisitorWindow", "8", None))
        self.pbDot.setText(_translate("VisitorWindow", ".", None))
        self.pbSix.setText(_translate("VisitorWindow", "6", None))
        self.pbTwo.setText(_translate("VisitorWindow", "2", None))
        self.pbNine.setText(_translate("VisitorWindow", "9", None))
        self.pbZero.setText(_translate("VisitorWindow", "0", None))
        self.pbHundred.setText(_translate("VisitorWindow", "00", None))
        self.pbOne.setText(_translate("VisitorWindow", "1", None))
        self.pbFour.setText(_translate("VisitorWindow", "4", None))
        self.pbThree.setText(_translate("VisitorWindow", "3", None))
        self.pbFive.setText(_translate("VisitorWindow", "5", None))
        self.pbSeven.setText(_translate("VisitorWindow", "7", None))
        self.pbEnter.setText(_translate("VisitorWindow", "Enter", None))
        self.pbCancel.setText(_translate("VisitorWindow", "Cancel", None))
        self.pushButton_17.setText(_translate("VisitorWindow", "PushButton", None))
        self.pushButton_19.setText(_translate("VisitorWindow", "PushButton", None))
        self.pushButton_20.setText(_translate("VisitorWindow", "PushButton", None))
        self.pushButton_18.setText(_translate("VisitorWindow", "PushButton", None))
        self.pushButton_5.setText(_translate("VisitorWindow", "PushButton", None))
        self.pushButton_4.setText(_translate("VisitorWindow", "PushButton", None))

