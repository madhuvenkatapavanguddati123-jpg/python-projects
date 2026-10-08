import random


game_data=["Rock","Paper","Scissors"]

#computer guss
while True:
    guss=random.randint(0,2)
    computer_guss=game_data[guss]
    while True:
        user_guss=input("enter Rock ,Paper or Scissors:")
        if user_guss in game_data:
            break
        else:
            print("invalid input Try again!")
    if user_guss==computer_guss:
        print("Tie!")
    elif computer_guss =="Scissors" and user_guss=="rock" :
        print("you wins!")
    elif  computer_guss=="Paper" and user_guss=="Scissors" :
        print("you wins!")
    elif computer_guss=="Rock" and user_guss=="Scissors":
        print("you win!")
    else:
        print("computer guss:",computer_guss)
        print("computer win!")         

     
