import sys

# the price list
price_list = {'CD':10.0,'VIN-EP':8.0,'VIN-S':5.0,'VIN-LP':15.0}

lines = sys.stdin.readlines()

bill = 0
for line in lines:
    item = line.split()
    product = item[0]
    quantity = int(item[1])
    bill += price_list[product] * quantity

print 'Bill:',bill,'euro'

