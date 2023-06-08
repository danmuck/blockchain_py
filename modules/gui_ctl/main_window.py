from PySide6 import QtCore
from PySide6.QtCore import QSize
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QStatusBar,
    QMainWindow,
    QPushButton,
    QToolBar,
    QGridLayout,
    QVBoxLayout,
    QWidget,
)

from modules.chain_ctl import Proof_of_Work
from modules.chain_ctl.Blockchain import Blockchain_
from modules.chain_ctl.Miner import Auto_Miner_
from modules.chain_ctl.Minter import Minter_
from modules.chain_ctl.Transactions import Wallet_

from modules.gui_ctl.menus.stacked_menu import MenuStack
from modules.gui_ctl.tab_widget import TabWidget

CHAIN: Blockchain_
CHAIN_ID: int
PROOF_OF_WORK: Proof_of_Work
MINER: Auto_Miner_
MINTER: Minter_
WALLET: Wallet_


class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Blockchain.py")
        self.resize(800, 600)

        # Bars
        self.set_menu_bar()
        self.set_toolbar()
        self.set_status_bar()

        # Compartments
        self.stack_menu = MenuStack(self)
        self.tab_widget = TabWidget()
        main_layout = self.set_main_layout()

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        self.centralWidget().setLayout(main_layout)

        # TESTING
        button_1 = QPushButton("Button 1")
        button_1.clicked.connect(self.button_1_clicked)
        # self.setCentralWidget(stack_menu)

    def set_main_layout(self) -> QGridLayout:
        menu_layout = QVBoxLayout()
        content_layout = QVBoxLayout()

        self.stack_menu = MenuStack(self)
        self.tab_widget = TabWidget()

        menu_layout.addWidget(self.stack_menu)
        content_layout.addWidget(self.tab_widget)

        grid_layout = QGridLayout()
        grid_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        # grid_layout.setColumnMinimumWidth(0, 560)
        grid_layout.setColumnStretch(0, 4)
        grid_layout.setColumnStretch(1, 6)

        grid_layout.addLayout(menu_layout, 0, 0)
        grid_layout.addLayout(content_layout, 0, 1)

        return grid_layout

    def set_menu_bar(self):
        # MenuBar and Menus
        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)

        # File Menu
        file_menu = menu_bar.addMenu("File")
        quit_action = file_menu.addAction("Goodbye")
        quit_action.triggered.connect(self.quit_app)

        # Edit Menu
        edit_menu = menu_bar.addMenu("Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")

        # Other Menu Options
        menu_bar.addMenu("Window")
        menu_bar.addMenu("Settings")
        menu_bar.addMenu("Help")

    def set_toolbar(self):
        # Toolbar
        toolbar = QToolBar("Main Toolbar")
        toolbar.setIconSize(QSize(22, 22))
        self.addToolBar(toolbar)

        quit_button = QAction("Goodbye", self)
        quit_button.triggered.connect(self.quit_app)

        action_1 = QAction("Hello", self)
        action_1.triggered.connect(self.toolbar_button_click)

        toolbar.addAction(quit_button)
        toolbar.addAction(action_1)

        toolbar.addSeparator()
        toolbar.addWidget(QPushButton("Click Me"))

    def set_status_bar(self):
        # Statusbar
        self.setStatusBar(QStatusBar(self))

    def button_1_clicked(self):
        self.statusBar().showMessage("Button 1 Clicked", 1500)

    def toolbar_button_click(self):
        self.statusBar().showMessage("This is the StatusBar", 3000)
        print("Clicked the toolbar -> action_1")

    def quit_app(self):
        self.app.quit()
