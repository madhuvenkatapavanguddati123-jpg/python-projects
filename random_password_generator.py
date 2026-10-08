import random


print("welcome to random password generator!")
print("how many letters would you like in your password?")
password=""
no_of_letters=int(input())
for i in range(no_of_letters):
    letters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    temp=random.choice(letters)
    password=password+temp
    
print("how many symbols would you like?") 
no_of_symbols=int(input())
for i in range(no_of_symbols):
        symbols='~!@#$%^&*()-+=_:"<>?/,|'
        temp=random.choice(symbols)
        password=password+temp
print("how many numbers would yoy like?")
no_of_numbers=int(input())
for i in range(no_of_numbers):
        nums='1234567890'
        temp=random.choice(nums)
        password=password+temp
password=set(password)        
for i in password:
       print(i,end="")   
