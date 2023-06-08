from PySide6.QtWidgets import (
    QWidget,
    QStackedWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QSizePolicy,
    QGridLayout,
    QApplication,
    QMessageBox,
    QInputDialog,
)

from modules.gui_ctl.chain.chain_ctl import chain_init


class WelcomeMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.button_layout = QVBoxLayout()
        self.buttons = {}

        # Items
        text_label = QLabel(
            "    -- Welcome to dirt_Ranch^_ ..! \nWhich wagon you ridin' today?"
        )
        custom_chain_btn = QPushButton("Enter Chain_id")
        default_chain_btn = QPushButton("Master::chain_id=0 (default)")
        autorun_btn = QPushButton("Advanced_Mode_Autorun")
        goodbye_btn = QPushButton("Goodbye")
        testing_btn = QPushButton("TESTING")
        self.buttons = {
            "custom_chain": custom_chain_btn,
            "default_chain": default_chain_btn,
            "autorun": autorun_btn,
            "goodbye": goodbye_btn,
            "testing": testing_btn,
        }
        for key, item in self.buttons.items():
            self.button_layout.addWidget(item)
            item.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.handle_button_clicks(key)
            item.setMinimumSize(52, 40)

        layout = QGridLayout()
        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 1)

        layout.addWidget(text_label, 0, 0)
        layout.addLayout(self.button_layout, 1, 0)
        self.setLayout(layout)

    def handle_button_clicks(self, key):
        match key:
            case "testing":
                self.buttons[key].clicked.connect(QApplication.quit)

            case "default_chain":
                self.buttons[key].clicked.connect(lambda: chain_init(0))

            case "custom_chain":

                def get_id():
                    title = "Custom Chain_id"
                    text = "Enter Chain_id: "
                    default_value = 0
                    chain_id, ok_pressed = QInputDialog.getInt(
                        self, title, text, default_value, 0
                    )
                    if ok_pressed:
                        if not chain_init(chain_id, False).sync_mc:
                            print("OFF MASTER -- NEEDS MENU")
                        QMessageBox.information(
                            self, "Result", f"On Chain: Chain_{chain_id}"
                        )

                self.buttons[key].clicked.connect(get_id)
