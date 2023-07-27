import unittest
import prices, card

class Test_prices(unittest.TestCase):
    def test_adult_no_return(self):
        price_list = prices.Prices()
        self.assertEqual(price_list.get_price("ADULT"), 200)

    def test_senior_return(self):
        price_list = prices.Prices()
        self.assertEqual(price_list.get_price("SENIOR_CITIZEN", True), 50)

    def test_kid_no_return(self):
        price_list = prices.Prices()
        self.assertEqual(price_list.get_price("KID"), 50)

    def test_kid_return(self):
        price_list = prices.Prices()
        self.assertEqual(price_list.get_price("KID", True), 25)


class Test_card(unittest.TestCase):
    def test_correct_details_stored(self):
        card1 = card.Card("MC1", 100)
        card2 = card.Card("MC2", 250)

        self.assertEqual(card1.get_amount(), 100)
        self.assertEqual(card1.get_id(), "MC1")
        self.assertEqual(card2.get_amount(), 250)
        self.assertEqual(card2.get_id(), "MC2")


    def test_deduct_cost_no_recharge(self):
        card1 = card.Card("MC1", 100)
        recharge_cost = card1.deduct_cost(50)

        self.assertEqual(recharge_cost, 0)
        self.assertEqual(card1.get_amount(), 50)

    def test_deduct_cost_with_recharge(self):
        card1 = card.Card("MC1", 100)
        recharge_cost = card1.deduct_cost(200)

        self.assertEqual(recharge_cost, 2)
        self.assertEqual(card1.get_amount(), 0)

if __name__ == '__main__':
    unittest.main()