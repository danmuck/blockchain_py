from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QGridLayout,
    QLineEdit,
    QSpinBox,
    QGroupBox,
    QHBoxLayout,
    QRadioButton,
)


class WorkshopMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.button_layout = QVBoxLayout()
        self.buttons = {}

        # Items
        text_label = QLabel(
            """
    -- Workshop::[Auto_Miner]

        Auto-Mine a set number of blocks!
        
        In the chain_data directory you will find your important Chain Data..
            -Chain_state::CHAIN (for viewing)
            -Chain_data::CHAIN::chain_data (for viewing)
            -Block_times keep record of block mine times in relation to difficulty.

                                                    -- dirt_Ranch^_mgmt
    
    """
        )
        # User Input
        self.user_input = {
            "minter_label": QLabel("Enter an Auto_Miner_name: "),
            "minter_name": QLineEdit(),
            "iters_label": QLabel("Enter desired iterations.. "),
            "iters_entry": QSpinBox(),
        }

        self.user_input["minter_name"].setText("Miner")
        self.user_input["minter_name"].setMaximumWidth(120)

        self.user_input["iters_entry"].setValue(16)
        self.user_input["iters_entry"].setMaximumWidth(120)

        self.suffixes = {
            "none": QRadioButton("None"),
            "k": QRadioButton("Thousand"),
            "m": QRadioButton("Million"),
        }
        self.suffixes["none"].setChecked(True)

        opts = QHBoxLayout()
        opts.setAlignment(Qt.AlignCenter)
        for _, button in self.suffixes.items():
            opts.addWidget(button)

        items_layout = QVBoxLayout()
        for _, widget in self.user_input.items():
            items_layout.addWidget(widget)

        items_layout.addLayout(opts)
        items_layout.setAlignment(Qt.AlignHCenter)
        group = QGroupBox()
        group.setLayout(items_layout)

        # Buttons
        self.buttons = {
            "start": QPushButton("Start"),
            "quick": QPushButton("Quick Run"),
            "goodbye": QPushButton("Back"),
        }

        for key, item in self.buttons.items():
            self.button_layout.addWidget(item)
            item.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            item.setMinimumSize(52, 36)

        layout = QGridLayout()
        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 1)

        layout.addWidget(text_label, 0, 0)
        layout.addWidget(group, 1, 0)
        layout.addLayout(self.button_layout, 2, 0)
        self.setLayout(layout)
