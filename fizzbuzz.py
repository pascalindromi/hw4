for i in range(1, 101):
    fizz = (i % 3 == 0) or str(i) == 3 #condition for fizz
    buzz = (i % 5 == 0) or str(i) == 5 #condition for buzz
    if fizz and buzz:
        print("FizzBuzz")
    elif fizz:
        print("Fizz")
    elif buzz:
        print("Buzz")
    else:
        print(i)