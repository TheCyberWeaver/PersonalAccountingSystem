# IMPORT THEME COLORS
# ///////////////////////////////////////////////////////////////
from gui.core.json_themes import Themes
from gui.core.functions import Functions
from gui.core.json_settings import Settings
from ui_PAS_History import Ui_Form
from qt_core import *
from gui.widgets import *
import pandas as pd
import sys
class historyWindow(QWidget):
    def __init__(self,DB,DBcursor):
        super().__init__()

        self.ui=Ui_Form()
        self.ui.setupUi(self)

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items
        self.setupUI()

        palette = QPalette()
        palette.setColor(self.backgroundRole(), self.themes["app_color"]["bg_one"])
        self.setPalette(palette)

        self.cursorObject=DBcursor
        self.mydb=DB

        self.icon_button_1.clicked.connect(lambda: self.fetchAllFromDatabase())
        self.push_button_1.clicked.connect(lambda: self.saveAll())
        self.push_button_2.clicked.connect(lambda: self.table_widget.insertRow(self.table_widget.rowCount()))
        self.push_button_3.clicked.connect(lambda: self.deleteCurrentRow())

        self.fetchAllFromDatabase()

    def fetchAllFromDatabase(self):

        # 保留表头
        self.table_widget.clearContents()
        self.table_widget.setRowCount(0)
        # 获取所有数据库信息并打印到表上
        showall = "select * from transactions"

        self.cursorObject.execute(showall)

        result = self.cursorObject.fetchall()
        # print(result)

        for id, category, amount, time, description, currency in result:
            row_number = self.table_widget.rowCount()
            self.table_widget.insertRow(row_number)  # Insert row
            self.table_widget.setItem(row_number, 0, QTableWidgetItem(category))
            self.table_widget.setItem(row_number, 1, QTableWidgetItem(str(amount)))
            self.table_widget.setItem(row_number, 2, QTableWidgetItem(currency))
            self.table_widget.setItem(row_number, 3, QTableWidgetItem(str(time)))
            self.table_widget.setItem(row_number, 4, QTableWidgetItem(description))
            self.table_widget.setRowHeight(row_number, 22)

        print("[History][Info]: data all updated from database")
    def deleteCurrentRow(self):
        if self.table_widget.currentRow() != None:
            currentRowIndex = self.table_widget.currentRow()
        else:
            return
        print("[History][info]: Deleting row",currentRowIndex)
        self.table_widget.removeRow(currentRowIndex)

    def saveAll(self):

        self.cursorObject.execute("DELETE FROM transactions")  # 先删除整个表，然后重新填写，逻辑最简单，保证数据库id完整性，没有跳行

        row_number = self.table_widget.rowCount()
        databaseID = 1  # 循环变量，用于表示数据库内当前应当存放的id
        for i in range(row_number):
            try:
                if self.table_widget.item(i, 0) == None:
                    category = ""  # 如果item为空特殊处理 #懒得整理逻辑，直接复制
                else:
                    category = self.table_widget.item(i, 0).text()

                if self.table_widget.item(i, 1) == None:
                    amount = ""
                else:
                    amount = self.table_widget.item(i, 1).text()

                if self.table_widget.item(i, 2) == None:
                    currency = ""
                else:
                    currency = self.table_widget.item(i, 2).text()

                if self.table_widget.item(i, 3) == None:
                    time = ""
                else:
                    time = self.table_widget.item(i, 3).text()

                if self.table_widget.item(i, 4) == None:
                    description = ""
                else:
                    description = self.table_widget.item(i, 4).text()

                description = description.strip()  # description最后会有\r，我也不知道为什么,需要在拼接字符串前将其删除

                if category == "" and amount == "" and currency == "" and time == "" and description == "":  # 如果一整行为空则放弃insert这一行，数据库id不会改变
                    continue

                insert = "INSERT INTO transactions(Category, Amount, Time, Description, Currency) VALUES('" \
                + category + "\' , \'" + amount + "\' ," + "STR_TO_DATE(\""+time+"\", \"%Y-%m-%d\")"+", \'" + description + "\' , \'" + currency + "\');"  # 加入这一行
                self.cursorObject.execute(insert)
            except:
                continue

        print("[History][Info]: save all data to database")
        self.fetchAllFromDatabase()  # 保存后刷新数据

        self.mydb.commit()  # 提交数据，否则DDL语句不会自动commit
    def setupUI(self):
        # ICON BUTTON 1
        self.icon_button_1 = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_refresh.svg"),
            parent=self,
            app_parent=self,
            tooltip_text="               Discard Changes",
            width=35,
            height=35,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["icon_active"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["pink"]
        )


        # PUSH BUTTON 1
        self.push_button_1 = PyPushButton(
            text="SAVE",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.push_button_1.setMaximumHeight(30)
        self.push_button_1.setMinimumWidth(200)
        self.icon_2 = QIcon(Functions.set_svg_icon("icon_save.svg"))
        self.push_button_1.setIcon(self.icon_2)

        # PUSH BUTTON 2
        self.push_button_2 = PyPushButton(
            text="New",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )

        self.icon_3 = QIcon(Functions.set_svg_icon("add.svg"))
        self.push_button_2.setMaximumHeight(30)
        self.push_button_2.setIcon(self.icon_3)
        self.push_button_2.setIconSize(QSize(28, 28))

        # PUSH BUTTON 3
        self.push_button_3 = PyPushButton(
            text="Delete",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon_4 = QIcon(Functions.set_svg_icon("delete.svg"))
        self.push_button_3.setMaximumHeight(30)
        self.push_button_3.setIcon(self.icon_4)
        self.push_button_3.setIconSize(QSize(43, 43))

        # TABLE WIDGETS
        self.table_widget = PyTableWidget(
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["context_color"],
            bg_color=self.themes["app_color"]["bg_two"],
            header_horizontal_color=self.themes["app_color"]["bg_three"],
            header_vertical_color=self.themes["app_color"]["bg_three"],
            bottom_line_color=self.themes["app_color"]["bg_three"],
            grid_line_color=self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color=self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color=self.themes["app_color"]["bg_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.table_widget.setColumnCount(5)
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_widget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table_widget.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Columns / Header
        self.column_1 = QTableWidgetItem()
        self.column_1.setTextAlignment(Qt.AlignCenter)
        self.column_1.setText("Category")

        self.column_2 = QTableWidgetItem()
        self.column_2.setTextAlignment(Qt.AlignCenter)
        self.column_2.setText("Amount")

        self.column_3 = QTableWidgetItem()
        self.column_3.setTextAlignment(Qt.AlignCenter)
        self.column_3.setText("Currency")

        self.column_4 = QTableWidgetItem()
        self.column_4.setTextAlignment(Qt.AlignCenter)
        self.column_4.setText("Date")

        self.column_5 = QTableWidgetItem()
        self.column_5.setTextAlignment(Qt.AlignCenter)
        self.column_5.setText("Description")
        # Set column
        self.table_widget.setHorizontalHeaderItem(0, self.column_1)
        self.table_widget.setHorizontalHeaderItem(1, self.column_2)
        self.table_widget.setHorizontalHeaderItem(2, self.column_3)
        self.table_widget.setHorizontalHeaderItem(3, self.column_4)
        self.table_widget.setHorizontalHeaderItem(4, self.column_5)

        self.ui.horizontalLayout.addWidget(self.icon_button_1)
        self.ui.horizontalLayout.addWidget(self.push_button_1)
        self.ui.horizontalLayout.addWidget(self.push_button_2)
        self.ui.horizontalLayout.addWidget(self.push_button_3)

        self.ui.horizontalLayout_2.addWidget(self.table_widget)