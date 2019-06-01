#!/usr/bin/env python
import random
class Product:

    def __init__(
            self,
            name,
            price=10,
            weight=20,
            flammability=0.5,
            identifier=random.randint(1000000, 10000000)):
        self.name = str(name)
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        """
        calculates the price divided by the weight, and then
        returns a message: if the ratio is less than 0.5 return
        "Not so stealable...", if it is greater or equal to 0.5
        but less than 1.0 return "Kinda stealable.", and otherwise
        return "Very stealable!"
        """
        try:
            
            self.stealratio = self.price / self.weight
            if self.stealratio < 0.5:
                a="Not so stealable..."
                print(a)
            elif self.stealratio < 1 and self.stealratio >= 0.5:
                a="Kinda stealable."
                print(a)
            else:
                a="Very stealable!"
                print(a)
        except ValueError:
            self.stealratio=None
            "Oops!  That was not a valid weight or price.  Try again..."
        return a 


    def explode(self):
        """
        calculates the flammability times the weight, and then
        returns a message: if the product is less than 10 return
        '...fizzle.', if it is greater or equal to 10 but less than
        50 return "...boom!", and otherwise return "...BABOOM!!".
        """
        self.flamratio = self.flammability * self.weight
        try:
            if self.flamratio < 10:
                b="...fizzle."
                print(b)
            elif self.flamratio >= 10 and self.flamratio < 50:
                b="...boom!"
                print(b)
            else:
                b="...BABOOM!!"
                print(b)
        except ValueError:
            print("Oops! That was not a valid weight or\
                   flammability.  Try again...")
        return b

class BoxingGlove(Product):
    #import random
    def __init__(
        self,
        name,
        price=10,
        weight=10,
        flammability=0.5,
        identifier=random.randint(1000000, 10000000)
                    ):
            super().__init__(
                name=name,
                price=price,
                weight=weight,
                flammability=flammability,
                identifier=identifier)

    def explode(self):
        """
        Override that always returns "...it's a glove."
        """
        print("...it's a glove.")

    def punch(self):
        if self.weight < 5:
            print("That tickles.")
        if self.weight >= 5 and self.weight < 15:
            print("Hey that hurt!")
        else:
            print("OUCH!")
