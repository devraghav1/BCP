N= int(input("enter a no."))
ans=0

while(N>0):
    d=N%10
    N=N//10
    ans=ans*10+d
print(ans)

