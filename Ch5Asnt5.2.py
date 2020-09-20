# Exercise 5.1: Write another program that prompts for a list of numbers as
# above and at the end prints out both the maximum and minimum of the numbers
# instead of the average.

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
