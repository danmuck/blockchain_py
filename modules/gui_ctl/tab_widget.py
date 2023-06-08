from PySide6.QtWidgets import (
    QWidget,
    QTabWidget,
    QLabel,
    QLineEdit,
    QHBoxLayout,
    QPushButton,
    QVBoxLayout,
    QTextEdit,
)

from modules.gui_ctl.chain.chain_ctl import (
    get_chain_string,
    get_wallet_string,
    get_joined_data,
)


class TextEdit(QWidget):
    def __init__(self, with_buttons: bool = False):
        super().__init__()
        self.setWindowTitle("QTextEdit")
        self.main_button = QPushButton("Refresh Data")

        self.text_edit = QTextEdit()
        main_layout = QVBoxLayout()

        # buttons
        if with_buttons:
            current_text_button = QPushButton("Print Current Text")
            current_text_button.clicked.connect(self.current_text_button_clicked)

            copy_button = QPushButton("Copy")
            copy_button.clicked.connect(self.text_edit.copy)

            cut_button = QPushButton("Cut")
            cut_button.clicked.connect(self.text_edit.cut)

            paste_button = QPushButton("Paste")
            paste_button.clicked.connect(self.text_edit.paste)

            undo_button = QPushButton("Undo")
            undo_button.clicked.connect(self.text_edit.undo)

            redo_button = QPushButton("Redo")
            redo_button.clicked.connect(self.text_edit.redo)

            set_plain_text_button = QPushButton("Set Plain Text")
            set_plain_text_button.clicked.connect(
                lambda: self.set_plain_text("sometext")
            )

            set_html_button = QPushButton("Set HTML")
            set_html_button.clicked.connect(self.set_html)

            clear_button = QPushButton("Clear")
            clear_button.clicked.connect(self.text_edit.clear)

            # Layout
            btn_layout = QHBoxLayout()
            btn_layout.addWidget(current_text_button)
            btn_layout.addWidget(copy_button)
            btn_layout.addWidget(cut_button)
            btn_layout.addWidget(paste_button)
            btn_layout.addWidget(undo_button)
            btn_layout.addWidget(redo_button)
            btn_layout.addWidget(set_plain_text_button)
            btn_layout.addWidget(set_html_button)
            btn_layout.addWidget(clear_button)

            main_layout.addLayout(btn_layout)
        else:
            self.text_edit.setReadOnly(True)
            refresh_button = self.main_button
            main_layout.addWidget(refresh_button)

        main_layout.addWidget(self.text_edit)

        self.setLayout(main_layout)

    # slots
    def current_text_button_clicked(self):
        print(self.text_edit.toPlainText())

    def set_plain_text(self, text: str):
        self.text_edit.setPlainText(text)

    def set_html(self):
        self.text_edit.setHtml("<h1>Header</h><p>Paragraph of text</p><br><hr>")


class TabWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTabWidget")

        tab_widget = QTabWidget(self)

        # Initialize Tabs
        self.chain_tab = TextEdit()
        self.notes_tab = TextEdit(True)
        self.wallet_tab = TextEdit()

        # Add Tabs
        tab_widget.addTab(self.chain_tab, "Chain")
        tab_widget.addTab(self.wallet_tab, "Wallet")
        tab_widget.addTab(self.notes_tab, "Notes")

        layout = QVBoxLayout()
        layout.addWidget(tab_widget)

        self.setLayout(layout)

        self.chain_tab.main_button.clicked.connect(lambda: self.print_chain())
        self.wallet_tab.main_button.clicked.connect(lambda: self.print_wallet())

    # Slots
    def print_chain(self):
        chain_str = get_chain_string()
        self.chain_tab.set_plain_text(chain_str)

    def print_wallet(self):
        wallet_str = get_wallet_string()
        self.wallet_tab.set_plain_text(wallet_str)

    def print_joined(self):
        joined_data = get_joined_data()
        self.wallet_tab.set_plain_text(joined_data)
