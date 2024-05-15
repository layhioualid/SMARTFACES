from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMainWindow
import dashboard
from database import search_employee, get_worked_hours_today, get_worked_hours_month
import frome
import presence

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Chercher")
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
        self.tableWidget.setGeometry(QtCore.QRect(200, 130, 740, 231))

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
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(400, 40, 241, 41))
        self.lineEdit.setStyleSheet("border:1px solid black;border-radius:8px")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(700, 40, 71, 41))
        self.pushButton_5.setStyleSheet("border:none; border-radius:8px; background-color:#74eb34;font-size:15px; color:white")
        self.pushButton_5.setObjectName("pushButton_5")
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
        self.pushButton_5.clicked.connect(self.search_employee)
        self.pushButton.clicked.connect(self.open_dashboard)
        self.pushButton_2.clicked.connect(self.redirect_to_frome)  # Connect the button to the function
        self.pushButton_4.clicked.connect(self.redirect_to_presence)  # Connect the button to the function

    def open_dashboard(self):
        # Create an instance of the DashboardWindow and show it
        self.dashboard_window = QMainWindow()
        ui = dashboard.Ui_MainWindow()
        ui.setupUi(self.dashboard_window)
        self.dashboard_window.show()
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Liste Employées"))
        self.pushButton_2.setText(_translate("MainWindow", "Ajouter Employées"))
        self.pushButton_3.setText(_translate("MainWindow", "Checher Employe"))
        self.pushButton_4.setText(_translate("MainWindow", "Consulter la présence"))
        self.pushButton_5.setText(_translate("MainWindow", "Chercher"))
        self.tableWidget.setColumnCount(8)  # Increase column count to accommodate "Email" column
        self.tableWidget.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)  # Adjust "Email" column width
        self.tableWidget.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)  # Center-align all columns
        self.tableWidget.setColumnCount(8) 
        # Set the headers for the table
        headers = ["ID", "Nom", "Prenom", "Email", "Poste", "Departement", "Heures par jour", "Heures par mois"]
        for index, header in enumerate(headers):
            item = self.tableWidget.horizontalHeaderItem(index)
            if item is None:
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setHorizontalHeaderItem(index, item)
            item.setText(_translate("MainWindow", header))

    def search_employee(self):
        search_text = self.lineEdit.text()
        print("Search Text:", search_text)  # Print the search text to verify it's correctly obtained
        # Call the search_employee function from database.py with the search_text
        search_result = search_employee(search_text)
        print("Search Result:", search_result)  # Print the search result to verify if it's obtained
        # Clear existing rows from the table
        self.tableWidget.setRowCount(0)
        # Populate the table with the search result
        for row, employee in enumerate(search_result):
            self.tableWidget.insertRow(row)
            for col, value in enumerate(employee):
                item = QTableWidgetItem(str(value))
                self.tableWidget.setItem(row, col, item)
                if col == 0:  # Assuming ID is in the first column
                    hours_today = get_worked_hours_today(value)
                    hours_item = QTableWidgetItem(str(hours_today))
                    print(hours_today)
                    self.tableWidget.setItem(row, 6, hours_item)
                    heure_par_moi = get_worked_hours_month(value)
                    hi = QTableWidgetItem(str(heure_par_moi))
                    print(heure_par_moi)
                    self.tableWidget.setItem(row, 7, hi)

    def redirect_to_frome(self):
        # Method for opening the Ajouter Employe window
        self.frome_window = QMainWindow()
        ui = frome.Ui_MainWindow()
        ui.setupUi(self.frome_window)
        self.frome_window.show()

    def redirect_to_presence(self):
        # Method for opening the Consulter la présence window
        self.presence_window = QMainWindow()
        ui = presence.Ui_MainWindow()
        ui.setupUi(self.presence_window)
        self.presence_window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
