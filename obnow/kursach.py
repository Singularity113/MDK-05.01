import sqlite3
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from qt_material import apply_stylesheet


class sklad(QWidget):
    def __init__(self):
        super(sklad, self).__init__()

        self.setWindowTitle('Склад')
        self.db_mat = sqlite3.connect(r'D:\kursach\obnow\material_accounting.db')
        self.cur=self.db_mat.cursor()
        self.cur.execute("""BEGIN""") 
        G = self.cur.execute("""SELECT COUNT() FROM material_accounting""").fetchone()[0]
        all = self.cur.execute("""SELECT * FROM material_accounting""").fetchall()
        self.cur.connection.commit()  
        assert G == len(all)
        self.tableWidget = QTableWidget()
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setRowCount(G)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(['id','Название','Количество(кг)','Цена за кг(руб)'])
        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)
        self.update()

        self.lbl_name = QLabel(self)
        self.lbl_name.setText('Введите наименование:')
        self.lbl_name.setFixedWidth(150)
        self.lbl_name.setFixedHeight(20)
        self.grid_layout.addWidget(self.lbl_name, 0, 2)

        self.e_name = QLineEdit(self)
        self.e_name.setFixedWidth(150)
        self.grid_layout.addWidget(self.e_name, 1, 2)

        self.lbl_col = QLabel(self)
        self.lbl_col.setText('Введите количество:')
        self.lbl_col.setFixedWidth(150)
        self.lbl_col.setFixedHeight(20)
        self.grid_layout.addWidget(self.lbl_col, 2, 2)

        self.e_col = QLineEdit(self)
        self.e_col.setFixedWidth(150)
        self.grid_layout.addWidget(self.e_col, 3, 2)

        self.btn_add = QPushButton('добавить')
        self.btn_add.setFixedWidth(150)
        self.grid_layout.addWidget(self.btn_add, 4, 2)
        self.btn_add.clicked.connect(self.add)

        self.btn_del = QPushButton('удалить')
        self.btn_del.setFixedWidth(150)
        self.grid_layout.addWidget(self.btn_del, 5, 2)
        self.btn_del.clicked.connect(self.dell)
        
        self.btn_zak = QPushButton('заказ сырья')
        self.btn_zak.setFixedWidth(150)
        self.grid_layout.addWidget(self.btn_zak, 6, 2)
        self.btn_zak.clicked.connect(self.show_win)
        
    def show_win(self):
        self.w2 = zakup()
        self.w2.show()
        # конец виджетов

    def update(self):
        self.tableWidget.clearContents()
        self.db_mat = sqlite3.connect(r'D:\kursach\obnow\material_accounting.db')
        self.cur=self.db_mat.cursor() 
        self.cur.execute("""BEGIN""") 
        G = self.cur.execute("""SELECT COUNT() FROM material_accounting""").fetchone()[0]
        all = self.cur.execute("""SELECT * FROM material_accounting""").fetchall()
        self.cur.connection.commit()  
        assert G == len(all)
        self.grid_layout.addWidget(self.tableWidget, 0, 0, G, 1)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setRowCount(G)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(['id','Название','Количество(кг)','Цена за кг(руб)'])
        
        
        self.cur.execute("""SELECT * FROM material_accounting""")
        self.it = self.cur.fetchall()
        for row in range(G):
            for col in range(4):
                self.tableWidget.setItem(row,col, QTableWidgetItem(str(self.it[row][col])))
        self.tableWidget.setColumnWidth(0,70)
        self.tableWidget.setColumnWidth(1,120)
        self.tableWidget.setColumnWidth(2,175)
        self.tableWidget.setColumnWidth(3,175)
        self.db_mat.close()

    def add(self):
        self.db_mat = sqlite3.connect(r'D:\kursach\obnow\material_accounting.db')
        self.cur=self.db_mat.cursor()
        self.cur.execute(f"""INSERT INTO material_accounting(name,count)
        VALUES('{self.e_name.text()}',{self.e_col.text()})
        """)
        self.db_mat.commit()
        self.e_name.clear()
        self.e_col.clear()
        self.db_mat.close()

        self.update()

    def dell(self):
        self.db_mat = sqlite3.connect(r'D:\kursach\obnow\material_accounting.db')
        self.cur=self.db_mat.cursor()
        self.id_m = self.tableWidget.model().data(self.tableWidget.currentIndex())
        self.cur.execute(f"""DELETE FROM material_accounting WHERE id_m='{self.id_m}'""")
        self.db_mat.commit()
        self.db_mat.close()
        self.update()

class zakup(QWidget):
    def __init__(self):
        super(zakup, self).__init__() 
        self.setWindowTitle('Заказ сырья')

        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)
        self.lbl_name = QLabel(self)
        self.lbl_name.setText('Введите наименование:')
        self.lbl_name.setFixedWidth(150)
        self.lbl_name.setFixedHeight(20)
        self.grid_layout.addWidget(self.lbl_name, 0, 2)

        self.e_name = QLineEdit(self)
        self.e_name.setFixedWidth(150)
        self.grid_layout.addWidget(self.e_name, 1, 2)

        self.lbl_col = QLabel(self)
        self.lbl_col.setText('Введите количество:')
        self.lbl_col.setFixedWidth(150)
        self.lbl_col.setFixedHeight(20)
        self.grid_layout.addWidget(self.lbl_col, 2, 2)

        self.e_col = QLineEdit(self)
        self.e_col.setFixedWidth(150)
        self.grid_layout.addWidget(self.e_col, 3, 2)

        self.e_col = QLineEdit(self)
        self.e_col.setFixedWidth(150)
        self.grid_layout.addWidget(self.e_col, 3, 2)

class menu(QWidget):
    def __init__(self):
        super(menu, self).__init__() 
        self.setWindowTitle('Меню')
        self.setFixedSize(500,500)

        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)

        self.btn_sklad = QPushButton('Склад')
        self.btn_sklad.setFixedSize(125,125)
        self.grid_layout.addWidget(self.btn_sklad, 0, 0)
        self.btn_sklad.clicked.connect(self.show_sklad)

        self.btn_zakup = QPushButton('Заказ сырья')
        self.btn_zakup.setFixedSize(125,125)
        self.grid_layout.addWidget(self.btn_zakup, 0, 1)
        self.btn_zakup.showMinimized()
        self.btn_zakup.clicked.connect(self.show_zakup)
        

    def show_sklad(self):
        
        self.skl=sklad()
        self.skl.show()
    
    def show_zakup(self):
        self.zak = zakup()
        self.zak.show()
        
        

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = menu()
    apply_stylesheet(app, theme='dark_cyan.xml')
    win.show()
    # sys.__excepthook__ = sys.excepthook
    # def my_exeption_hook(exctype, value, traceback):
    #     msg = QMessageBox()
    #     msg.setIcon(QMessageBox.Information)
    #     msg.setText('Введены не верные данные')
    #     msg.setWindowTitle('Ошибка!')
    #     msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    #     msg.exec_()
    # sys.excepthook = my_exeption_hook
    sys.exit(app.exec_())
