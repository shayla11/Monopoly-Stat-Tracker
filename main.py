from PyQt6 import uic

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QHBoxLayout
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("firstExample.ui", self)

        self.scrollContent = self.scrollArea.widget()  # scrollAreaWidgetContents
        self.hbox_layout = QHBoxLayout(self.scrollContent)
        self.scrollContent.setLayout(self.hbox_layout)

        # Connect the button
        self.buyPropertyButton.clicked.connect(self.add_property_box)

        self.counter = 0

    def add_property_box(self):
        label = QLabel(f"Box {self.counter}")
        label.setFixedSize(250, 400)  # ✅ Fixed size
        label.setStyleSheet("background-color: lightblue; border: 1px solid black; padding: 5px;")
        self.hbox_layout.addWidget(label)
        self.counter += 1


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


