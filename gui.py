# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
"""
GUI made in PyQt designer and .ui file was made into .py
"""
from PyQt4 import QtCore, QtGui
import Card
import Algorithm
import card_img

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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1280, 720)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(1020, 600, 210, 80))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.listWidget = QtGui.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(1026, 120, 201, 421))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(110, 50, 911, 491))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri Light"))
        font.setPointSize(72)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri Light"))
        font.setPointSize(12)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(1030, 50, 191, 71))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Blackjack Counter", None))
        self.pushButton.setText(_translate("Dialog", "Refresh", None))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.label.setText(_translate("Dialog", "-3%", None))
        self.label.setStyleSheet('color: red')
        self.label_2.setText(_translate("Dialog", "Disadvantage: House always has edge in start", None))
        self.label_3.setText(_translate("Dialog", "Count", None))

    #update the list view with new counter
    def count_update(self, Dialog, r_count, counter):
        r_count = str(r_count)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = self.listWidget.item(counter)
        item.setText(_translate("Dialog", r_count, None))
        
        

    #update advantage percentage
    def percentage_update(self, Dialog, adv_percentage):
        adv_percentage = str(adv_percentage)
        self.label.setText(_translate("Dialog", adv_percentage + "%", None))

    #update text
    def text_update(self, Dialog, adv_percentage):
        if (adv_percentage == 0):   
            self.label_2.setText(_translate("Dialog", "No Advantage: Even Game", None))
            self.label.setStyleSheet('color: black')
        elif (adv_percentage > 0):
            self.label_2.setText(_translate("Dialog", "Advantage   : Player's Edge", None))
            self.label.setStyleSheet('color: green')
        elif (adv_percentage < 0):
            self.label_2.setText(_translate("Dialog", "Disadvantage: House's  Edge", None))
            self.label.setStyleSheet('color: reds')
        else:
            self.label_2.setText(_translate("Dialog", "Invalid Percentage", None))
        


if __name__ == "__main__":
    import sys
    stream_url = input("Enter stream url: ")
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    #create ui start
    ui.setupUi(Dialog)

    counter = 0
    r_count = 0
    adv_percentage = -3
    def on_click():
        global counter
        global r_count
        
        #getCard
        card_input = card_img.get_final_value(stream_url)
        #card_input = int (card_input)
        
        #Algorithms - get running count and advantage percentage
        card = Card.Card(card_input)
        r_count = Algorithm.get_r_count(card, r_count)

        print(r_count)
        
        adv_percentage = Algorithm.get_adv_percentage(r_count)

        print(adv_percentage)
        
        #Update GUI based on refresh button
        ui.count_update(Dialog, r_count, counter)
        counter += 1
        ui.percentage_update(Dialog, adv_percentage)
        ui.text_update(Dialog, adv_percentage)
        
    ui.pushButton.clicked.connect(on_click)
      
    Dialog.show()
    sys.exit(app.exec_())


