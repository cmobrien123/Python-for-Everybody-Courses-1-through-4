# fname = input('Enter file name: ')
fname = 'mbox-short.txt'

fhand = open(fname)
# print(fhand)
count = dict()

for line in fhand:
    if not line.startswith('From '): continue
    line = line.rstrip()
    line = line.split()
    word = line[1]
    count[word]= count.get(word,0)+1
# print(count)

MaxName = None
MaxNumb = 0
for k,v in count.items():
    if MaxName == None or v>MaxNumb:
        MaxName=k
        MaxNumb=v
print(MaxName, MaxNumb)

# print(count.items())


## Test to see if Desktop github is working
##another Test
