import Enums


class Property:

    # Constructor
    def __init__(self, name: str, color: str, base_cost: int, building_cost: int, property_values: list[int]):
        self.name = name
        self.color = color
        self.base_cost = base_cost
        self.building_cost = building_cost
        self.property_values = property_values

        self.current_rent = property_values[0]
        self.total_investment = 0  # running total of base cost, and house/hotel purchased
        self.total_profit = 0
        self.houses_bought = 0
        self.hotel_bought = False
        self.color_set = False

    def opponent_landed(self):
        self.total_profit += self.current_rent
        print("Opponent landed on: {0}. +${1} (Total Gross: +${2})".format(str(self.name),
                                                                           str(self.current_rent),
                                                                           str(self.total_profit)))

    def buy_house(self):
        self.houses_bought += 1
        self.current_rent = self.property_values[self.houses_bought]
        print("House Purchased! New rent value for {0} is ${1}".format(str(self.name), self.current_rent))
        if self.houses_bought > 4:
            print("Max houses purchased.")

    def sell_house(self):
        # if low on money player can sell house back for half price
        self.houses_bought -= 1
        if self.houses_bought < 0:
            print("No more houses to sell")
        else:
            self.current_rent = self.property_values[self.houses_bought]
            self.total_profit -= self.building_cost / 2  # adjust total profit if you sell back to bank

    def get_houses(self):
        return self.houses_bought

    def buy_hotel(self):
        self.hotel_bought = True
        self.current_rent = self.property_values[5]

    def sell_hotel(self):
        if not self.hotel_bought:
            print("No hotel to sell")
        else:
            self.current_rent = self.property_values[0]
            self.hotel_bought = False
            self.total_profit -= self.building_cost / 2  # adjust total profit if you sell back to bank

    def get_hotel(self):
        return self.hotel_bought

    def get_current_property_rent(self):
        if self.hotel_bought:
            self.current_rent = self.property_values[5]  # hotel value
        elif self.color_set:
            self.current_rent = self.property_values[0] * 2  # color set value
        else:
            self.current_rent = self.property_values[self.houses_bought]  # correlates to house value
        return "Current property rent is: $" + str(self.current_rent)
