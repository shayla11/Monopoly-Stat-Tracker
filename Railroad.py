class Railroad:

    # Constructor
    def __init__(self, name: str):
        self.name = name
        self.base_cost = 200

        self.railroad_rent = [0, 15, 50, 100, 200]
        self.railroads_owned = 0
        self.railroad_set = False
        self.total_profit = 0

    def buy_railroad(self):
        self.railroads_owned += 1

    def opponent_landed(self):
        self.total_profit += self.railroad_rent[self.railroads_owned]
        print("Opponent landed on: {0}. +${1} (Total Gross: +${2})".format(str(self.name),
                                                                           str(self.railroad_rent[self.railroads_owned]),
                                                                           str(self.total_profit)))









