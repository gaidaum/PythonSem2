#!/usr/bin/env python

def get_quantity(product):
 prompt = 'How many ' + product + '?\n'
 quantity = int(raw_input(prompt))
 return quantity

cd_lp = 10.0
vin_lp = 15.0
vin_ep = 8.0
vin_S = 5.0

cd_lp_no = get_quantity('cd albums')
vin_lp_no = get_quantity('vinyl albums')
vin_ep_no = get_quantity('vinyl EPs')
vin_S_no = get_quantity('vinyl singles')

bill = (cd_lp * cd_lp_no) + (vin_lp * vin_lp_no) + (vin_ep *
vin_ep_no) + (vin_7 * vin_7_no)
print 'Bill:',bill, 'euro'



