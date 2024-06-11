name=input("Enter your name:")
age=int(input("Enter your age:"))

time=input("Enter 'daytime show' or 'evening show' for the time of the show:")

match time:
    case "daytime show":
        dticketprice_0to4="free"
        dticketprice_5to17=50
        dticketprice_18to64=100
        dticketprice_65andabove=80
        
    case "evening show":
        eticketprice_0to4="free"
        eticketprice_5to17=70
        eticketprice_18to64=120
        eticketprice_65andabove=100

    case _:
        print("Unknown time")
        
if time=="daytime show":
    if age<0:
        print("ERROR: The age cannot be a negative number.")
    elif (age>=0 and age<=4):
        print(f"Hello {name}, your ticket is {dticketprice_0to4} for the {time}!")
    elif (age>=5 and age<=17):
        print(f"Hello {name}, your ticket costs ₱{dticketprice_5to17} for the {time}!")
    elif (age>=18 and age<=64):
        print(f"Hello {name}, your ticket costs ₱{dticketprice_18to64} for the {time}!")
    elif (age>=64 and age<=float('inf')):
        print(f"Hello {name}, your ticket costs ₱{dticketprice_65andabove} for the {time}!")
    else:
        print(f"You're not a human.")
elif time=="evening show":
    if age<0:
        print("ERROR: The age cannot be a negative number.")
    elif (age>=0 and age<=4):
        print(f"Hello {name}, your ticket is {eticketprice_0to4} for the {time}!")
    elif (age>=5 and age<=17):
        print(f"Hello {name}, your ticket costs ₱{eticketprice_5to17} for the {time}!")
    elif (age>=18 and age<=64):
        print(f"Hello {name}, your ticket costs ₱{eticketprice_18to64} for the {time}!")
    elif (age>=64 and age<=float('inf')):
        print(f"Hello {name}, your ticket costs ₱{eticketprice_65andabove} for the {time}!")
    else:
        print(f"You're not a human.")
else:
    print(f"You're not a human.")





