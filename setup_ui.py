# ///////////////////////////////////////////////////////////////
#
# BY: Thomas Lu
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////

# IMPORT THEME COLORS
# ///////////////////////////////////////////////////////////////
from gui.core.json_themes import Themes
from gui.core.json_settings import Settings
# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui.widgets import *
from qt_core import *
# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////
# MAIN FUNCTIONS
# ///////////////////////////////////////////////////////////////
from gui.core.functions import Functions
from ui_PAS_window import Ui_Dialog
import os
# PY WINDOW
# ///////////////////////////////////////////////////////////////
class SetupMainWindow:
    def __init__(self):
        super().__init__()
        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_Dialog()
        self.ui.setup_ui(self)



    # SETUP MAIN WINDOW WITH CUSTOM PARAMETERS
    # ///////////////////////////////////////////////////////////////
    def setup_gui(self):
        # APP TITLE
        # ///////////////////////////////////////////////////////////////

        self.setWindowTitle(self.settings["app_name"])
        self.setWindowIcon(QtGui.QIcon(self.settings["icon"]))


        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings(self.settingFilesFolderPath)
        self.settings = settings.globalSettingitems

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes(self.settingFilesFolderPath)
        self.themes = themes.items

        palette = QPalette()
        palette.setColor(self.backgroundRole(),self.themes["app_color"]["bg_one"])
        self.setPalette(palette)

        # ICON BUTTON 1
        self.icon_button_1 = PyIconButton(
            icon_path = Functions.set_svg_icon("icon_refresh.svg"),
            parent = self,
            app_parent = self,
            tooltip_text = "               Discard Changes",
            width = 35,
            height = 35,
            radius = 8,
            dark_one = self.themes["app_color"]["dark_one"],
            icon_color = self.themes["app_color"]["icon_color"],
            icon_color_hover = self.themes["app_color"]["icon_hover"],
            icon_color_pressed = self.themes["app_color"]["icon_active"],
            icon_color_active = self.themes["app_color"]["icon_active"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_hover = self.themes["app_color"]["dark_three"],
            bg_color_pressed = self.themes["app_color"]["pink"]
        )


        # ICON BUTTON 2
        self.icon_button_2 = PyIconButton(
            icon_path = Functions.set_svg_icon("icon_add_user.svg"),
            parent = self,
            app_parent = None,
            tooltip_text = "BTN with tooltip",
            width = 40,
            height = 40,
            radius = 8,
            dark_one = self.themes["app_color"]["dark_one"],
            icon_color = self.themes["app_color"]["icon_color"],
            icon_color_hover = self.themes["app_color"]["icon_hover"],
            icon_color_pressed = self.themes["app_color"]["white"],
            icon_color_active = self.themes["app_color"]["icon_active"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_hover = self.themes["app_color"]["dark_three"],
            bg_color_pressed = self.themes["app_color"]["green"],
        )

        self.push_button_3 = PyPushButton(
            text="ADD",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.push_button_3.setMinimumHeight(30)


        self.line_edit_money = PyLineEdit(
            text="",
            place_holder_text="Amount of Money",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.line_edit_money.setMinimumHeight(30)

        self.line_edit_description = PyLineEdit(
            text="",
            place_holder_text="Description",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.line_edit_description.setMinimumHeight(30)

        self.ui.horizontalLayout_3.addWidget(self.line_edit_money)
        self.ui.horizontalLayout_3.addWidget(self.line_edit_description)
        self.ui.horizontalLayout_3.addWidget(self.push_button_3)








