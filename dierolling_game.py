import random
playing=True
while   playing:#loop
    choice=input('Roll the dice(y/n):')               #ask the user
    if choice=='y':#if the user enters y
        die1=random.randint(1,6)
        die2=random.randint(1,6)
        print(f'{die1},{die2}')#generate two random numbers
    elif choice=='n':#if user enters n
        print("thank for coming")
        break  #break
    else:
        print("invalid")
#exit