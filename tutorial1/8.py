count = 18
for i in range(1, count+1):
    print('%5i %5s %5s %10s' % (i,oct(i)[2:],hex(i)[2:].upper(), bin(i)[2:]))
