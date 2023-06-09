from PySide6.QtWidgets import (
    QWidget,
    QStackedWidget,
    QVBoxLayout,
    QApplication,
)

from modules.gui_ctl.menus.main_menu_stack import MainMenuStack
from modules.gui_ctl.menus.wallet_menu import WalletInitMenu
from modules.gui_ctl.menus.welcome_menu import WelcomeMenu
from modules.gui_ctl.tab_widget import TabWidget


class MenuStack(QWidget):
    def __init__(self, tabs: TabWidget):
        super().__init__()
        self.tabs = tabs
        # Create a stacked widget
        self.stacked_widget = QStackedWidget()

        # Menus and Parent TabWidget
        self.welcome_menu = WelcomeMenu()
        self.main_menu = MainMenuStack(self.stacked_widget, tabs)
        self.wallet_menu = WalletInitMenu()

        # Add Menus and set initial
        self.stacked_widget.addWidget(self.welcome_menu)
        self.stacked_widget.addWidget(self.main_menu)
        self.stacked_widget.addWidget(self.wallet_menu)

        self.stacked_widget.setCurrentWidget(self.welcome_menu)

        # Set the layout for the widget
        layout = QVBoxLayout(self)
        layout.addWidget(self.stacked_widget)

        # handle connections
        self.handle_welcome_menu_slots()
        self.handle_wallet_menu_slots()

    def handle_welcome_menu_slots(self):
        self.welcome_menu.buttons["custom_chain"].clicked.connect(
            lambda: self.stacked_widget.setCurrentWidget(self.wallet_menu)
        )
        self.welcome_menu.buttons["default_chain"].clicked.connect(
            lambda: self.stacked_widget.setCurrentWidget(self.wallet_menu)
        )
        self.welcome_menu.buttons["goodbye"].clicked.connect(QApplication.quit)

    def handle_wallet_menu_slots(self):
        for k, v in self.wallet_menu.wallets.items():
            v.clicked.connect(
                lambda: self.stacked_widget.setCurrentWidget(self.main_menu)
            )
        self.wallet_menu.buttons["goodbye"].clicked.connect(
            lambda: self.stacked_widget.setCurrentWidget(self.welcome_menu)
        )
