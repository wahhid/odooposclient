# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'orderitem.ui'
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

class Ui_OrderItem(object):
    def setupUi(self, OrderItem):
        OrderItem.setObjectName(_fromUtf8("OrderItem"))
        OrderItem.resize(738, 120)
        OrderItem.setAutoFillBackground(False)
        OrderItem.setStyleSheet(_fromUtf8("QWidget#OrderItem{\n"
"    background-color: rgb(0, 71, 102); \n"
"    color:rgb(255,255,255);\n"
"    border-size:2px;\n"
"    border-color:black;\n"
"}\n"
"\n"
"QWidget#OrderItem:hover{\n"
"    background-color: rgb(0, 140, 200);\n"
"}"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(OrderItem)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lblProduct = QtGui.QLabel(OrderItem)
        self.lblProduct.setMinimumSize(QtCore.QSize(100, 100))
        self.lblProduct.setMaximumSize(QtCore.QSize(100, 100))
        self.lblProduct.setAlignment(QtCore.Qt.AlignCenter)
        self.lblProduct.setObjectName(_fromUtf8("lblProduct"))
        self.horizontalLayout.addWidget(self.lblProduct)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lblProductName = QtGui.QLabel(OrderItem)
        self.lblProductName.setObjectName(_fromUtf8("lblProductName"))
        self.verticalLayout.addWidget(self.lblProductName)
        self.lblQuantity = QtGui.QLabel(OrderItem)
        self.lblQuantity.setObjectName(_fromUtf8("lblQuantity"))
        self.verticalLayout.addWidget(self.lblQuantity)
        self.lblPrice = QtGui.QLabel(OrderItem)
        self.lblPrice.setObjectName(_fromUtf8("lblPrice"))
        self.verticalLayout.addWidget(self.lblPrice)
        self.lblDiscount = QtGui.QLabel(OrderItem)
        self.lblDiscount.setObjectName(_fromUtf8("lblDiscount"))
        self.verticalLayout.addWidget(self.lblDiscount)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(OrderItem)
        QtCore.QMetaObject.connectSlotsByName(OrderItem)

    def retranslateUi(self, OrderItem):
        OrderItem.setWindowTitle(_translate("OrderItem", "Form", None))
        self.lblProduct.setText(_translate("OrderItem", "Product Image", None))
        self.lblProductName.setText(_translate("OrderItem", "Product Name", None))
        self.lblQuantity.setText(_translate("OrderItem", "Qty : 0 Pcs", None))
        self.lblPrice.setText(_translate("OrderItem", "Price : Rp", None))
        self.lblDiscount.setText(_translate("OrderItem", "Discount : Rp", None))

