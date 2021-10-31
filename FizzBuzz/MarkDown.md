## MarkDown

# At first I thought I needed to use the "for in" command to determine the interval from 1 to 100, and then use the if statement to make the final output work. But I failed, and here is my first attempt.

- def fizzbuzz(x):

 for i in range(0, 100):

  if (x % 3 ==0) and (x % 5 ==0):

      print("FizzBuzz")

  elif (x % 3 ==0):

        print("Fizz")

  elif (x % 5 ==0):

        print("Buzz")

# I thought it didn't work because I wasn't sure about the output of x, so I added the "else" statement, but apparently the result wasn't good.

- def fizzbuzz(x):

 for i in range(0, 100):

  if (x % 3 ==0) and (x % 5 ==0):

      print("FizzBuzz")

  elif (x % 3 ==0):

        print("Fizz")

  elif (x % 5 ==0):

        print("Buzz")

  else:

       print(x)

# Then, at Rachel's prompting, I looked at the "lovely!" example from class and saw that the code could be done by "count", so I tried to change it. And it seems that I succeeded! But the runtime doesn't start from 1. I think I know what to do.  

- def fizzbuzz(count):

 for i in range(0, count + 1):

  if (i % 3 ==0) and (i % 5 ==0):

      print("FizzBuzz")

  elif (i % 3 ==0):

        print("Fizz")

  elif (i % 5 ==0):

        print("Buzz")

  else:

        print(i)
        
# After changing the range I did it! It was a fun process! Here is the final code.

- def fizzbuzz(count):

 for i in range(1, count + 1):

  if (i % 3 ==0) and (i % 5 ==0):

      print("FizzBuzz")

  elif (i % 3 ==0):

        print("Fizz")

  elif (i % 5 ==0):

        print("Buzz")

  else:

        print(i)

fizzbuzz(100)
