# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
#total number of people on the list
num_people = len(names)
#randomly pick the number on the list
random_pick = random.randint(0, num_people -1)
#turn number into name
bill_payer = names[random_pick]
print(bill_payer + " is buying today!")