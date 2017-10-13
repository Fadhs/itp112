age = 17
day = 5
if day == 6 or day == 7:
   price = 10
elif day == 1 or day == 2 or day == 3 or day == 4 or day == 5:
   if age <16:
       price = 7.5
   elif age >= 16 and age < 65:
       price = 10
   else:
       price = 5.5
print("You have to pay $%.2f for the ticket." % (price))
