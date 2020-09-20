# # hrs= 45
# # rate = "ten"

hrs = input('Enter hours:')
rate = input('Enter rates:')

try:
    h = float(hrs)
    r = float(rate)
except:
    print('Error, please enter a number')
    quit() ## THIS IS VERY USEFUL, if not used, you are trying to run code with undefined variable (h and r)

if h>40:
    over = h-40
    o = float(over)
    normal_hours = h-o
    nh = float(normal_hours)
    pay = (nh*r)+(o*(1.5*r))
else:
    pay = h*r

print(pay)
print('Test')
