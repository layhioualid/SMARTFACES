from PyQt5 import QtCore, QtGui, QtWidgets
from database import get_dep, insert_employee
import dashboard
import chercher
import presence


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
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(400, 0, 361, 51))
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(238, 110, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);\n"
                                  "font-size:14px")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(238, 160, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);\n"
                                  "font-size:14px")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(538, 110, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);\n"
                                  "font-size:14px")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(538, 160, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);\n"
                                  "font-size:14px")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(330, 110, 181, 24))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(620, 110, 221, 24))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(330, 160, 181, 24))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(620, 160, 221, 24))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(330, 210, 181, 24))
        self.comboBox.setObjectName("comboBox")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(238, 210, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);\n"
                                  "font-size:14px")
        self.label_5.setObjectName("label_5")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(630, 210, 211, 24))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(540, 210, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(0, 0, 0);\n"
                                  "font-size:14px")
        self.label_6.setObjectName("label_6")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(500, 290, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "border:none;\n"
                                        "background-color: rgb(52, 235, 225);")
        self.pushButton_6.setObjectName("pushButton_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 925, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.lineEdit.setStyleSheet("QLineEdit { border: 2px solid black; border-radius: 5px; }")
        self.lineEdit_2.setStyleSheet("QLineEdit { border: 2px solid black; border-radius: 5px; }")
        self.lineEdit_3.setStyleSheet("QLineEdit { border: 2px solid black; border-radius: 5px; }")
        self.lineEdit_4.setStyleSheet("QLineEdit { border: 2px solid black; border-radius: 5px; }")

        # Styling for "Parcourir" button
        self.pushButton_5.setStyleSheet("QPushButton { border: none; background-color: #2ecc71; color: white; border-radius: 5px; }")
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox.setStyleSheet("QComboBox { border: 2px solid black; border-radius: 5px; padding: 1px 18px 1px 3px; }"
                             "QComboBox::drop-down { subcontrol-origin: padding; subcontrol-position: top right; width: 20px; border-left-width: 1px; border-left-color: darkgray; border-left-style: solid; border-top-right-radius: 3px; border-bottom-right-radius: 3px; }"
                             "QComboBox::down-arrow { image: url(drop_down_icon.png); }"
                             "QComboBox::down-arrow:on { top: 1px; }"
                             "QComboBox QAbstractItemView { border: 2px solid black; selection-background-color: lightgray; }")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Liste Employées"))
        self.pushButton_2.setText(_translate("MainWindow", "Ajouter Employées"))
        self.pushButton_3.setText(_translate("MainWindow", "Checher Employe"))
        self.pushButton_4.setText(_translate("MainWindow", "    Consulter la pésence"))
        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "hr { height: 1px; border-width: 0; }\n"
                                            "li.unchecked::marker { content: \"\\2610\"; }\n"
                                            "li.checked::marker { content: \"\\2612\"; }\n"
                                            "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:700;\">Ajouter Employée</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Nom"))
        self.label_2.setText(_translate("MainWindow", "Email"))
        self.label_3.setText(_translate("MainWindow", "Prenom"))
        self.label_4.setText(_translate("MainWindow", "Poste"))
        self.label_5.setText(_translate("MainWindow", "Departement"))
        self.pushButton_5.setText(_translate("MainWindow", "parcourir"))
        self.label_6.setText(_translate("MainWindow", "Image"))
        self.pushButton_6.setText(_translate("MainWindow", "Ajouter"))

    def redirect_to_dashboard(self):
        
        self.dashboard_window = QtWidgets.QMainWindow()
        ui = dashboard.Ui_MainWindow()
        ui.setupUi(self.dashboard_window)
        self.dashboard_window.show()
        MainWindow.close()

    def redirect_to_chercher(self):
        
        # self.chercher_window = chercher.Ui_MainWindow()
        # self.chercher_window.show()
        # self.close()
        self.chercher_window = QtWidgets.QMainWindow()
        self.ui = chercher.Ui_MainWindow()
        self.ui.setupUi(self.chercher_window)
        self.ui.pushButton_5.clicked.connect(self.ui.search_employee)
        self.ui.pushButton.clicked.connect(self.ui.open_dashboard)
        
        self.chercher_window.show()
        MainWindow.close()

    def redirect_to_presence(self):
        self.presence_window = QtWidgets.QMainWindow()
        ui = presence.Ui_MainWindow()
        ui.setupUi(self.presence_window)
        self.presence_window.show()
        MainWindow.close()

    def populate_departments(self):
        try:
            departments = get_dep()
            for dep_id, dep_name in departments:
                # Concatenate department ID and department name
                dep_text = f"{dep_id}: {dep_name}"
                # Add the concatenated text to the combo box
                self.comboBox.addItem(dep_text)
        except Exception as e:
            print("Error occurred while populating departments:", e)

    def browse_file(self):
        self.file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Choisir une image", "",
                                                                   "Image Files (*.png *.jpg *.jpeg *.bmp)")
        if self.file_path:
            # Set the file path to some variable or display it somewhere
            print("Selected File:", self.file_path)

    def ajouter_employe(self):
        # Retrieve employee information
        nom = self.lineEdit.text()
        prenom = self.lineEdit_3.text()
        email = self.lineEdit_2.text()
        poste = self.lineEdit_4.text()
        departement_id = int(self.comboBox.currentText().split(':')[0])

        # Check if any input field is empty
        if nom == '' or prenom == '' or email == '' or poste == '':
            # If any field is empty, show error message
            msg_box = QtWidgets.QMessageBox()
            msg_box.setIcon(QtWidgets.QMessageBox.Warning)
            msg_box.setWindowTitle("Erreur")
            msg_box.setText("Tous les champs doivent être remplis.")
            msg_box.exec_()
            return

        # Check if a department is selected
        if departement_id == 0:
            # If no department is selected, show error message
            msg_box = QtWidgets.QMessageBox()
            msg_box.setIcon(QtWidgets.QMessageBox.Warning)
            msg_box.setWindowTitle("Erreur")
            msg_box.setText("Veuillez sélectionner un département.")
            msg_box.exec_()
            return

        # Check if a file is selected
        if not hasattr(self, 'file_path') or not self.file_path:
            # If no file is selected, show error message
            msg_box = QtWidgets.QMessageBox()
            msg_box.setIcon(QtWidgets.QMessageBox.Warning)
            msg_box.setWindowTitle("Erreur")
            msg_box.setText("Veuillez sélectionner une image.")
            msg_box.exec_()
            return

        # Read the image file as binary data
        with open(self.file_path, 'rb') as f:
            image_data = f.read()
        
        # Insert the employee record
        insert_employee(nom, prenom, email, poste, departement_id, image_data)

        # Clear input fields
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.comboBox.setCurrentIndex(0)  # Reset combo box to first item

        # Show success message
        msg_box = QtWidgets.QMessageBox()
        msg_box.setIcon(QtWidgets.QMessageBox.Information)
        msg_box.setWindowTitle("Succès")
        msg_box.setText("Employé ajouté avec succès.")
        msg_box.exec_()


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        
        self.pushButton_6.clicked.connect(self.ajouter_employe)
        self.pushButton_5.clicked.connect(self.browse_file)
        self.pushButton.clicked.connect(self.redirect_to_dashboard)
        self.pushButton_3.clicked.connect(self.redirect_to_chercher)
        self.pushButton_4.clicked.connect(self.redirect_to_presence)
        self.populate_departments()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
