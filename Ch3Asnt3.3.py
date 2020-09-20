# score=0.85

score = input("Give a score between 0.0 and 1.0")
s = float(score)
## note that g  is grade
try:
    if s>0 and s<=1:
        if s >=0.6 and s<0.7:
            G= "D"
        elif s>=0.7 and s<0.8:
            G= "C"
        elif s>=0.8 and s<0.9:
            G= "B"
        elif s>=0.9:
            G= "A"
        else:
            G="F"
    print(G)
except:
    print("Not able to calculate. Need number to be between 0.0 and 1.0")
