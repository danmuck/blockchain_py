from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QSizePolicy, QGridLayout


class MainMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.button_layout = QVBoxLayout()
        self.buttons = {}

        # Items
        text_label = QLabel("    -- Where to next?")
        office_btn = QPushButton("Office")
        workshop_btn = QPushButton("Workshop")
        crafting_bench_btn = QPushButton("Crafting Bench")
        throw_dirt_btn = QPushButton("Throw $DIRT")
        trading_post_btn = QPushButton("Trading Post")
        message_board_btn = QPushButton("Message Board")
        the_mound_btn = QPushButton("The Mound")
        the_pit_btn = QPushButton("The Pit")
        wallet_opts_btn = QPushButton("Wallet Options")
        goodbye_btn = QPushButton("Back")

        self.buttons = {
            "office": office_btn,
            "workshop": workshop_btn,
            "craft": crafting_bench_btn,
            "throw": throw_dirt_btn,
            "trade": trading_post_btn,
            "message": message_board_btn,
            "mound": the_mound_btn,
            "pit": the_pit_btn,
            "wallet": wallet_opts_btn,
            "goodbye": goodbye_btn,
        }
        for key, item in self.buttons.items():
            self.button_layout.addWidget(item)
            item.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            item.setMinimumSize(52, 36)

        layout = QGridLayout()
        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 1)

        layout.addWidget(text_label, 0, 0)
        layout.addLayout(self.button_layout, 1, 0)
        self.setLayout(layout)
