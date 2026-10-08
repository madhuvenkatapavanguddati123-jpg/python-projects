# coffee mechine

mechine_data={
    "latte":{
        "price":50,
        "ingredents":{
            "milk":50,
            "power":10,
            "water":100
        }
    },
    "espresso":{
        "price":40,
        "ingredents":{
            "milk":50,
            "power":20,
            "water":80
        }
    },
    "coffee":{
        "price":80,
        "ingredents":{
            "milk":50,
            "power":20,
            "water":80
        }
    }
}
items=["espresso","latte","coffee"]
profit=0
milk=50
power=300
water=1000
while True:
    if milk==0 or power==0 or water==0:
        print("mechine out of ingredents . try after sometime !")
    #to take customer order
    user_input=input("What would you like to have(espresso,latte,coffee):").lower()
    #check is customer order in menu
    if user_input in items:
        #items used for order
        # money from user

        rupee_5=int(input("how many 5 rupees do you have:"))
        rupee_10=int(input("how many 10 rupees do you have:"))
        rupee_20=int(input("how many 20 rupees do you have:"))
        user_amount=5*rupee_5+10*rupee_10+20*rupee_20
        item_price=mechine_data[user_input]["price"]
        
        milk_used=mechine_data[user_input]["ingredents"]["milk"]
        water_used=mechine_data[user_input]["ingredents"]["water"]
        power_used=mechine_data[user_input]["ingredents"]["power"]


        if user_amount>=item_price:
            
           #items used
            if  milk<milk_used or power<power_used or water<water_used:
                print(f"item not avaliable\nhear is your ammount rs {user_amount}")
            else:    
                milk-=milk_used
                power-=power_used
                water-=water_used
                #calculate profit
                profit+=item_price
                #customer change
                if user_amount>item_price:
                    print(f"hear is your change rs {user_amount-item_price}")
                print("hear is your order!")
        else:
            print("not enough money")    

    elif user_input=="report":
        user_pass_key=input("enter your pass key:")
        if user_pass_key=="madhu@1234":
            print(f"milk={milk}\npower={power}\nwater={water}\nprofit={profit}")
        else:
            print("access denide!")      
    elif user_input=="service":
        user_pass_key=input("enter your pass key:")
        if user_pass_key=="madhu@1234":
            milk+=int(input("how much milk do you want to add:"))
            water+=int(input("how much water do you want to add:"))
            power+=int(input("how much power do you want to add: ")) 
        else:
            print("access denied!")       
    elif user_input=="off":
        user_pass_key=input("enter your pass key:")
        if user_pass_key=="madhu@1234":
                 break
        else:
            print("access denied!")
print("mechine is off! Thank you")            
