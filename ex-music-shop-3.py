import sys
# the price list
price_list = {'CD':10.0,'VIN-EP':8.0,'VIN-S':5.0,'VIN-LP':15.0}

lines = sys.stdin.readlines()

vin_total = 0
bill = 0
vin_disc = .15 # 15% discount on vinyl
for line in lines:
    item = line.split()
    product = item[0]
    quantity = int(item[1])
    bill += price_list[product] * quantity
    # calculate vinyl total
    if 'VIN' in product:
        vin_total += price_list[product] * quantity
    # calculate number of free cds
    elif 'CD' == product: 
        free_cds = quantity/3

print 'Bill before discounts:',bill,'euro'

# apply vinyl discount
if vin_total > 100:
    bill -= vin_total * vin_disc

# apply cd discount
bill -= free_cds * price_list['CD']

print 'Bill after discounts:',bill,'euro'

