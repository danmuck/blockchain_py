from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QGridLayout,
)


class MainMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.button_layout = QVBoxLayout()
        self.buttons = {}

        btn_font = QFont("Courier New")
        btn_font.setPointSize(16)

        # Items
        text_label = QLabel("    -- Where to next?")
        text_label.setFont(btn_font)

        self.buttons = {
            "office": QPushButton("Office"),
            "workshop": QPushButton("Workshop"),
            "craft": QPushButton("Crafting Bench"),
            "throw": QPushButton("Throw $DIRT"),
            "trade": QPushButton("Trading Post"),
            "message": QPushButton("Message Board"),
            "mound": QPushButton("The Mound"),
            "pit": QPushButton("The Pit"),
            "wallet": QPushButton("Wallet Options"),
            "goodbye": QPushButton("Back"),
        }

        for key, item in self.buttons.items():
            self.button_layout.addWidget(item)
            item.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            item.setMinimumSize(52, 36)
            item.setMaximumWidth(300)
            item.setFont(btn_font)

        layout = QGridLayout()
        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 1)

        layout.addWidget(text_label, 0, 0)
        layout.addLayout(self.button_layout, 1, 0)
        self.setLayout(layout)
