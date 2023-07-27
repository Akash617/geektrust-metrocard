class Prices:
    def __init__(self):
        self.__price_list = {"ADULT": 200, "SENIOR_CITIZEN": 100, "KID": 50}

    def get_price(self, type, return_trip=False):
        if return_trip:
            return (self.__price_list[type] / 2)

        return self.__price_list[type]

    def get_discount(self, type, return_trip=False):
        if return_trip:
            return (self.__price_list[type] / 2)

        return 0
