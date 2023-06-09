from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QRadioButton,
    QSpinBox,
    QLineEdit,
)


class CraftingBenchMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.button_layout = QVBoxLayout()
        self.buttons = {}

        # Items
        text_label = QLabel(
            """
    -- Welcome to the Crafting Bench::[No_funs]

        No_funs are a very basic implementation of NFTs or Non-Fungible Tokens...
            with every iteration you have the chance to land a No_fun...
            ... and in turn, mine a block into the current chain!
            ... No_funs carry traits with a chance to land a rare void state.
        
        Currently all No_funs are written into blocks::chain_data with that 
        expected to change upon the implementation of txns and $DIRT.
        
        All Minter_data can be found in the [minter_data] directory once a 
        minter has been initialized along with your respective Chain_data
        files in the [chain_data] directory.

                                                    -- dirt_Ranch^_mgmt
    """
        )
        # User Input
        self.user_input = {
            "minter_label": QLabel("Enter a Minter_name: "),
            "minter_name": QLineEdit(),
            "iters_label": QLabel("Enter desired iterations.. "),
            "iters_entry": QSpinBox(),
        }

        self.user_input["minter_name"].setText("Minter")
        self.user_input["minter_name"].setMaximumWidth(120)

        self.user_input["iters_entry"].setValue(16)
        self.user_input["iters_entry"].setMaximum(999999)
        self.user_input["iters_entry"].setMaximumWidth(120)

        self.suffixes = {
            "1": QRadioButton("None"),
            "1_000": QRadioButton("Thousand"),
            "1_000_000": QRadioButton("Million"),
        }
        self.suffixes["1_000"].setChecked(True)

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
