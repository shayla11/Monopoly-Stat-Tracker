from enum import Enum

from classes.Property import Property
from classes.Railroad import Railroad
from classes.Utility import Utility


class Properties(Enum):
    # Property Name, Color, Price, House/Hotel Cost, Property Values
    BALTIC_AVE = Property("Baltic Ave", "Brown", 60, 50, [4, 20, 60, 180, 320, 450])
    MEDITERRANEAN_AVE = Property("Mediterranean Ave", "Brown", 60, 50, [2, 10, 30, 90, 160, 250])

    ORIENTAL_AVE = Property("Oriental Ave", "Light Blue", 100, 50, [6, 30, 90, 270, 400, 550])
    VERMONT_AVE = Property("Vermont Ave", "Light Blue", 100, 50, [6, 30, 90, 270, 400, 550])
    CONNECTICUT_AVE = Property("Connecticut Ave", "Light Blue", 120, 50, [8, 40, 100, 300, 450, 600])

    ST_CHARLES_PLACE = Property("St. Charles Place", "Pink", 140, 100, [10, 50, 150, 450, 625, 750])
    STATES_AVE = Property("States Ave", "Pink", 140, 100, [10, 50, 150, 450, 625, 750])
    VIRGINIA_AVE = Property("Virginia Ave", "Pink", 160, 100, [12, 60, 180, 500, 700, 900])

    ST_JAMES_PLACE = Property("St. James Place", "Orange", 180, 100, [14, 70, 200, 550, 750, 950])
    TENNESSEE_AVE = Property("Tennessee Ave", "Orange", 180, 100, [14, 70, 200, 550, 750, 950])
    NEW_YORK_AVE = Property("New York Ave", "Orange", 200, 100, [16, 80, 220, 660, 800, 1000])

    KENTUCKY_AVE = Property("Kentucky Ave", "Red", 220, 150, [18, 90, 250, 700, 875, 1050])
    INDIANA_AVE = Property("Indiana Ave", "Red", 220, 150, [18, 90, 250, 700, 875, 1050])
    ILLINOIS_AVE = Property("Illinois Ave", "Red", 240, 150, [20, 100, 300, 750, 925, 1100])

    ATLANTIC_AVE = Property("Atlantic Ave", "Yellow", 260, 150, [22, 110, 330, 800, 975, 1150])
    VENTNOR_AVE = Property("Ventnor Ave", "Yellow", 260, 150, [22, 110, 330, 800, 975, 1150])
    MARVIN_GARDENS = Property("Marvin Gardens", "Yellow", 280, 150, [24, 120, 360, 850, 1025, 1200])

    PACIFIC_AVE = Property("Pacific Ave", "Green", 300, 200, [26, 130, 390, 900, 1100, 1275])
    NORTH_CAROLINA_AVE = Property("North Carolina Ave", "Green", 300, 200, [26, 130, 390, 900, 1100, 1275])
    PENNSYLVANIA_AVE = Property("Pennsylvania Ave", "Green", 320, 200, [28, 150, 450, 1000, 1200, 1400])

    PARK_PLACE = Property("Park Place", "Dark Blue", 350, 200, [35, 175, 500, 1100, 1300, 1500])
    BOARDWALK = Property("Boardwalk", "Dark Blue", 400, 200, [50, 200, 600, 1400, 1700, 2000])


class Utilities(Enum):
    ELECTRIC_COMPANY = Utility("Electric Company")
    WATER_WORKS = Utility("Water Works")
