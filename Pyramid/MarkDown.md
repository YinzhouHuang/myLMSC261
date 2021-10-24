## MarkDown
- At first, after referring to the hints on how to write a “for loop”, I started trying to figure out how I could write a pyramid.
- After many attempts I got:
stack = int(input("How tall(1~8) the pyramid should be?"))
for i in range(1,stack+1):
for j in range(0,11):
print("#",end="")
print()
- After successfully running the code thinking it was done I realized that I needed to make the pyramid with the ramp to the left instead of the ramp to the right. Then I started thinking and trying to figure out how to do it.
After trying the following code I managed to write the pyramid with the slope to the left!
stack = int(input("How tall(1~8) the pyramid should be?"))
 for i in range(0,stack):
    for j in range(0,stack-i-1):
       print(end=" ")
    for j in range(0,i+1):
       print("#",end="")
    print()
- So I just end up providing an if command for this string of code to keep the pyramid stacking interval between 1 and 8, and if it's outside of that interval I get the appropriate hint.
- This assignment was not an easy challenge for me, and it took me quite a while to figure out how to use the “for loop” to achieve the result I wanted. Because if the ramp is to the left you have to think about spaces, which is harder than if it is to the right.
