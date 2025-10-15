class Utility:

    # Constructor
    def __init__(self, name: str):
        self.name = name

        self.base_cost = 150
        self.utility_rent = 0
        self.utilities_owned = 0
        self.utilities_set = False
        self.total_profit = 0

    def buy_utility(self):
        self.utilities_owned += 1
        print("{0} was bought!".format(self.name))

    def sell_utility(self):
        if self.utilities_owned == 0:
            print("No owned utilities to sell")
        else:
            self.utilities_owned -= 1

    def opponent_landed(self, opponent_role: int):
        # Set utility rent based on opponent role
        if self.utilities_set:
            self.utility_rent = 10 * opponent_role
        else:
            self.utility_rent = 4 * opponent_role

        self.total_profit += self.utility_rent
        print("Opponent landed on: {0} and rolled a {1} earning you ${2} (Total Gross: +${3})".format(str(self.name), str(opponent_role),
                                                                           str(self.utility_rent),
                                                                           str(self.total_profit)))

