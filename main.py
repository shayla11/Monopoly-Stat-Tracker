import re

from PyQt6 import uic

from PyQt6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QWidget
import sys

import Enums
from Enums import Utilities, Railroads, Properties

RAILROADS_LIST = [Enums.Railroads.B_O_RAILROAD.name, Enums.Railroads.READING_RAILROAD.name,
                  Enums.Railroads.PENNSYLVANIA_RAILROAD.name, Enums.Railroads.SHORT_LINE.name]
UTILITIES_LIST = [Enums.Utilities.WATER_WORKS.name, Enums.Utilities.ELECTRIC_COMPANY.name]


def get_property(name: str) -> Utilities | Railroads | Properties:
    # Remove unwanted characters: anything not alphanumeric or space
    cleaned = re.sub(r"[^\w\s]", "", name)
    # Replace spaces with underscores and convert to uppercase
    enum_name = "_".join(cleaned.strip().upper().split())

    # Check for Railroad or Utilities
    if enum_name in RAILROADS_LIST:
        board_property = Enums.Railroads[enum_name]
    elif enum_name in UTILITIES_LIST:
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
        global box
        property_name = self.propertySelectName.currentText()
        board_property = get_property(property_name)  # Convert to enum

        # If property already owned, skip adding a widget
        if board_property.value.owned:
            print(board_property.name + " already own!")
        else:
            # Else proceed with adding the property to the own list and adding a new widget box
            board_property.value.owned = True
            self.owned_properties.append(board_property.name)
            print("Owned Properties" + str(self.owned_properties))

            # Create box based on property, railroad, or utility
            if board_property.name in UTILITIES_LIST:
                # box = UtilityCardBox()
                print("utility card not ready yet")
            elif board_property.name in RAILROADS_LIST:
                # box = RailroadCardBox()
                print("railroad card not ready yet")
            else:
                box = PropertyCardBox(property_name, board_property)
                box.setFixedSize(250, 400)  # Move outside else when railroad and utility is ready
                self.hbox_layout.addWidget(box)  # Move outside else when railroad and utility is ready


class PropertyCardBox(QWidget):
    def __init__(self, name: str, board_property: Utilities | Railroads | Properties):
        super().__init__()
        uic.loadUi("propertyCard.ui", self)

        self.property = board_property.value
        self.rent = 0
        self.total_profit = 0
        # Set the name of the box to the property name
        self.propertyNameLabel.setText(name)
        # Set Color

        # Connect buttons to methods
        self.housesOwnedSpinBox.valueChanged.connect(self.update_rent)
        self.hotelOwnedCheckBox.clicked.connect(self.toggle_hotel)
        self.opponentLandedButton.clicked.connect(self.add_rent_to_total)

        # Set initial rent
        self.update_rent()

    def toggle_hotel(self):
        self.hotelOwnedCheckBox = not self.hotelOwnedCheckBox
        # Reset houses to 0 if hotel is turned on
        if self.hotelOwnedCheckBox:
            self.housesOwnedSpinBox.setValue(0)
        self.update_rent()

    def update_rent(self):
        if not self.hotelOwnedCheckBox:
            self.rent = self.property.property_values[5]  # Hotel rent
        else:
            house_count = self.housesOwnedSpinBox.value()
            if house_count > 4:
                print("Max of 4 houses reached!")
                self.housesOwnedSpinBox.setValue(4)
                house_count = 4
            self.rent = self.property.property_values[house_count]  # Grab house rent based on count

        self.currentRentAmountlabel.setText(f"${self.rent}")

    def add_rent_to_total(self):
        self.total_profit = self.total_profit + self.rent
        self.totalProfitAmountLabel.setText(f"${self.total_profit}")


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
