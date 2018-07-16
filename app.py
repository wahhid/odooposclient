from PyQt4 import QtGui, QtCore

from libGUI.posclient import Ui_VisitorWindow
from libGUI.orderitem import Ui_OrderItem
import sys


class OrderItem(QtGui.QWidget, Ui_OrderItem):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_OrderItem()
        self.ui.setupUi(self)

class PosClient(QtGui.QWidget, Ui_VisitorWindow):

    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_VisitorWindow()
        self.ui.setupUi(self)
        self.ui.lineEdit.setInputMask("###.###,##")
        self.ui.pbOne.clicked.connect(self.on_click_numpad)
        self.ui.pbTwo.clicked.connect(self.on_click_numpad)
        self.ui.pbThree.clicked.connect(self.on_click_numpad)
        self.ui.pbFour.clicked.connect(self.on_click_numpad)
        self.ui.pbFive.clicked.connect(self.on_click_numpad)
        self.ui.pbSeven.clicked.connect(self.on_click_numpad)
        self.ui.pbEight.clicked.connect(self.on_click_numpad)
        self.ui.pbNine.clicked.connect(self.on_click_numpad)
        item01 = OrderItem()
        item02 = OrderItem()
        listwidgetitem01 = QtGui.QListWidgetItem(self.ui.listOrder)
        listwidgetitem01.setSizeHint(item01.sizeHint())
        self.ui.listOrder.addItem(listwidgetitem01)
        self.ui.listOrder.setItemWidget(listwidgetitem01,item01)

        listwidgetitem02 = QtGui.QListWidgetItem(self.ui.listOrder)
        listwidgetitem02.setSizeHint(item01.sizeHint())
        self.ui.listOrder.addItem(listwidgetitem02)
        self.ui.listOrder.setItemWidget(listwidgetitem02,item02)



    def on_click_numpad(self):
        self.ui.lineEdit_2.setText(self.ui.lineEdit_2.text() + self.sender().text())


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    app.setStyle(QtGui.QStyleFactory.create('Cleanlooks'))
    posclientui = PosClient()
    posclientui.show()
    sys.exit(app.exec_())

