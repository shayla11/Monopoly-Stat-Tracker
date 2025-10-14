import Enums


def set_properties() -> str:
    # lol are baltic and med purple now??
    #baltic_ave_property = Property("Baltic Ave", "Brown", 60, 50, 50, [4, 20, 60, 180, 320, 450])

    return "hi"

if __name__ == '__main__':
    baltic = Enums.Properties.BALTIC_AVE.value
    #print(baltic.name)
    #print(baltic.hotel_bought)
    #baltic.buy_hotel()
    #print(baltic.get_hotel())
    print(baltic.get_current_property_rent())
    baltic.sell_hotel()
    baltic.opponent_landed()
    baltic.opponent_landed()
    baltic.opponent_landed()
    baltic.buy_house()
    baltic.opponent_landed()
    baltic.opponent_landed()
    print(baltic.get_current_property_rent())

    # Utilize QtPy to figure out how to make a UI that has some stats and buttons that will
    # 1. Allow player to say that bought a property
    # 2. Buy Sell Houses / Hotels
    # 3. Log Opponent landed on their property
    # 4. Keep track of total profit from owned properties
    # May make some github project issues to track these!


