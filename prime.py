lower=int(input("enter the value"))#generating
upper=int(input("enter the value"))
for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)

n=int(input("value?"))#checking
if n>1:
    for i in range(2,n):
        if n%i==0:
            print("not prime")
            break
    else:
        print("prime")
