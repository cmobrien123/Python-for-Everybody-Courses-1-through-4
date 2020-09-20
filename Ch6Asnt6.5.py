text = "X-DSPAM-Confidence:    0.8475";


x=text.find(".")
y=text[x-1:x+5]
# print(y)
yint=float(y)
print(yint)

 
