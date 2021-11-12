import random
class rannumber:


    def __init__(self, amount, minRange, maxRange):
        check = [amount, minRange, maxRange]
        if all([type(x) == int and x >= 0 for x in check]):
            self.amount = amount
            self.minRange = minRange
            self.maxRange = maxRange
        else:
            print("Input needs to be a positive number")

    def getRandomNumber(self):
        for x in range(self.amount):
            print(random.randint(self.minRange, self.maxRange))

test = rannumber(3,4,8)
test.getRandomNumber()