import Enums
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QHBoxLayout, QPushButton, QDialog, QVBoxLayout, QLineEdit, \
    QFormLayout, QDialogButtonBox
import sys


def set_properties() -> str:
    # lol are baltic and med purple now??
    #baltic_ave_property = Property("Baltic Ave", "Brown", 60, 50, 50, [4, 20, 60, 180, 320, 450])

    return "hi"

class Window(QDialog):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("QDialog")
        dialogLayout = QVBoxLayout()
        formLayout = QFormLayout()
        formLayout.addRow("Name:", QLineEdit())
        formLayout.addRow("Age:", QLineEdit())
        formLayout.addRow("Job:", QLineEdit())
        formLayout.addRow("Hobbies:", QLineEdit())
        dialogLayout.addLayout(formLayout)
        buttons = QDialogButtonBox()
        buttons.setStandardButtons(
            QDialogButtonBox.StandardButton.Cancel
            | QDialogButtonBox.StandardButton.Ok
        )
        dialogLayout.addWidget(buttons)
        self.setLayout(dialogLayout)

#if __name__ == '__main__':
    #baltic = Enums.Properties.BALTIC_AVE.value
    #print(baltic.name)
    #print(baltic.hotel_bought)
    #baltic.buy_hotel()
    #print(baltic.get_hotel())
    #print(baltic.get_current_property_rent())
    #baltic.sell_hotel()
    #baltic.opponent_landed()
    #baltic.opponent_landed()
    #baltic.opponent_landed()
    #baltic.buy_house()
    #baltic.opponent_landed()
    #baltic.opponent_landed()
    #print(baltic.get_current_property_rent())


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


