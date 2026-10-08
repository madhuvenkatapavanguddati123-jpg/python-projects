import random

while True:
      out=[]
      user_input=input("Role the dice(y/n):").lower()
      if user_input=='y' :
            for i in range(2):
                  out.append(random.randint(1,6))
            print(out)       
      elif user_input=='n':
            print("thanks for playing")
            break
      else:
            print("invalid input!")
                      
