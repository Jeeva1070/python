n=int(input("eter the input"))#up star 
for row in range(n):
      for col in range(n):
          if(col==0 or row==n-1 or row==col):
              print("*",end="")
          else:
              print(end=" ")
      print()
#------------------------------------------------------------------------------        
n=int(input("enter the input"))#down star 
for row in range(n):
      for col in range(n):
          if(row==0 or col==n-1 or row==col):
              print("*",end="")
          else:
              print(end=" ")
      print()
#------------------------------------------------------------------------------ 
print("-----------hollow triangle-------------")       
for row in range(1,5):
      for col in range(1,8):
            if row==4 or row+col==5 or col-row==3:
                  print("*",end="")
            else:
                  print(end=" ")
      print()

print("-----------equal triangle-------------")
n=int(input("enter the rows:"))
k=2
for row in range(1,n+1):
      for col in range(1,2*n):
            if row+col==n+1 or col-row==n-1:
                  print("*",end="")
            elif row==n and col!=k:
                  print("*",end="")
                  k=k+2
            else:
                  print(end=" ")
      print()
#------------------------------------------------------------------------------ 
n=int(input("enter the rows"))#while loop triangle
row=0
while row<n:
      star=row+1
      while star>0:
            print("*",end="")
            star=star-1
      row=row+1
      print()
#------------------------------------------------------------------------------  
num=int(input("enter the rows:"))#while loop pyramid
row=0
while row<num:
      space=num-row-1
      while space>0:
            print(end=" ")
            space=space-1
      star=row+1
      while star>0:
            print("*",end=" ")
            star=star-1
      row=row+1
      print()
            
