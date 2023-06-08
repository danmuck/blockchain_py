from PySide6 import QtCore
from PySide6.QtWidgets import (
    QWidget,
    QStackedWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QSizePolicy,
    QGridLayout,
    QApplication,
)

from modules.gui_ctl.chain.chain_ctl import wallet_quick_login


class WalletMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.wallet_layout = QVBoxLayout()
        self.button_layout = QVBoxLayout()
        self.buttons = {}
        self.wallets = {}

        # Items
        text_label = QLabel("    -- Which wallet would you like to use?")

        goodbye_btn = QPushButton("Goodbye")
        testing_btn = QPushButton("TESTING")
        self.buttons = {
            "testing": testing_btn,
            "goodbye": goodbye_btn,
        }

        for wallet in wallet_quick_login().print_wallets(False):
            new_button = QPushButton(wallet)
            self.wallets.update({wallet: new_button})
        self.wallets_indexed = [*self.wallets.keys()]
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

        layout = QGridLayout()
        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 2)
        layout.setRowStretch(2, 1)
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 5)
        layout.setColumnStretch(2, 1)

        layout.addWidget(text_label, 0, 0)
        layout.addLayout(self.wallet_layout, 1, 0)
        layout.addLayout(self.button_layout, 2, 0, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)

    def handle_button_clicks(self, key):
        if len(key) == 66:
            self.wallets[key].clicked.connect(
                lambda: wallet_quick_login(False, self.wallets_indexed.index(key))
            )

        else:
            match key:
                case "testing":
                    pass
                    # self.buttons["testing"].clicked.connect(QApplication.quit)

    def print_wallets(self):
        i = 0
        for wallet in wallet_quick_login().print_wallets(False):
            print(f"{i}. {wallet}")
            i += 1
