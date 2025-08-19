n = int (input("enter a no."))
S = 0
while(n>0):
    digit = n%10
    n=n//10
    S+=digit
print(S)
