# Exercise  9.4: Add ccode to the above program to figure out who has the most
# mesasges in the file.
# After all the data has been read and the dictionary has been created, look
# through the dictionary using a maximum loop (see Section [maximumloop]) to
# find who has the most messages and print how many messages the person has.
# Enter a file name: mbox-short.txt
# cwen@iupui.ed 5
# Enter a file name: mbox.txt
# zqian@umich.edu 195


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
