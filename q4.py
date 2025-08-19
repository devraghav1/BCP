num = int(input("Enter a number: "))

if num % 7 == 0 or num % 10 == 5:
    print("The number is divisible by 7 or ends with 5.")
else:
    print("The number is not divisible by 7 and does not end with 5.")
