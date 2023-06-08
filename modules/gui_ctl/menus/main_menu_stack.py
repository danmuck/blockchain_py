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

from modules.gui_ctl.menus.main_menu.main_menu import MainMenu


class MainMenuStack(QWidget):
    def __init__(self, parent: QStackedWidget = None):
        super().__init__(parent)
        self.parent = parent
        # Create a stacked widget
        self.stacked_widget = QStackedWidget()

        # Menus
        self.main_menu = MainMenu()

        # Add Menus and set initial
        self.stacked_widget.addWidget(self.main_menu)

        self.stacked_widget.setCurrentWidget(self.main_menu)

        # Set the layout for the widget
        layout = QVBoxLayout(self)
        layout.addWidget(self.stacked_widget)

        # handle connections
        self.handle_main_menu_slots()
        self.handle_main_menu(self.main_menu.buttons)

    def handle_main_menu_slots(self):
        self.main_menu.buttons["wallet"].clicked.connect(
            lambda: self.parent.setCurrentWidget(self.parent.widget(2))
        )
        self.main_menu.buttons["goodbye"].clicked.connect(
            lambda: self.parent.setCurrentWidget(self.parent.widget(2))
        )

    def handle_main_menu(self, buttons):
        for key, button in buttons.items():
            match key:
                case "office":
                    pass

                case "workshop":
                    pass

                case "craft":
                    pass

                case "throw":
                    pass

                case "trade":
                    pass

                case "message":
                    pass

                case "mound":
                    pass

                case "pit":
                    pass

                case "wallet":
                    pass

                case "goodbye":
                    button.clicked.connect(lambda: print())
