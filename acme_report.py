#!/usr/bin/env python

import random
from acme import Product
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

def generate_products(n=30):
    """
    name should be a random adjective from ['Awesome', 'Shiny',
    'Impressive', 'Portable', 'Improved'] followed by a space and
    then a random noun from ['Anvil', 'Catapult' 'Disguise' 'Mousetrap',
    '???'], e.g. 'Awesome Anvil' and Portable Catapult' are both possible
    price and weight should both be from 5 to 100
    flammability should be from 0.0 to 2.5 (floats)
    """
    try:
        product_list = []
        for i in range(n):
            adj = random.choice(ADJECTIVES)
            noun = random.choice(NOUNS)
            name = adj + ' ' + noun
            weight = random.randint(5, 100)
            price = random.randint(5, 100)
            flamm = random.uniform(0.0, 2.5)
            _ = Product(name, price, weight, flamm)
            product_list.append(_)
        return product_list
    except ValueError:
        print("Oops you did it again")

def inventory_report(product_list):
    """
    takes a list of products, and prints a "nice" summary
    """
    for i in range(len(product_list)):
        prod = product_list[i]
        print("------------------")
        print(".product number", i+1)
        print(".name :", prod.name)
        print(".price :", prod.price)
        print(".weight :", prod.weight)
        print(".flammability :", round(prod.flammability, 2))
        print(".identifier :", prod.identifier)

if __name__ == '__main__':
    inventory_report(generate_products())
