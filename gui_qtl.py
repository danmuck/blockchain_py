import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QFont
from modules.gui_ctl.main_window import MainWindow

app = QApplication(sys.argv)

font = app.font()
font.setFamily("Monospace")
font.setStyleHint(QFont.Monospace)
font.setPointSize(12)
app.setFont(font)

window = MainWindow(app)
# window = MainWindow()
window.show()

app.exec()
