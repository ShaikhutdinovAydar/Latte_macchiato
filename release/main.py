import sys
import sqlite3
from PyQt5 import uic
from UI_files.main_ui import Ui_MainWindow_main
from UI_files.addEditCoffeeForm import Ui_MainWindow_add
from UI_files.addEditCoffeeForm_UPDATE import Ui_MainWindow_up
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class ADD(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui_add = Ui_MainWindow_add()
        self.ui_add.setupUi(self)
        self.ui_add.add_btn.clicked.connect(self.d)

    def d(self):
        con = sqlite3.connect("data/coffees.db")
        cur = con.cursor()
        cur.execute(
            f"INSERT INTO coffee(Name, degree_of_roasting, ground, taste, cost, volume)"
            f" VALUES('{self.ui_add.lineEdit.text()}', '{self.ui_add.lineEdit_2.text()}', '{self.ui_add.lineEdit_3.text()}',"
            f" '{self.ui_add.lineEdit_4.text()}', '{self.ui_add.lineEdit_5.text()}', '{self.ui_add.lineEdit_6.text()}')")
        con.commit()
        con.close()
        self.up = MyWidget()
        self.up.show()
        self.hide()


class UP(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow_up()
        self.ui.setupUi(self)
        self.ui.up_btn.clicked.connect(self.dd)

    def dd(self):
        con = sqlite3.connect("data/coffees.db")
        cur = con.cursor()
        if self.ui.lineEdit.text() != '':
            cur.execute(
                f"UPDATE coffee SET Name = '{self.ui.lineEdit.text()}' WHERE ID = {int(self.ui.lineEdit_7.text())}")
        if self.ui.lineEdit_2.text() != '':
            cur.execute(
                f"UPDATE coffee SET degree_of_roasting = '{self.ui.lineEdit_2.text()}'"
                f" WHERE ID = {int(self.ui.lineEdit_7.text())}")
        if self.ui.lineEdit_3.text() != '':
            cur.execute(
                f"UPDATE coffee SET ground = '{self.ui.lineEdit_3.text()}' WHERE ID = {int(self.ui.lineEdit_7.text())}")
        if self.ui.lineEdit_4.text() != '':
            cur.execute(
                f"UPDATE coffee SET taste = '{self.ui.lineEdit_4.text()}' WHERE ID = {int(self.ui.lineEdit_7.text())}")
        if self.ui.lineEdit_5.text() != '':
            cur.execute(
                f"UPDATE coffee SET cost = '{self.ui.lineEdit_5.text()}' WHERE ID = {int(self.ui.lineEdit_7.text())}")
        if self.ui.lineEdit_6.text() != '':
            cur.execute(
                f"UPDATE coffee SET volume = '{self.ui.lineEdit_6.text()}' WHERE ID = {int(self.ui.lineEdit_7.text())}")
        # cur.execute(f"UPDATE coffee SET Name = '{self.lineEdit.text()}',"
        #             f" degree_of_roasting = '{self.lineEdit_2.text()}',"
        #             f" ground = '{self.lineEdit_3.text()}', taste = '{self.lineEdit_4.text()}',"
        #             f" cost = '{self.lineEdit_5.text()}', volume = '{self.lineEdit_6.text()}'"
        #             f" WHERE ID = {int(self.lineEdit_7.text())}")
        con.commit()
        con.close()
        self.up = MyWidget()
        self.up.show()
        self.hide()


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        ui = Ui_MainWindow_main()
        ui.setupUi(self)
        # Подключение к БД
        con = sqlite3.connect("data/coffees.db")
        # Создание курсора
        cur = con.cursor()
        # Выполнение запроса и получение всех результатов
        self.result = cur.execute("SELECT * FROM coffee").fetchall()
        ui.tableWidget.setColumnCount(7)
        ui.tableWidget.setHorizontalHeaderLabels(
            ["id", "title", "degree of roasting", "ground in grains", "the description of the taste", "cost",
             "the amount of taste"])
        ui.tableWidget.setRowCount(0)
        for i, row in enumerate(self.result):
            ui.tableWidget.setRowCount(ui.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                ui.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))
        ui.tableWidget.resizeColumnsToContents()
        con.commit()
        con.close()
        ui.pushButton.clicked.connect(self.ad)
        ui.pushButton_2.clicked.connect(self.up)

    def ad(self):
        self.window = ADD()
        self.window.show()
        self.hide()

    def up(self):
        self.w = UP()
        self.w.show()
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
