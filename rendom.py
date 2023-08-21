# import random
# import math

# lower=int(input("Enter lower number :- "))
# higher=int(input("Enter higher number :- "))

# a=random.randint(lower,higher)

# print("\n\t you are only ",round(math.log(lower-higher + 1,2)),"chances to guess the integer!!!\n")

# i=0

# while i<math.log(lower-higher + 1, 2):
#     i+=1

#     guess=int(input("Guess a number :- "))

#     if a==guess:
#         print("Congratulations you did it in",i,"try")
#         break
#     elif a>guess:
#         print("you guessed to small!!")
#     elif a<guess:
#         print("you guessed to high!!")

# if i>=math.log(lower-higher + 1, 2):
#     print("\nthe number is %d",a)
#     print("\tbetter luck of next time!!")


import random
n = random.randint(1,100)
guess = int(input("Enter any number: "))
while n!= guess:
    if guess < n:
        print("Too low")
        guess = int(input("Enter number again: "))

    elif guess > n:
        print("Too high!")

        guess = int(input("Enter number again: "))

    else:

      break

print("you guessed it right!!")

