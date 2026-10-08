import random


player_choose=True
while player_choose:
     computer_guss=random.randint(1,100)
     while True:
          user_guss=int(input("Enter a number between 1 to 100: "))
          if user_guss==computer_guss:
               print("correct answer!")
               break
          elif user_guss>computer_guss:
               print("Too High")
          elif user_guss<computer_guss:
               print("Too low")
     player_choose=input("play again (y/n): ").lower()
     if player_choose=='y':
          player_choose=True
     elif player_choose=='n':
           print("thanks for playing")
           player_choose=False
     else :
          print("invalid input Try again!")                 
