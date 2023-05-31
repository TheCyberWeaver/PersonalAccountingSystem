# -*- coding: utf-8 -*-
# 导入sys
import sys
import mysql.connector
import string
import datetime

from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from PySide6.QtGui import *
# 任何一个PySide界面程序都需要使用QApplication
# 我们要展示一个普通的窗口，所以需要导入QWidget，用来让我们自己的类继承
from PySide6.QtWidgets import QApplication, QWidget
# 导入我们生成的界面
from ui_PAS_window import *

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
import os
import sys
import tempfile
from plotly.io import to_html
import plotly.graph_objs as go
from PySide6 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets,QtWebEngineCore
from ui_PAS_History import Ui_Form
from gui.core.json_settings import Settings
from setup_ui import *
from ui_PAS_window import Ui_Dialog
from historyWindow import historyWindow
# 继承QWidget类，以获取其属性和方法

exchangeRate={
    "Yuan":1,
    "Euro":7.5,
    "US Dollar":6.5
}

class PersonalAccountingSystem(QWidget):
    def __init__(self):
        super().__init__()

        self.settingFilesFolderPath=""

        # 设置界面为我们生成的界面
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)


        #self.setFixedSize(self.width(), self.height())

        settings = Settings(self.settingFilesFolderPath)
        print("[PAS][info]: using",settings.settings_path)
        self.settings = settings.globalSettingitems
        self.projectPath=settings.get_project_path()


        SetupMainWindow.setup_gui(self)

        # /////////////////////////////////////////////////////////////////////////////
        # log into database
        # /////////////////////////////////////////////////////////////////////////////
        self.mydb = mysql.connector.connect(
            host=self.settings["mysql_host"],
            user=self.settings["user"],
            password=self.settings["password"]
        )

        # /////////////////////////////////////////////////////////////////////////////
        # manipulating database
        # /////////////////////////////////////////////////////////////////////////////
        self.cursorObject = self.mydb.cursor()

        createDatabase = "CREATE DATABASE IF NOT EXISTS personal_accounting_system"
        useDatabase = "USE personal_accounting_system"
        #createTableWallet = "CREATE TABLE IF NOT EXISTS wallet(id INT PRIMARY KEY,name varchar(50),description text, current_money INT);"
        createTableTransactions = "CREATE TABLE IF NOT EXISTS transactions(idTransactions INT NOT NULL AUTO_INCREMENT PRIMARY KEY," \
                            "Category varchar(45),Amount FLOAT,Time DATE,Description text, Currency varchar(25));"
        initalWalletData=""
        try:
            self.cursorObject.execute(useDatabase)
        except:
            print("[PAS][info]: Creating new Database called passwordmanager")
            self.cursorObject.execute(createDatabase)
            self.cursorObject.execute(initalWalletData)


        self.cursorObject.execute(useDatabase)
        self.cursorObject.execute(createTableTransactions)

        # /////////////////////////////////////////////////////////////////////////////
        # data
        # /////////////////////////////////////////////////////////////////////////////
        self.wallet=[]
        self.transactions=[]

        self.labels=["Expenditure","Income"]
        self.parents=["",""]
        self.values=[100,100]
        # /////////////////////////////////////////////////////////////////////////////
        #
        # /////////////////////////////////////////////////////////////////////////////
        self.updateStatistic()

        self.uiInitiation()



    def uiInitiation(self):
        self.ui.label_3.setStyleSheet('color: white')
        self.push_button_3.clicked.connect(lambda: self.addOneRowOfData())
        self.ui.pushButton.clicked.connect(lambda: self.openHistory())
        self.ui.comboBox_currency.currentTextChanged.connect(lambda: self.updateStatistic())

    def openHistory(self):
        self.w = historyWindow(self.mydb,self.cursorObject)
        self.w.show()

    def addOneRowOfData(self):
        sentence="INSERT INTO transactions(Category, Amount, Time, Description, Currency) VALUES("
        sentence+="\'"+self.ui.comboBox_category.currentText()+"\',"
        sentence+=self.line_edit_money.text()+","
        sentence+="STR_TO_DATE(\""+str(datetime.date.today())+"\", \"%Y-%m-%d\")"+","
        sentence+="\""+self.line_edit_description.text()+"\","
        sentence+="\""+self.ui.comboBox_currency.currentText()+"\");"
        self.cursorObject.execute(sentence)
        self.mydb.commit()

        self.updateStatistic()

    def fetchAllFromDatabase(self):

        # 获取所有数据库信息并打印到表上
        showall = "select * from transactions"

        self.cursorObject.execute(showall)

        self.transactions = self.cursorObject.fetchall()
        # print(result)


        print("[PAS][Info]: data all updated from database")
    def show_graph(self):



        fig = px.sunburst(self.data_df,
                          path=['outOrIn', 'Category', 'currency'],
                          values='NormalAmount',
                          color='time',
                          color_continuous_scale='RdBu'
                          )
        fig.update_layout(
            autosize=True,
            paper_bgcolor="#44475a",
        )
        import plotly
        #plotly.offline.plot(fig, filename='tmp.html',auto_open=True, config={"responsive": True, 'scrollZoom': False})
        #fig.write_html("file.html")

        self.ui.webEngineView.settings().setAttribute(QtWebEngineCore.QWebEngineSettings.ShowScrollBars, False)
        #self.ui.webEngineView.settings().setAttribute(QtWebEngineCore.QWebEngineSettings.WebGLEnabled, True)
        self.temp_file = tempfile.NamedTemporaryFile(mode="w", suffix=".html", delete=False, encoding='utf-8')

        self.temp_file.seek(0)
        if fig is None:
            fig = go.Figure()
        html = to_html(fig, config={"responsive": True, 'scrollZoom': True,"modeBarButtonsToRemove": ['toImage', 'hoverClosestPie'],"displaylogo": False})
        html += "\n<style>body{margin: 0;}" \
                "\n.plot-container,.main-svg,.svg-container{width:100% !important; height:100% !important;}</style>"

        #print(html)
        self.temp_file.write(html)
        self.temp_file.truncate()
        self.temp_file.seek(0)
        self.ui.webEngineView.load(QtCore.QUrl.fromLocalFile(self.temp_file.name))
        self.ui.webEngineView.setZoomFactor(0.8)




    def updateStatistic(self):
        self.fetchAllFromDatabase()

        data=[]
        column_names = ["Category", "NormalAmount", "time","currency","outOrIn"]
        totalMoney=0
        for id, Category, amount, time, description, currency in self.transactions:
            totalMoney += exchangeRate.get(currency, 0) * amount
            outOrIn=""
            if amount<=0:
                outOrIn="Expenditure"
            else:
                outOrIn="Income"
            data.append([Category,abs(exchangeRate.get(currency, 0) * amount),time,currency,outOrIn])
        self.data_df = pd.DataFrame(np.array(data),columns=column_names)

        self.ui.label_3.setText(str(round(totalMoney/exchangeRate[self.ui.comboBox_currency.currentText()],2)))
        self.show_graph()
    def btn_clicked(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        if btn.objectName() == "btn_search":
            print("hello")

    def btn_released(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        # DEBUG
        print(f"Button {btn.objectName()}, released!")
    # RESIZE EVENT
    # ///////////////////////////////////////////////////////////////

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

    def closeEvent(self, event):
        sys.exit(0)

# 程序入口
if __name__ == "__main__":
    # 初始化QApplication，界面展示要包含在QApplication初始化之后，结束之前
    app = QApplication(sys.argv)

    # 初始化并展示我们的界面组件
    window = PersonalAccountingSystem()
    print("[info]: Process", window.settings["app_name"], "is starting")
    window.show()

    sys.exit(app.exec())
