# the price list
cd_lp = 10.0
vin_lp = 15.0
vin_ep = 8.0
vin_sin = 5.0

# get the quantities from the user
cd_lp_no = int(raw_input('How many cd albums?\n'))
vin_lp_no = int(raw_input('How many vinyl albums?\n'))
vin_ep_no = int(raw_input('How many vinyl EPs?\n'))
vin_sin_no = int(raw_input('How many vinyl singles?\n'))

# calculate the bill
bill = (cd_lp * cd_lp_no) + (vin_lp * vin_lp_no) +(vin_ep * vin_ep_no) + (vin_sin * vin_sin_no)
print 'Bill:',bill, 'euro'
