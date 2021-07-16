a=int(input("คะแนนเก็บ :"))
b=int(input("คะแนนสอบกลางภาค :"))
c=int(input("คะแนนสอบปลายภาค :"))
z=a+b+c
if(80<=z<=100):
    print("A")
elif(75<=z<=79):
    print("B+")
elif(70<=z<=74):
    print("B")
elif(65<=z<=69):
    print("C+")
elif(60<=z<=64):
    print("C")
elif(55<=z<=59):
    print("D+")
elif(50<=z<=54):
    print("D")
else:
    print("F")