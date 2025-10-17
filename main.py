from PyQt6 import uic

from PyQt6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLineEdit, QFormLayout, QDialogButtonBox, QMainWindow
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("firstExample.ui", self)  # Load the .ui file into this window

if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())



    # Utilize QtPy to figure out how to make a UI that has some stats and buttons that will
    # 1. Allow player to say that bought a property
    # 2. Buy Sell Houses / Hotels
    # 3. Log Opponent landed on their property
    # 4. Keep track of total profit from owned properties
    # May make some github project issues to track these!

    # will also need to be definityive on how the total profit will be. maybe a mode to start from price put in, or pure profits. Or Both!
    # will also need to deciede will the method have barriers for over buying and over selling properites? or will buttons be disabled. need to exeperiment with QtPy


