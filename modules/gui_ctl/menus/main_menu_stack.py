from PySide6.QtWidgets import (
    QWidget,
    QStackedWidget,
    QVBoxLayout,
)

from modules.gui_ctl.menus.main_menu.main_menu import MainMenu
from modules.gui_ctl.menus.main_menu.office import OfficeMenu
from modules.gui_ctl.tab_widget import TabWidget


class MainMenuStack(QWidget):
    def __init__(self, parent: QStackedWidget, tabs: TabWidget):
        super().__init__(parent)
        self.parent = parent
        self.tabs = tabs
        # Create a stacked widget
        self.stacked_widget = QStackedWidget()

        # Menus
        self.menus = {
            "main": MainMenu(),
            "office": OfficeMenu()
        }

        # Add Menus and set initial
        for _, menu in self.menus.items():
            self.stacked_widget.addWidget(menu)
        self.stacked_widget.setCurrentWidget(self.menus["main"])

        # Set the layout for the widget
        layout = QVBoxLayout(self)
        layout.addWidget(self.stacked_widget)

        # handle connections
        self.handle_main_menu()

    def handle_main_menu(self):
        for key, button in self.menus["main"].buttons.items():
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
                    button.clicked.connect(
                        lambda: self.parent.setCurrentWidget(self.parent.widget(2))
                    )

                case "goodbye":
                    button.clicked.connect(lambda: print())
                    button.clicked.connect(
                        lambda: self.parent.setCurrentWidget(self.parent.widget(2))
                    )
