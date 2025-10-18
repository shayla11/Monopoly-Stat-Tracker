import re

from PyQt6 import uic

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QHBoxLayout
import sys

import Enums
from Enums import Utilities, Railroads, Properties

RAILROADS = [Enums.Railroads.B_O_RAILROAD.name, Enums.Railroads.READING_RAILROAD.name, Enums.Railroads.PENNSYLVANIA_RAILROAD.name, Enums.Railroads.SHORT_LINE.name]
UTILITIES = [Enums.Utilities.WATER_WORKS.name, Enums.Utilities.ELECTRIC_COMPANY.name]


def get_property(name: str) -> Utilities | Railroads | Properties:
    # Remove unwanted characters: anything not alphanumeric or space
    cleaned = re.sub(r"[^\w\s]", "", name)
    # Replace spaces with underscores and convert to uppercase
    enum_name =  "_".join(cleaned.strip().upper().split())

    # Check for Railroad or Utilities
    if enum_name in RAILROADS:
        board_property = Enums.Railroads[enum_name]
    elif enum_name in UTILITIES:
        board_property = Enums.Utilities[enum_name]
    else:
        board_property = Enums.Properties[enum_name]
    return board_property


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
        board_property = get_property(property_name)  # Convert to enum

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
