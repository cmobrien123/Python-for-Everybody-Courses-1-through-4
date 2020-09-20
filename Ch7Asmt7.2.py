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
