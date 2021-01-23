from PySide6.QtWidgets import *
from PySide6.QtGui import *
from designer.ps6_tables import Ui_Form
from database.connector import dataBase
import sys

class tables_app(QDialog):
    def __init__(self):
        super(tables_app, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # ========================
        # ----- QTableWidget -----
        # ========================
        # ----- Obtener datos -----
        connector_widget = dataBase()
        self.datos_widget = connector_widget.getData()
        # ----- Setear filas y columnas -----
        self.column_widget = len(self.datos_widget[0]) - 1
        self.fila_widget = len(self.datos_widget)
        self.ui.tableWidget.setColumnCount(self.column_widget)
        self.ui.tableWidget.setRowCount(self.fila_widget)
        # ----- Encabezados -----
        lista_widget = ["Producto", "Codigo", "Precio"]
        self.ui.tableWidget.setHorizontalHeaderLabels(lista_widget)
        # ----- Mostrar datos -----
        for fila in range(len(self.datos_widget)):
            for columna in range(1, len(self.datos_widget[0])):
                self.ui.tableWidget.setItem(fila, columna - 1, QTableWidgetItem(str(self.datos_widget[fila][columna])))
        # ----- Eventos -----
        self.ui.tableWidget.doubleClicked.connect(self.set_table_view)
        # ======================
        # ----- QTableView -----
        # ======================
        # ----- Obtener datos -----
        connector_view = dataBase()
        self.datos_view = connector_view.getData()
        # ----- Crear modelo -----
        self.fila_view = len(self.datos_view)
        self.column_view = len(self.datos_view[0]) - 1
        self.model = QStandardItemModel(self.fila_view, self.column_view)
        self.ui.tableView.setModel(self.model)
        # ----- Encabezados -----
        lista_view = ["Producto", "Codigo", "Precio"]
        self.model.setHorizontalHeaderLabels(lista_view)
        # ----- Mostrar datos -----
        for fila in range(len(self.datos_view)):
            for columna in range(1, len(self.datos_view[0])):
                self.model.setItem(fila, columna - 1, QStandardItem(str(self.datos_view[fila][columna])))
        # ----- Eventos -----
        self.ui.tableView.doubleClicked.connect(self.set_table_widget)

    def set_table_view(self, fila):
        data = self.datos_widget[fila.row()]
        fila = self.fila_view
        # ----- Rellenar dato -----
        for y in range(1, len(data)):
            self.model.setItem(fila, y - 1, QStandardItem(str(data[y])))
        # ----- Extra -----
        self.fila_view += 1

    def set_table_widget(self, fila):
        data = self.datos_view[fila.row()]
        fila = self.fila_widget
        # ----- Rellenar dato -----
        self.ui.tableWidget.insertRow(fila)
        for y in range(1, len(data)):
            self.ui.tableWidget.setItem(fila, y - 1, QTableWidgetItem(str(data[y])))
        # ----- Extra -----
        self.fila_widget += 1

if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_app = tables_app()
    my_app.show()
    sys.exit(app.exec_())
