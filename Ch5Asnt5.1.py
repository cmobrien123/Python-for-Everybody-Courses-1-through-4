# Exercise 5.1: Write a program which repeatedly reads numbers until the user
# enters "done". Once "done" is entered, print out the total, count, and average
# of the numbers. If the user enters anything other than a number, detect their
# mistake using try and except and print an error message and skip to the next
# number.
# Enter a number: 4
# Enter a number: 5
# Enter a number: bad data
# Invalid input
# Enter a number: 7
# Enter a number: done


num = 0
tot = 0.0
while True:
    sval = input("Enter a number: ")
    if sval == 'done':
        break
    try:
        fval = float(sval)
        print(fval)
        num = num +1
        tot = tot + fval
    except:
        print("please enter a number, not a string. enter done if finished")

print('All Done')
print(tot,num,tot/num)
