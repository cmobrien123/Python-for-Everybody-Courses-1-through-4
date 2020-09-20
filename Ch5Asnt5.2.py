largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try:
        fnum = int(num)
        if largest is None:
            largest = fnum
        if fnum > largest:
            largest = fnum
        if smallest is None:
            smallest = fnum
        if fnum < smallest:
            smallest = fnum
    except:
        print('Invalid input')

print("Maximum is", largest)
print("Minimum is", smallest)
