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
