from random import randint

n=randint(0,100)
a=-1
guess =0

while (n!=a):
    guess+=1
    a=int(input("enter the number :"))

    if (a<n):
        print("guess higher number pls")
    else:
        print("guess lower value")
print(f"you guessed the right number {n} in {guess} attempts")