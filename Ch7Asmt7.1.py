fname = input('please enter the name of the file:')
# fname = 'words.txt'
fh= open(fname, 'r')
for line in fh:
    line = line.strip()
    line = line.upper()
    print(line)
