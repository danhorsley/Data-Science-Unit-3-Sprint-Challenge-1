#!/usr/bin/env python
import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS

class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)
    
    def test_default_product_weight(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)
        
    def test_steal_explode(self):
        """Tests default product steal 
        and explode as they should."""
        prod = Product('Test Product')
        test_steal = prod.price / prod.weight
        
        if test_steal < 0.5:
            self.assertEqual(prod.stealability(), "Not so stealable...")

        elif 0.5 <= test_steal < 1:
            self.assertEqual(prod.stealability(), "Kinda stealable.")

        else:
            self.assertEqual(prod.explode(), "Very stealable!")

        if test_explode < 10:
            self.assertEqual(prod.explode(), "...fizzle.")

        elif test_explode >= 10 and test_explode < 50:
            self.assertEqual(prod.stealability(), "...boom!")

        else:
            self.assertEqual(prod.explode(), "...BABOOM!!")
            
class AcmeReportTests(unittest.TestCase):
  
  def test_default_num_products(self):
    prods = generate_products()
    self.assertEqual(len(prods),30)
    
    def test_legal_names(self):
        prods = generate_products()
        for prod in prods:
            split=prod.name.rsplit(' ', 1)
            first_bit=split[0]
            second_bit=split[1]
            bool_first=(first_bit in(ADJECTIVES))
            bool_second=(second_bit in (NOUNS))
            self.assertEqual(bool_first, True)
            self.assertEqual(bool_second, True)