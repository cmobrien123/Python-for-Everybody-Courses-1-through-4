
# hours = 45
# rate= 10.5

hours = input("Enter hours:")
rate = input("Enter rate:")

h =float(hours)
r =float(rate)

def computepay(h2, r2):
    if h2>40:
        o2=h2-40
        pay = (40*r2)+(o2*(r2*1.5))
    else:
        pay = h2*r2
    return(pay)


print(computepay(h, r))
