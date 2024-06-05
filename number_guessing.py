import random 
print("Welcome to THE GAME")
top=(input("enter your high number "))
if(top.isdigit()):
    top=int(top)
    if(top<=0):
        print("number should be greater than 0")
else:
    print("it should be a number")
    quit()
number=random.randint(0,top)
guess=input(f"Guess the number ")
if(guess.isdigit()):
    guess=int(guess)
else:
    print("it should be a number")
    quit()
count=1

while True:
    if(guess!=number):
        guess=input("Try Again!!")
        if(guess.isdigit()):
            guess=int(guess)
            count=count+1
        else:
            print("it should be a number")
            count+=1
            continue
    else:
        print("That's Right!! You did it in",count,"tries ")
        break