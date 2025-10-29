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
        self.owned = False
