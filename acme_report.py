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
    details=[]
    for i in range(len(product_list)):
        prod = product_list[i]
        info = [prod.name, prod.price, prod.weight, prod.flammability]
        details.append(info)
    def av(l):
        return round(sum(l)/len(l),2)
    names = len(set([x[0] for x in details]))
    prices = av([x[1] for x in details])
    weights = av([x[2] for x in details])
    flammability = av([x[3] for x in details])
    scores = [names, prices, weights, flammability]
    labels = ['no. unique names','average price','average weight','average flammability']
    print("-------------------------------")
    print(".Product Report")
    print(".number of unique names :", names)
    print(".average price :", prices)
    print(".average weight :", weights)
    print(".average flammability", flammability)
    print("-------------------------------")

    return_dict=dict(zip(labels, scores))
 
    return return_dict

if __name__ == '__main__':
    inventory_report(generate_products())
