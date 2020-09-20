# hrs= 45
# rate = 10.5

hrs = input('Enter hours:')
h = float(hrs)
rate = input('Enter rates:')
r = float(rate)

if h>40:
    over = h-40
    o = float(over)
    normal_hours = h-o
    nh = float(normal_hours)
    pay = (nh*r)+(o*(1.5*r))
else:
    pay = h*r

print(pay)
