age = 17
day = 5
if day == 6 or day == 7:
   price = 10
if day > 0 and day < 6:
   if age < 16:
       price = 7.5
   elif age < 65:
       price = 10
   else:
       price = 5.5
print("You have to pay $%.2f for the ticket." % (price))
