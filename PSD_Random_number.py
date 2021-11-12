import random
class rannumber:

    #The init checks the parameteres and sees if they are
    #numbers and positive. If these two pre conditions are met
    #an instance of the class is created. 
    def __init__(self, amount, minRange, maxRange):
        check = [amount, minRange, maxRange]
        if all([type(x) == int and x >= 0 for x in check]):
            self.amount = amount
            self.minRange = minRange
            self.maxRange = maxRange
        else:
            print("Input needs to be a positive number")

    #The function return the amount of number based on its self.amount
    #value and the range for the random numbers are set with
    #self.minRange and self.maxRange. 
    def getRandomNumber(self):
        for x in range(self.amount):
            print(random.randint(self.minRange, self.maxRange))

while True:
    values = input("Enter the amount of numbers and the range for random: ")
    values_list = values.split(" ")
    rannumber(int(values_list[0]),int(values_list[1]),int(values_list[2])).getRandomNumber()
