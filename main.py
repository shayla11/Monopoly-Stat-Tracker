import re

from PyQt6 import uic
from PyQt6.QtGui import QPixmap

from PyQt6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QWidget
import sys

import Enums
from Enums import Utilities, Properties
from classes.Railroad import Railroad

UTILITIES_LIST = [Enums.Utilities.WATER_WORKS.name, Enums.Utilities.ELECTRIC_COMPANY.name]


def get_property(name: str) -> Utilities | Railroad | Properties:
    # Remove and replace unwanted characters and make uppercase
    cleaned = re.sub(r"[^\w\s]", "", name)
    enum_name = "_".join(cleaned.strip().upper().split())

    # Check for Railroad or Utilities
    if enum_name.__contains__("RAILROAD"):
        board_property = Railroad("Railroad")
    elif enum_name in UTILITIES_LIST:
        board_property = Enums.Utilities[enum_name].value
    else:
        board_property = Enums.Properties[enum_name].value
    return board_property


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.owned_properties: list[Enums.Properties] = []
        uic.loadUi("UIs/MainWindow.ui", self)

        self.scrollContent = self.scrollArea.widget()
        self.hbox_layout = QHBoxLayout(self.scrollContent)
        self.scrollContent.setLayout(self.hbox_layout)

        # Connect the buy property button
        self.buyPropertyButton.clicked.connect(self.add_box)

        self.railroad_is_owned = False

    def add_box(self):
        # Get name of property added
        property_name = self.propertySelectName.currentText()
        board_property = get_property(property_name)  # Convert to enum

        # If property already owned, skip adding a widget
        if (type(board_property) == Railroad and self.railroad_is_owned) or board_property.owned:
            print(board_property.name + " already own!")

        # Else proceed with adding the property to the own list and adding a new widget box
        else:
            board_property.owned = True
            self.owned_properties.append(board_property.name)
            print("Owned Properties" + str(self.owned_properties))

            # Create box based on property, railroad, or utility
            if board_property.name in UTILITIES_LIST:
                # box = UtilityCardBox()
                print("utility card not ready yet")
            elif board_property.name.__contains__("Railroad"):
                self.railroad_is_owned = True
                box = RailroadCardBox(board_property)
                box.setFixedSize(250, 400)
                self.hbox_layout.addWidget(box)
            else:
                box = PropertyCardBox(property_name, board_property)
                box.setFixedSize(250, 400)  # Move outside else when railroad and utility is ready
                self.hbox_layout.addWidget(box)  # Move outside else when railroad and utility is ready


class PropertyCardBox(QWidget):
    def __init__(self, name: str, board_property: Properties):
        super().__init__()
        uic.loadUi("UIs/propertyCard.ui", self)

        self.property = board_property
        self.rent = 0
        self.total_profit = 0
        # Set the name of the box to the property name
        self.propertyNameLabel.setText(name)
        # Set Color
        self.propertyNameLabel.setStyleSheet(f"background-color: {board_property.color}; border: 3px solid black;")

        # Connect buttons to methods
        self.housesOwnedSpinBox.valueChanged.connect(self.update_rent)
        self.hotelOwnedCheckBox.clicked.connect(self.toggle_hotel)
        self.opponentLandedButton.clicked.connect(self.add_rent_to_total)

        # Set initial rent (Skip for railroads and utilities)
        if not name.__contains__("Railroad"):
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
                print("Max houses reached!")
                self.housesOwnedSpinBox.setValue(4)
                house_count = 4
            self.rent = self.property.property_values[house_count]

        self.currentRentAmountlabel.setText(f"${self.rent}")

    def add_rent_to_total(self):
        self.total_profit = self.total_profit + self.rent
        self.totalProfitAmountLabel.setText(f"${self.total_profit}")


class RailroadCardBox(QWidget):
    def __init__(self, board_property: Railroad):
        super().__init__()
        uic.loadUi("UIs/railroadCard.ui", self)

        self.railroad = board_property
        self.rent = 0
        self.total_profit = 0

        # Set Railroad Pictures
        self.pixmap = QPixmap('railroad.png')
        self.railroadPic1.setPixmap(self.pixmap)
        self.railroadPic2.setPixmap(self.pixmap)
        self.railroadPic3.setPixmap(self.pixmap)
        self.railroadPic4.setPixmap(self.pixmap)

        self.railroadPic1.setScaledContents(True)
        self.railroadPic2.setScaledContents(False)
        self.railroadPic3.setScaledContents(False)
        self.railroadPic4.setScaledContents(False)

        self.railroadOwnedSpinBox.setValue(1)

        # Connect buttons to methods
        self.railroadOwnedSpinBox.valueChanged.connect(self.update_rent)
        self.railroadOwnedSpinBox.valueChanged.connect(self.update_railroad_logos)
        self.opponentLandedButton.clicked.connect(self.add_rent_to_total)

        # Set initial rent
        self.update_rent()

    def update_railroad_logos(self):
        railroad_count = self.railroadOwnedSpinBox.value()
        # Set train pictures
        if railroad_count == 0:
            self.railroadPic1.setScaledContents(False)
            self.railroadPic2.setScaledContents(False)  # Off
            self.railroadPic3.setScaledContents(False)  # Off
            self.railroadPic4.setScaledContents(False)  # Off
        if railroad_count == 1:
            self.railroadPic1.setScaledContents(True)
            self.railroadPic2.setScaledContents(False)  # Off
            self.railroadPic3.setScaledContents(False)  # Off
            self.railroadPic4.setScaledContents(False)  # Off
        if railroad_count == 2:
            self.railroadPic2.setScaledContents(True)
            self.railroadPic3.setScaledContents(False)  # Off
            self.railroadPic4.setScaledContents(False)  # Off
        if railroad_count == 3:
            self.railroadPic3.setScaledContents(True)
            self.railroadPic4.setScaledContents(False)  # Off
        if railroad_count == 4:
            self.railroadPic4.setScaledContents(True)

    def update_rent(self):
        railroad_count = self.railroadOwnedSpinBox.value()
        if railroad_count > 4:
            print("Max railroads reached!")
            self.railroadOwnedSpinBox.setValue(4)
            railroad_count = 4
        self.rent = self.railroad.railroad_rent[railroad_count]  # Grab house rent based on count

        self.currentRentAmountlabel.setText(f"${self.rent}")

    def add_rent_to_total(self):
        self.total_profit = self.total_profit + self.rent
        self.totalProfitAmountLabel.setText(f"${self.total_profit}")


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
