# Exercise  7.2: Write a program to prompt for a file name, and then read
# through the file and look for lines of the form:
# X-DSPAM-Confidence:0.8475
# When you encounter a line that starts with "X-DSPAM-Confidence:" pull apart
# the line to extract the floating-point number on the line. count these lines
# and then compute the total of the spam confidence values from these lines.
# When you reach the end of the file, print out the average spam confidence.
# Enter the file name: mbox.txt
# Average spam confidence: 0.894128046745
# Enter the file name: mbox-short.txt
# Average spam confidence: 0.750718518519
# Test your file on the mbox.txt and mbox-short.txt files.


hname = input('please enter file name')
fname = open(hname)

# fname = open('mbox-short.txt')
total= 0
count = 0
for line in fname:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    # print(line)
    # print(len(line))
    x =line[20:27]
    y= float(x)
    # print(y)
    total = total + y
    count= count +1
# print(total)
# print(count)

avg = total/count
avgg = str(avg)
# print(avg)
print("Average spam confidence:", avgg)
# print('done')
