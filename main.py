from PyQt6 import uic

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QHBoxLayout
import sys

import Enums

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.owned_properties: list[Enums.Properties] = []
        uic.loadUi("firstExample.ui", self)

        self.scrollContent = self.scrollArea.widget()
        self.hbox_layout = QHBoxLayout(self.scrollContent)
        self.scrollContent.setLayout(self.hbox_layout)

        # Connect the buy property button
        self.buyPropertyButton.clicked.connect(self.add_property_box)

    def add_property_box(self):
        # Get name of property added
        property_name = self.propertySelectName.currentText()
        enum_name = property_name.upper().replace(" ", "_")  # Convert to enum
        board_property = Enums.Properties[enum_name]

        # If property already owned, skip adding a widget
        if board_property.value.owned:
            print(board_property.name + " already own!")
            return

        # Else proceed with adding the property to the own list and adding a new widget box
        else:
            board_property.value.owned = True
            self.owned_properties.append(board_property.name)
            print("Owned Properties" + str(self.owned_properties))
            label = QLabel(f"{property_name}")
            label.setFixedSize(250, 400)
            label.setStyleSheet("background-color: lightblue; border: 1px solid black; padding: 5px;")
            self.hbox_layout.addWidget(label)


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
