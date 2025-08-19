num1=int(input("enter num1:"))
num2=int(input("enter num2:"))
num3=int(input("enter num3:"))

if num1>num2 and num2>num3:
  print("num3 is smallest:",num3)
elif num2>num1 and num3>num1:
  print("num1 is smallest:",num1)
else:
  print("num2 is smallest:",num2)