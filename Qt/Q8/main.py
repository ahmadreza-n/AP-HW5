import sys
import os
import sqlite3
import requests

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap

connection = sqlite3.connect('database.db')


loginForm = uic.loadUiType(os.path.join(os.getcwd(), 'gui.ui'))[0]
registerForm = uic.loadUiType(os.path.join(os.getcwd(), 'form.ui'))[0]
mainFormm = uic.loadUiType(os.path.join(os.getcwd(), 'mainForm.ui'))[0]


class loginClass(loginForm, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.mainWindow = None
        self.loginButton.clicked.connect(self.login)
        self.registerButton.clicked.connect(self.register)

    def login(self):
        username = self.usernameBox.toPlainText()
        password = self.passwordBox.toPlainText()
        stmt = "SELECT name, phone, username, password FROM users WHERE username = (?) AND password = (?)"
        args = (username, password)
        result = connection.execute(stmt, args)
        for row in result:
            if row[2] == username and row[3] == password:
                self.mainWindow = mainClass(row)
                self.close()
                self.mainWindow.show()

    def register(self):
        self.registerWindow = registerClass()
        self.close()
        self.registerWindow.show()


class registerClass(registerForm, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.registerButton.clicked.connect(self.register)

    def register(self):
        name = self.nameBox.toPlainText()
        phone = self.phoneBox.toPlainText()
        username = self.usernameBox.toPlainText()
        password = self.passwordBox.toPlainText()
        stmt = "INSERT INTO users(name, phone, username, password) values (?, ?, ?, ?)"
        args = (name, phone, username, password)
        connection.execute(stmt, args)
        connection.commit()
        stmt = "SELECT name, phone, username, password FROM users WHERE username = (?) AND password = (?)"
        args = (username, password)
        result = connection.execute(stmt, args)
        for row in result:
            if row[2] == username and row[3] == password:
                self.mainWindow = mainClass(row)
                self.close()
                self.mainWindow.show()
                break


class mainClass(mainFormm, QMainWindow):
    def __init__(self, user):
        super().__init__()
        self.setupUi(self)
        self.user = user
        self.helloBox.setText(f"hello {self.user[0]}")
        pixmap = QPixmap('image.jpg')
        self.mapBox.setPixmap(pixmap)
        r = requests.get(r'https://map.ir/static?width=400&height=400&zoom_level=12&markers=color%3Aorigin%7Clabel%3A%D9%85%D9%BE%7C51.422174%2C35.732469')
        print(r.status_code)
        print(type(r))
        r.iter_content

app = QApplication(sys.argv)

loginWindow = loginClass()
loginWindow.show()

sys.exit(app.exec())
