import random
A=int(input("Enter the starting point of your range: "))
B=int(input("Enter the end point of your range: "))
num = random.randint(A,B)
guess = None
count=0

while guess != num  :
    guess = input("guess a number between "+ str(A) +" and " + str(B)+" :")
    guess = int(guess)
    if count>=7:
        print("Better Luck Next Time!")
    elif guess == num:
        print("congratulations! you won!")
        break
    elif(guess>num):
         print("Try Again!You guessed too High")
         break
    elif(guess<num):
        print("Try Again! You guessed too small")
    count=count+1