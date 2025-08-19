num = int(input("Enter a number: "))

if num % 3 == 0 and num % 10 == 4:
    print("The number is divisible by 3 and ends with 4.")
else:
    print("The number does not meet both conditions.")