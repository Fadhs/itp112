temp = 33
if temp < 20:
    desc = "Cold"
elif temp >= 20 and temp < 28:
    desc = "Cool"
elif temp >= 28 and temp < 33:
    desc = "Warm"
else:
    desc = "Hot"
print(desc)
