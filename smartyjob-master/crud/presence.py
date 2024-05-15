from PyQt5 import QtCore, QtGui, QtWidgets
import frome,dashboard,chercher,database

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 600) 
        MainWindow.setStyleSheet("background-color:#fff;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.navbar = QtWidgets.QGraphicsView(self.centralwidget)
        self.navbar.setGeometry(QtCore.QRect(0, 0, 161, 591))
        self.navbar.setStyleSheet("border:none")
        self.navbar.setObjectName("navbar")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(-30, 100, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton.setFont(font)
        self.pushButton.setMouseTracking(False)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("border:none;\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: #2f89ff;\n"
"border-radius:20%;\n"
"font-size:15px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(-30, 180, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setMouseTracking(False)
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet("border:none;\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color:#2f89ff;\n"
"border-radius:20%;\n"
"font-size:15px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(-30, 270, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setMouseTracking(False)
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setStyleSheet("border:none;\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color:#2f89ff;\n"
"border-radius:20%;\n"
"font-size:15px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(200, 130, 701, 231))
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(-30, 360, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setMouseTracking(False)
        self.pushButton_4.setAutoFillBackground(False)
        self.pushButton_4.setStyleSheet("border:none;\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color:#2f89ff;\n"
"border-radius:20%;\n"
"font-size:15px;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(400, 40, 241, 41))
        self.dateEdit.setStyleSheet("")
        self.dateEdit.setObjectName("dateEdit")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(650, 40, 155, 41))
        self.pushButton_5.setStyleSheet("border:none; border-radius:8px;background-color:#99FFFF;color:#000;font-size:14px;font-weight:bold")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(400, 10, 241, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 925, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
         # Connect button click to function

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Liste Employées"))
        self.pushButton_2.setText(_translate("MainWindow", "Ajouter Employées"))
        self.pushButton_3.setText(_translate("MainWindow", "Checher Employe"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Code"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nom"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Prenom"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Departement"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Email"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Heures par jour"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Heures par mois"))
        self.pushButton_4.setText(_translate("MainWindow", "   Consulter la pésence"))
        self.pushButton_5.setText(_translate("MainWindow", "Consulter la pésence"))
        self.label.setText(_translate("MainWindow", "CONSULTER LA PRESENCE"))  # Set the title label text

    def chercher_par_date(self):
        selected_date = self.dateEdit.date().toString("yyyy-dd-MM")  
        print("Selected Date:", selected_date)  
        emp_present = database.get_presence_par_date(selected_date)
        self.tableWidget.setRowCount(0)
    
    # Populate the table with employees present
        row = 0
        for emp in emp_present:
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(emp[0])))  # ID
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(emp[1]))       # Nom
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(emp[2]))       # Prénom
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(emp[3]))       # Email
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(emp[5]))       # Département
            self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(database.get_worked_hours_today(emp[0])) )      # heure par jour
            self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(database.get_worked_hours_month(emp[0])))       # par mois
            row += 1

        
    def redirect_to_dashboard(self):
        self.dashboard_window = QtWidgets.QMainWindow()
        ui = dashboard.Ui_MainWindow()
        ui.setupUi(self.dashboard_window)
        self.dashboard_window.show()
       

    def redirect_to_chercher(self):
        self.chercher_window = QtWidgets.QMainWindow()
        ui = chercher.Ui_MainWindow()
        ui.setupUi(self.chercher_window)
        self.chercher_window.show()
       

    def redirect_to_frome(self):
        self.frome_window = QtWidgets.QMainWindow()
        ui = frome.Ui_MainWindow()
        ui.setupUi(self.frome_window)
        self.frome_window.show()
       

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.redirect_to_dashboard)
        self.pushButton_2.clicked.connect(self.redirect_to_frome)
        self.pushButton_3.clicked.connect(self.redirect_to_chercher)
        self.pushButton_5.clicked.connect(self.chercher_par_date) 
        self.pushButton_5.clicked.connect(self.chercher_par_date)
        

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())