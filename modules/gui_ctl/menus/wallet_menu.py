from PySide6 import QtCore
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QSizePolicy,
    QGridLayout,
)

from modules.gui_ctl.chain.chain_ctl import wallet_quick_login, chain_init


def get_wallets():
    wallets = {}
    try:
        for wallet in wallet_quick_login().print_wallets(False):
            new_button = QPushButton(wallet)
            wallets.update({wallet: new_button})
    except NameError:
        chain_init(0)
        for wallet in wallet_quick_login().print_wallets(False):
            new_button = QPushButton(wallet)
            wallets.update({wallet: new_button})

    wallets_indexed = [*wallets.keys()]
    return wallets, wallets_indexed


def set_grid() -> QGridLayout:
    layout = QGridLayout()
    layout.setRowStretch(0, 1)
    layout.setRowStretch(1, 2)
    layout.setRowStretch(2, 1)
    layout.setColumnStretch(0, 1)
    layout.setColumnStretch(1, 5)
    layout.setColumnStretch(2, 1)

    return layout


class WalletMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.wallet_layout = QVBoxLayout()
        self.button_layout = QVBoxLayout()
        self.buttons = {}
        self.wallets, self.wallets_indexed = get_wallets()

        # Items
        text_label = QLabel("    -- Which wallet would you like to use?")

        self.buttons = {
            "recover": QPushButton("Recover"),
            "testing": QPushButton("TESTING"),
            "goodbye": QPushButton("Goodbye"),
        }

        for key, item in self.wallets.items():
            self.wallet_layout.addWidget(item)
            item.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.handle_button_clicks(key)
            item.setMinimumSize(512, 30)
            item.setMaximumHeight(40)

        for key, item in self.buttons.items():
            self.button_layout.addWidget(item)
            item.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.handle_button_clicks(key)
            item.setMinimumSize(52, 40)
            item.setMaximumSize(240, 40)

        layout = set_grid()
        layout.addWidget(text_label, 0, 0)
        layout.addLayout(self.wallet_layout, 1, 0)
        layout.addLayout(self.button_layout, 2, 0, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)

    def handle_button_clicks(self, key):
        if len(key) == 66:
            self.wallets[key].clicked.connect(
                lambda: wallet_quick_login(False, self.wallets_indexed.index(key))
            )


class WalletInitMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.wallet_layout = QVBoxLayout()
        self.button_layout = QVBoxLayout()
        self.buttons = {}
        self.wallets, self.wallets_indexed = get_wallets()

        # Items
        text_label = QLabel("    -- Which wallet would you like to use?")

        self.buttons = {
            "goodbye": QPushButton("Goodbye"),
        }

        for key, item in self.wallets.items():
            self.wallet_layout.addWidget(item)
            item.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.handle_button_clicks(key)
            item.setMinimumSize(512, 30)
            item.setMaximumHeight(40)

        for key, item in self.buttons.items():
            self.button_layout.addWidget(item)
            item.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            item.setMinimumSize(52, 40)
            item.setMaximumSize(240, 40)

        layout = set_grid()
        layout.addWidget(text_label, 0, 0)
        layout.addLayout(self.wallet_layout, 1, 0)
        layout.addLayout(self.button_layout, 2, 0, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)

    def handle_button_clicks(self, key):
        self.wallets[key].clicked.connect(
            lambda: wallet_quick_login(False, self.wallets_indexed.index(key))
        )
