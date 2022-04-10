import sys
import random

boys = ["name 1", "name 2", "name 3"]
girls = ["name 4", "name 5", "name 6"]

input("Press enter to generate a new ship" + "\n\n")

while True:
    rand = random.randint(1,10)
    if rand == 1:
        rand3 = random.randint(1,2)
        if rand3 < 2:
            rand = random.randint(0, len(boys)-1)
            rand2 = random.randint(0, len(boys)-1)
            
            if rand2 == rand:
                rand2 = rand2 + 1

            rand3 = random.randint(1,2)
            if rand3 < 2:
                ship = boys[rand] + " x " + boys[rand2]
            else:
                ship = boys[rand2] + " x " + boys[rand]
            
        else:
            rand = random.randint(0, len(girls)-1)
            rand2 = random.randint(0, len(girls)-1)
            
            if rand2 == rand:
                rand2 = rand2 + 1

            rand3 = random.randint(1,2)
            if rand3 < 2:
                ship = girls[rand] + " x " + girls[rand2]
            else:
                ship = girls[rand2] + " x " + girls[rand]
            
        print("New ship: " + ship)
        
    else:
        rand = random.randint(0, len(boys)-1)
        rand2 = random.randint(0, len(girls)-1)
        rand3 = random.randint(1,2)
        if rand3 < 2:
            ship = boys[rand] + " x " + girls[rand2]
        else:
            ship = girls[rand2] + " x " + boys[rand]
            
        print("New ship: " + ship)
        
    input("Press enter to generate a new ship" + "\n\n")
    


