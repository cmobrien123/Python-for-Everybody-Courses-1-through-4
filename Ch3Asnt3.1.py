# Exercise 3.1: Rewrite your pay computation to give the employee 1.5 times the
# rate for hours worked above 40 hours.
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

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
#fin
