# Exercise 3.2: Rewrite your pay program using try and except so that your
# program handles non-numerical input gracefully by printing a message and
# exiting the program. The folowing shows two executions of the program:
# Enter Hours: 20
# Enter Rate : nine
# Error, please enter numeric input
# Enter Hours: forty
# Error, please enter numeric input

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
#print('Test')
