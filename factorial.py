def fact(n):#/*using recursion/*
    if n==0:
        return 1
    else:
        return n*fact(n-1)

n=int(input())
result=fact(n)
print(result)

j=int(input("enter the value:"))#using for loop
resu=1
for i in range(j,0,-1):
      resu=resu*i
print(resu)
