percentage=int(input("enter percentage:"))
if percentage>=85:
    print("Grade: A+")
elif percentage>=65 and percentage<85:
    print("Grade: A")
elif percentage>=45 and percentage<65:
    print("Grade: B")
elif percentage>=25 and percentage<45:
    print("Grade: C")
else:
    print("Grade: D")