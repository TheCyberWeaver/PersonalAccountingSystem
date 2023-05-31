# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PAS_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QLabel, QLayout, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(500, 675)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 35))
        self.label.setStyleSheet(u"font: 700 18pt \"Segoe Script\";")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamilies([u"Segoe Script"])
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.label_2.setStyleSheet(u"font: 700 14pt \"Segoe Script\";")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(48)
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_3)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.comboBox_period = QComboBox(Dialog)
        self.comboBox_period.addItem("")
        self.comboBox_period.addItem("")
        self.comboBox_period.addItem("")
        self.comboBox_period.addItem("")
        self.comboBox_period.setObjectName(u"comboBox_period")
        self.comboBox_period.setMaximumSize(QSize(100, 16777215))

        self.verticalLayout_3.addWidget(self.comboBox_period)

        self.comboBox_currency = QComboBox(Dialog)
        self.comboBox_currency.addItem("")
        self.comboBox_currency.addItem("")
        self.comboBox_currency.addItem("")
        self.comboBox_currency.setObjectName(u"comboBox_currency")
        self.comboBox_currency.setMaximumSize(QSize(100, 16777215))

        self.verticalLayout_3.addWidget(self.comboBox_currency)

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(100, 16777215))

        self.verticalLayout_3.addWidget(self.pushButton)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.comboBox_category = QComboBox(Dialog)
        self.comboBox_category.addItem("")
        self.comboBox_category.addItem("")
        self.comboBox_category.addItem("")
        self.comboBox_category.addItem("")
        self.comboBox_category.addItem("")
        self.comboBox_category.addItem("")
        self.comboBox_category.addItem("")
        self.comboBox_category.addItem("")
        self.comboBox_category.addItem("")
        self.comboBox_category.setObjectName(u"comboBox_category")
        self.comboBox_category.setMaximumSize(QSize(130, 16777215))
        self.comboBox_category.setEditable(False)

        self.horizontalLayout_3.addWidget(self.comboBox_category)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.webEngineView = QWebEngineView(Dialog)
        self.webEngineView.setObjectName(u"webEngineView")
        self.webEngineView.setMinimumSize(QSize(450, 250))
        self.webEngineView.setUrl(QUrl(u"about:blank"))

        self.horizontalLayout_2.addWidget(self.webEngineView)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Personal Accounting System", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Balance", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"123", None))
        self.comboBox_period.setItemText(0, QCoreApplication.translate("Dialog", u"Total", None))
        self.comboBox_period.setItemText(1, QCoreApplication.translate("Dialog", u"Year", None))
        self.comboBox_period.setItemText(2, QCoreApplication.translate("Dialog", u"Month", None))
        self.comboBox_period.setItemText(3, QCoreApplication.translate("Dialog", u"Week", None))

        self.comboBox_currency.setItemText(0, QCoreApplication.translate("Dialog", u"Yuan", None))
        self.comboBox_currency.setItemText(1, QCoreApplication.translate("Dialog", u"Euro", None))
        self.comboBox_currency.setItemText(2, QCoreApplication.translate("Dialog", u"US Dollar", None))

        self.pushButton.setText(QCoreApplication.translate("Dialog", u"History", None))
        self.comboBox_category.setItemText(0, QCoreApplication.translate("Dialog", u"Work", None))
        self.comboBox_category.setItemText(1, QCoreApplication.translate("Dialog", u"School", None))
        self.comboBox_category.setItemText(2, QCoreApplication.translate("Dialog", u"Refund", None))
        self.comboBox_category.setItemText(3, QCoreApplication.translate("Dialog", u"Entertainment", None))
        self.comboBox_category.setItemText(4, QCoreApplication.translate("Dialog", u"Food", None))
        self.comboBox_category.setItemText(5, QCoreApplication.translate("Dialog", u"Others", None))
        self.comboBox_category.setItemText(6, QCoreApplication.translate("Dialog", u"Transportation", None))
        self.comboBox_category.setItemText(7, QCoreApplication.translate("Dialog", u"Rent", None))
        self.comboBox_category.setItemText(8, QCoreApplication.translate("Dialog", u"Projects", None))

    # retranslateUi

