
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
import plotly
from qt_core import *
from PySide6 import QtWidgets,QtWebEngineWidgets,QtCore
class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.button = QtWidgets.QPushButton('Plot', self)
        self.browser = QtWebEngineWidgets.QWebEngineView(self)

        vlayout = QtWidgets.QVBoxLayout(self)
        vlayout.addWidget(self.button, alignment=QtCore.Qt.AlignHCenter)
        vlayout.addWidget(self.browser)

        self.button.clicked.connect(self.show_graph)
        self.resize(1000,800)

    def show_graph(self):

        df = px.data.tips()
        fig = go.Figure(go.Sunburst(labels=[
            "Female", "Male", "Dinner", "Lunch", 'Dinner ', 'Lunch ', 'Fri', 'Sat',
            'Sun', 'Thu', 'Fri ', 'Thu ', 'Fri  ', 'Sat  ', 'Sun  ', 'Fri   ', 'Thu   '
        ],
            parents=[
                "", "", "Female", "Female", 'Male', 'Male',
                'Dinner', 'Dinner', 'Dinner', 'Dinner',
                'Lunch', 'Lunch', 'Dinner ', 'Dinner ',
                'Dinner ', 'Lunch ', 'Lunch '
            ],
            values=np.append(
                np.append(
                    df.groupby('sex').tip.mean().values,
                    df.groupby(['sex',
                                'time']).tip.mean().values,
                ),
                df.groupby(['sex', 'time',
                            'day']).tip.mean().values),
            marker=dict(colors=px.colors.sequential.Emrld)),
            layout=go.Layout(paper_bgcolor='rgba(0,0,0,0)',
                             plot_bgcolor='rgba(0,0,0,0)'))


        plotly.offline.plot(fig, filename='tmp.html',auto_open=False)

        self.browser.load('E:/PersonalAccountingSystem/tmp.html')
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = Widget()
    widget.show()
    app.exec()