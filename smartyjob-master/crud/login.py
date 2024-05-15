from PyQt5 import QtCore, QtGui, QtWidgets
import dashboard
from database import check_login
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(787, 562)
        MainWindow.setStyleSheet("background-color:#fff")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 410, 91, 51))
        self.pushButton.setStyleSheet("QPushButton {\n"
                                       "    background-color: #000;\n"
                                       "    color: #fff;\n"
                                       "    font-size: 15px;\n"
                                       "    border: none;\n"
                                       "    border-radius: 8px;\n"
                                       "}\n"
                                       "QPushButton:hover {\n"
                                       "    background-color: #555;\n"
                                       "}\n"
                                       "")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(280, 200, 281, 31))
        self.lineEdit.setStyleSheet("border:1px solid #000;\n"
                                    "border-radius: 6px;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(280, 280, 281, 31))
        self.lineEdit_2.setStyleSheet("border:1px solid #000;\n"
                                      "border-radius: 6px;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 210, 91, 16))
        self.label.setStyleSheet("text-align: center;font-size:15px")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 280, 91, 16))
        self.label_2.setStyleSheet("text-align: center;font-size:15px")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 787, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect login button click event to function
        self.pushButton.clicked.connect(self.login_clicked)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "LOGIN"))
        self.label.setText(_translate("MainWindow", "Username"))
        self.label_2.setText(_translate("MainWindow", "PASSWORD"))

    def login_clicked(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        if not username or not password:
            error_message = "Please enter both username and password."
            QtWidgets.QMessageBox.warning(
                None, "Login Error", error_message, QtWidgets.QMessageBox.Ok
            )
        else:
            result = check_login(username, password)
            if result:
                print("Login successful!")
                self.show_dashboard()
                MainWindow.close() 
            else:
                error_message = "Incorrect email or password."
                QtWidgets.QMessageBox.warning(
                    None, "Login Error", error_message, QtWidgets.QMessageBox.Ok
                )
    def show_dashboard(self):
        self.dashboard_window = QtWidgets.QMainWindow()
        ui = dashboard.Ui_MainWindow()  # Use Ui_MainWindow instead of DashboardWindow
        ui.setupUi(self.dashboard_window)
        self.dashboard_window.show()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
