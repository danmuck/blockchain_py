from PySide6.QtWidgets import (
    QWidget,
    QStackedWidget,
    QVBoxLayout,
    QApplication,
)

from modules.chain_ctl.Blockchain import Blockchain_
from modules.gui_ctl.menus.main_menu import MainMenu
from modules.gui_ctl.menus.wallet_menu import WalletMenu
from modules.gui_ctl.menus.welcome_menu import WelcomeMenu


class MenuStack(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Create a stacked widget
        self.stacked_widget = QStackedWidget()

        # Menus
        self.welcome_menu = WelcomeMenu()
        self.main_menu = MainMenu()
        self.wallet_menu = WalletMenu()

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
        self.handle_main_menu_slots()
        self.handle_wallet_menu_slots()

    def handle_welcome_menu_slots(self):
        self.welcome_menu.buttons["custom_chain"].clicked.connect(
            lambda: self.stacked_widget.setCurrentWidget(self.wallet_menu)
        )
        self.welcome_menu.buttons["default_chain"].clicked.connect(
            lambda: self.stacked_widget.setCurrentWidget(self.wallet_menu)
        )
        self.welcome_menu.buttons["goodbye"].clicked.connect(QApplication.quit)

    def handle_main_menu_slots(self):
        # self.main_menu.buttons["office"].clicked.connect(
        #     lambda: self.stacked_widget.setCurrentWidget(self.welcome_menu)
        # )
        self.main_menu.buttons["wallet"].clicked.connect(
            lambda: self.stacked_widget.setCurrentWidget(self.wallet_menu)
        )
        self.main_menu.buttons["goodbye"].clicked.connect(
            lambda: self.stacked_widget.setCurrentWidget(self.wallet_menu)
        )

    def handle_wallet_menu_slots(self):
        for k, v in self.wallet_menu.wallets.items():
            v.clicked.connect(
                lambda: self.stacked_widget.setCurrentWidget(self.main_menu)
            )
        self.wallet_menu.buttons["testing"].clicked.connect(
            lambda: self.stacked_widget.setCurrentWidget(self.main_menu)
        )
        self.wallet_menu.buttons["goodbye"].clicked.connect(
            lambda: self.stacked_widget.setCurrentWidget(self.welcome_menu)
        )
