# Exercise  10.2: This program counts the distribution of the hour of the day
# for each of the messages. You can pull the hour from the "From" line by finding
# the time string and then splitting that string into parts using the colon
# character. Once you have accumulated the counts for each hour, print out the
# counts, one per line, sorted by hour as shown below.
# Sample line: From stephen.marquard@uct.ac.az Sat Jan 05 09:14:16 2008
# Sample Execution:
# python timeofday.py
# Enter a file name: mbox-short.txt
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1



fname = input('enter file')
# fname= 'mbox-short.txt'
fhand=open(fname)
# print(fhand)
counts=dict()
lst=list()
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    line = line.split()
    # print(line)
    time= line[5]
    # print(time)
    x =time.split(':')
    hr=x[0]
    # print(hr)
    lst.append(hr)
# print(lst)
for hr in lst:
    counts[hr] =counts.get(hr, 0)+1
# print(counts)
lst2=list()
for k,v in counts.items():
    lst2.append((k,v))
    # print(k,v)
lst2.sort(reverse=False)
for k,v in lst2:
    print(k,v)
