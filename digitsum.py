number = int(input("input a number: "))
digit_sum = 0
while number > 0:
    digit_sum += number % 10 # returns the last digit and adds to digit_sum
    number = number // 10 # removes the last digit from number, repeat  
print(f"Digit sum: {digit_sum}")