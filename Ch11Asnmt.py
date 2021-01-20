#opening file and defining global variables
file = open('CH11C_Obrien_data.txt','r')
import re
lines=file.readlines()
tot_num=list()
sum_num=0

#loop to use RE to find all numbers and convert to integers
for line in lines:
    num = re.findall('[0-9]+',line)
    tot_num =tot_num + num
for x in tot_num:
    x=int(x)
    sum_num=sum_num+x

#printing final solution
print(sum_num)
