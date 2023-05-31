import os
import sys
import tempfile
from plotly.io import to_html
import plotly.graph_objs as go
from PySide6 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets,QtWebEngineCore


class PlotlyViewer(QtWebEngineWidgets.QWebEngineView):

    def __init__(self, fig=None):
        super().__init__()
        #self.page().profile().downloadRequested.connect(self.on_downloadRequested)

        self.settings().setAttribute(QtWebEngineCore.QWebEngineSettings.ShowScrollBars, False)
        self.settings().setAttribute(QtWebEngineCore.QWebEngineSettings.WebGLEnabled, True)

        self.temp_file = tempfile.NamedTemporaryFile(mode="w", suffix=".html", delete=False,encoding='utf-8')
        self.set_figure(fig)

        self.resize(700, 600)
        self.setWindowTitle("Draw")

    def set_figure(self, fig=None):
        self.temp_file.seek(0)
        if fig is None:
            fig = go.Figure()
        fig.update_xaxes(showspikes=True)
        fig.update_yaxes(showspikes=True)
        html = to_html(fig, config={"responsive": True, 'scrollZoom': True})
        html += "\n<style>body{margin: -50;}" \
                "\n.plot-container,.main-svg,.svg-container{width:200% !important; height:200% !important;}</style>"

        self.temp_file.write(html)
        self.temp_file.truncate()
        self.temp_file.seek(0)
        self.load(QtCore.QUrl.fromLocalFile(self.temp_file.name))

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        self.temp_file.close()
        os.unlink(self.temp_file.name)
        super().closeEvent(event)

    def sizeHint(self) -> QtCore.QSize:
        return QtCore.QSize(400, 400)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=[1, 2, 3],
        y=[4, 5, 6],
        name="yaxis1 data"
    ))
    fig.update_layout(
        xaxis=dict(domain=[0.1, 0.9]),
        yaxis=dict(title="yaxis title", )
    )
    pv = PlotlyViewer(fig=fig)
    pv.show()
    app.exec_()