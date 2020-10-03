from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox

from models.fraction import Fraction


class MainWindowF(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.__win = uic.loadUi('../templates/Qt_design.ui')

    def show(self) -> None:  # -> mainloop()
        self.__win.show()
