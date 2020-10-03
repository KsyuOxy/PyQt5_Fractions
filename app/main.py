import sys
from models.fraction import Fraction
from PyQt5.QtWidgets import QApplication
from gui.win import MainWindowF

app = QApplication([])
win = MainWindowF()
win.show()

sys.exit(app.exec())
