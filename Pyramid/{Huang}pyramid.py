stack = int(input("How tall(1~8) the pyramid should be?"))
if stack <=8 and stack >=1:
 for i in range(0,stack):
    for j in range(0,stack-i-1):
       print(end=" ")
    for j in range(0,i+1):
       print("#",end="")
    print()
else:
    print("number is out of range, please exit the program.")
