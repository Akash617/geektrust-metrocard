class Card:
    def __init__(self, id, amount):
        self.__id = id
        self.__amount = amount
        self.__recharge_cost = 0
        self.__recharge_rate = 0.02

    def get_id(self):
        return self.__id

    def get_amount(self):
        return self.__amount

    def deduct_cost(self, cost):
        self.__amount -= cost

        if self.get_amount() < 0:
            self.__recharge_cost = self.__reset_amount()

        return self.__recharge_cost

    def __reset_amount(self):
        self.__recharge_cost = (-self.__amount * self.__recharge_rate)
        self.__amount = 0

        return self.__recharge_cost
