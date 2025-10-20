import re

from PyQt6 import uic

from PyQt6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QWidget
import sys

import Enums
from Enums import Utilities, Railroads, Properties

RAILROADS = [Enums.Railroads.B_O_RAILROAD.name, Enums.Railroads.READING_RAILROAD.name, Enums.Railroads.PENNSYLVANIA_RAILROAD.name, Enums.Railroads.SHORT_LINE.name]
UTILITIES = [Enums.Utilities.WATER_WORKS.name, Enums.Utilities.ELECTRIC_COMPANY.name]


def get_property(name: str) -> Utilities | Railroads | Properties:
    # Remove unwanted characters: anything not alphanumeric or space
    cleaned = re.sub(r"[^\w\s]", "", name)
    # Replace spaces with underscores and convert to uppercase
    enum_name = "_".join(cleaned.strip().upper().split())

    # Check for Railroad or Utilities
    if enum_name in RAILROADS:
        board_property = Enums.Railroads[enum_name]
    elif enum_name in UTILITIES:
        board_property = Enums.Utilities[enum_name]
    else:
        board_property = Enums.Properties[enum_name]
    return board_property


class MainWindow(QMainWindow):
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
            box = PropertyBox(property_name)
            box.setFixedSize(250, 400)
            self.hbox_layout.addWidget(box)


class PropertyBox(QWidget):
    def __init__(self, name):
        super().__init__()
        uic.loadUi("propertyCard.ui", self)

        # Set the name from the box to the property
        self.propertyNameLabel.setText(name)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
