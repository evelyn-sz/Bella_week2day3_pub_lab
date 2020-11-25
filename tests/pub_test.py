import unittest
from src.pub import Pub #capital P because class names always begin with capital letter
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):#these parameters tell python this is a test, and not a normal class
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.drink = Drink("Mojito", 8.00)
        self.customer_1 = Customer("Skye", 50.00, 19)
        self.customer_2 = Customer("David", 25.00, 17) 

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_till_updated(self):
        self.assertEqual(108, self.pub.add_to_till(self.drink))

    def test_pub_checks_age(self):
        self.assertEqual(True, self.pub.check_age(self.customer_1))
        self.assertEqual(False, self.pub.check_age(self.customer_2))