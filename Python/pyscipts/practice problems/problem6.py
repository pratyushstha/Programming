# Simulates rolling a six-sided die and asks user if they want to roll again
 
import random
a = input("Roll?(y/n)")
while a == "y" : 
    print(random.randint(1, 6))
    a = input("Roll again?(y/n)")