#It is a popular game played among kids. Especially, in the US.
# If you want to read about it: https://en.wikipedia.org/wiki/Fizz_buzz#:~:text=Fizz%20buzz%20(often%20spelled%20FizzBuzz,a%20loop%20and%20conditional%20statements. 

for number in range (1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)