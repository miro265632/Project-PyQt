# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1049, 836)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.create = QtWidgets.QPushButton(self.centralwidget)
        self.create.setGeometry(QtCore.QRect(710, 170, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.create.setFont(font)
        self.create.setAutoDefault(True)
        self.create.setDefault(False)
        self.create.setObjectName("create")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 501, 801))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar.setGeometry(QtCore.QRect(520, 10, 21, 801))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(550, 10, 491, 141))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.dedline = QtWidgets.QDateEdit(self.formLayoutWidget)
        self.dedline.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2023, 11, 3), QtCore.QTime(0, 0, 0)))
        self.dedline.setObjectName("dedline")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.dedline)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.name_task = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.name_task.setObjectName("name_task")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.name_task)
        self.description = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.description.setObjectName("description")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.description)
        self.importance_box = QtWidgets.QComboBox(self.formLayoutWidget)
        self.importance_box.setMinimumContentsLength(0)
        self.importance_box.setObjectName("importance_box")
        self.importance_box.addItem("")
        self.importance_box.addItem("")
        self.importance_box.addItem("")
        self.importance_box.addItem("")
        self.importance_box.addItem("")
        self.importance_box.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.importance_box)
        self.aaaaa = QtWidgets.QPushButton(self.centralwidget)
        self.aaaaa.setGeometry(QtCore.QRect(580, 610, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.aaaaa.setFont(font)
        self.aaaaa.setObjectName("aaaaa")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(870, 670, 101, 101))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("belca.webp"))
        self.label_5.setObjectName("label_5")
        self.go_out = QtWidgets.QPushButton(self.centralwidget)
        self.go_out.setGeometry(QtCore.QRect(580, 700, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.go_out.setFont(font)
        self.go_out.setObjectName("go_out")
        self.update = QtWidgets.QPushButton(self.centralwidget)
        self.update.setGeometry(QtCore.QRect(710, 260, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.update.setFont(font)
        self.update.setObjectName("update")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.create.setText(_translate("MainWindow", "Добавить задачу"))
        self.label.setText(_translate("MainWindow", "Название задачи"))
        self.label_3.setText(_translate("MainWindow", "Сроки"))
        self.label_2.setText(_translate("MainWindow", "Описание задачи"))
        self.label_4.setText(_translate("MainWindow", "Выберите уровень \n"
"важности задачи (от 0 до 5)"))
        self.importance_box.setItemText(0, _translate("MainWindow", "0"))
        self.importance_box.setItemText(1, _translate("MainWindow", "1"))
        self.importance_box.setItemText(2, _translate("MainWindow", "2"))
        self.importance_box.setItemText(3, _translate("MainWindow", "3"))
        self.importance_box.setItemText(4, _translate("MainWindow", "4"))
        self.importance_box.setItemText(5, _translate("MainWindow", "5"))
        self.aaaaa.setText(_translate("MainWindow", "Загрузить в .csv"))
        self.go_out.setText(_translate("MainWindow", "Выйти"))
        self.update.setText(_translate("MainWindow", "Обновить список дел"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())