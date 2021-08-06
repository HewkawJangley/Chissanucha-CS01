i=0
NumTotal=[]
while (True):
     i=int(input("input:"))
     NumTotal += [i]
     NumTotal.sort()
     if i ==-1:
         break
     print(NumTotal)