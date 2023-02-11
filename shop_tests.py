import unittest
from shop_final_ver2 import Product

class TestProduct(unittest.TestCase):

    def setUp(self):
        self.prod1 = Product("thing", 333, 4.0)

    def test1_id(self):
        self.assertEqual(self.prod1.get_id(), 0)
        self.prod2 = Product("thing2", 333, 4.0)
        self.assertEqual(self.prod2.get_id(), 1)
        self.prod3 = Product("thing3", 333, 4.0)
        self.assertEqual(self.prod3.get_id(), 2)

    def test2_init(self):
        self.assertEqual(self.prod1.name, "thing")
        self.assertEqual(self.prod1.price, 333)
        self.assertEqual(self.prod1.rating, 4.0)

    def test3_name(self):
        self.assertEqual(self.prod1.name, "thing")

    def test4_price(self):
        self.assertEqual(self.prod1.price, 333)
        self.prod1.price = 444
        self.assertEqual(self.prod1.price, 444)


    def test4_rating(self):
        self.assertEqual(self.prod1.rating, 4.0)
        self.prod1.rating = 4.4
        self.assertEqual(self.prod1.rating, 4.4)

    def test5_is_valid_name(self):
        self.assertIsInstance(self.prod1.name, str)
        self.assertTrue(self.prod1.is_valid_name())


    def test6_is_valid_price(self):
        self.assertIsInstance(self.prod1.price, (int,float))

    def test7_is_valid_rating(self):
        self.assertIsInstance(self.prod1.rating, (int,float))



if __name__ == '__main__':
    unittest.main()