ang1=int(input("enter num1:"))
ang2=int(input("enter num2:"))
ang3=int(input("enter num3:"))
if ang1+ang2+ang3==180 and ang1>0 and ang2>0 and ang3>0:
    print("triangle is valid")
    if ang1==90 or ang2==90 or ang3==90:
        print("triangle is right angled")
    elif ang1>90 or ang2>90 or ang3>90:
        print("triangle is obtuse")
    else:
        print("triangle is acute")
else:
    print("triangle is not valid")
