from PyQt5 import QtCore, QtGui, QtWidgets
from database import get_employee_list, delete_employee_by_id
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QPixmap, QImage
import chercher
import frome
import presence

class EmployeeInfoWindow(QWidget):
    def __init__(self, employee_info):
        super().__init__()
        self.setWindowTitle("Employee Information")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        if isinstance(employee_info, tuple):  # Check if employee_info is a tuple
            employee_info = list(employee_info)  # Convert tuple to list

        if isinstance(employee_info, list):
            titre = ["id","Nom", "Prenom", "Email", "Poste", "Departement"]
            for i in range(len(titre)):
                text = QLabel(titre[i] + ": " + str(employee_info[i]))  # Convert to string
                text.setWordWrap(True)
                layout.addWidget(text)
            
            img_data = employee_info[-1].encode('utf-8')
            qimage = QImage.fromData(img_data, "JPG")
            pixmap = QtGui.QPixmap(qimage)
            image_label = QLabel()
            image_label.setPixmap(pixmap)
            layout.addWidget(image_label)

            btn_layout = QtWidgets.QHBoxLayout()
            btn_search = QtWidgets.QPushButton("Voir les projet", clicked=lambda: chercher.show())
            btn_layout.addWidget(btn_search)
            layout.addLayout(btn_layout)
        else:
            error_label = QLabel("Employee not found!")
            layout.addWidget(error_label)

        self.setLayout(layout)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Liste Employe")
        MainWindow.resize(1200, 600)  # Increase the width of the main window
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
        self.tableWidget.setGeometry(QtCore.QRect(270, 120, 800, 341))  # Increase the width of the table widget
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)  # Increase column count to 8
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
        self.tableWidget.setHorizontalHeaderItem(5, item)  # Add header for the Actions column
        item = QtWidgets.QTableWidgetItem()  # Add header for the "Consulter" column
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()  # Add header for the "Position" column
        self.tableWidget.setHorizontalHeaderItem(7, item)
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
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(410, 20, 211, 70))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(19)
        font.setBold(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet("color:#000;border:none;text-align:center")
        self.plainTextEdit.setObjectName("plainTextEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 21))  # Increase the width of the menu bar
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton_2.clicked.connect(lambda: self.redirect_to_forme(MainWindow))
        self.pushButton_4.clicked.connect(lambda: self.redirect_to_presence(MainWindow))
        self.pushButton_3.clicked.connect(lambda: self.open_chercher_employee(MainWindow))

        # Call the function to populate the table
        self.populate_employee_table()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Liste Employées"))
        self.pushButton_2.setText(_translate("MainWindow", "Ajouter Employées"))
        self.pushButton_3.setText(_translate("MainWindow", "Checher Employe"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nom"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Prenom"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Email"))  # Adjusted the header text to "Email"
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Position"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Departement"))  # Header text for the "Position" column
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Consulter"))  # Header text for the "Consulter" column
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Actions"))  # Header text for the Actions column
        self.pushButton_4.setText(_translate("MainWindow", "    Consulter la pésence"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "Liste Employées"))

    def populate_employee_table(self):
        employee_list = get_employee_list()
        self.tableWidget.setRowCount(len(employee_list))
        for row, employee in enumerate(employee_list):
            for col, value in enumerate(employee):
                item = QtWidgets.QTableWidgetItem(str(value))
                self.tableWidget.setItem(row, col, item)

            delete_button = QtWidgets.QPushButton("Delete")
            delete_button.setStyleSheet("background-color: red; color: white")  # Set button color to red
            delete_button.clicked.connect(lambda _, row=row: self.delete_employee(row))
            self.tableWidget.setCellWidget(row, 7, delete_button)

            view_button = QtWidgets.QPushButton("Consulter")
            view_button.setStyleSheet("background-color: green; color: white")  # Set button color to green
            view_button.clicked.connect(lambda _, row=row: self.view_employee(row))
            self.tableWidget.setCellWidget(row, 6, view_button)

    def delete_employee(self, row):
        id_item = self.tableWidget.item(row, 0)
        if id_item is not None:
            employee_id = id_item.text()
            # Call the delete function from database.py with the extracted ID
            delete_employee_by_id(employee_id)
            # Update the table after deletion
            self.populate_employee_table()

    def view_employee(self, row):
        employee_info = []
        image_col_index = 6  # Assuming the image column index is 6
        for col in range(self.tableWidget.columnCount()):
            item = self.tableWidget.item(row, col)
            if item:
                if col == image_col_index:
                    # If it's the image column, retrieve the image data
                    image_data = item.text()
                    employee_info.append(image_data)
                else:
                    employee_info.append(item.text())

        # Create a new EmployeeInfoWindow instance and pass employee_info
        self.employee_info_window = EmployeeInfoWindow(employee_info)
        self.employee_info_window.show()

    def open_chercher_employee(self, MainWindow):
    # Modified method for opening the Chercher Employee window
        self.chercher_window = QtWidgets.QMainWindow()
        self.ui = chercher.Ui_MainWindow()
        self.ui.setupUi(self.chercher_window)
        self.ui.pushButton_5.clicked.connect(self.ui.search_employee)
        self.ui.pushButton.clicked.connect(self.ui.open_dashboard)
        
        self.chercher_window.show()
        MainWindow.close()


    def redirect_to_forme(self, MainWindow):
    # Method for opening the Ajouter Employe window
        self.forme_window = QtWidgets.QMainWindow()
        self.ui = frome.MainWindow()
        self.ui.setupUi(self.forme_window)
        # self.ui.pushButton_5.clicked.connect(self)
        self.ui.pushButton_6.clicked.connect(self.ui.ajouter_employe)
        self.ui.pushButton_5.clicked.connect(self.ui.browse_file)
        self.ui.pushButton.clicked.connect(self.ui.redirect_to_dashboard)
        self.ui.pushButton_3.clicked.connect(self.ui.redirect_to_chercher)
        self.ui.pushButton_4.clicked.connect(self.ui.redirect_to_presence) # Connect to the presence redirect
        self.ui.populate_departments()
        self.forme_window.show()
        MainWindow.close()

    def redirect_to_presence(self, MainWindow):
    # Method for opening the Consulter la présence window
        self.presence_window = QtWidgets.QMainWindow()
        self.ui = presence.MainWindow()
        self.ui.setupUi(self.presence_window)
        self.ui.pushButton_5.clicked.connect(self.ui.chercher_par_date)  # Connect the signal to chercher_par_date
        self.ui.redirect_to_chercher()
        self.ui.redirect_to_dashboard()

        self.presence_window.show()
        MainWindow.close()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
