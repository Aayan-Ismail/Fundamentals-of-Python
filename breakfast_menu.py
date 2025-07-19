day = input("what day of the week is it? ")
print(day)

if (day == "monday"): 
    print("roti")

elif (day == "tuesday"):
    print("bread")

elif (day == "wednesday"):
    print("eggs")

elif (day == "thursday"):
    print("ox, three barrels of mead, eight salmon")

elif (day == "friday"):
    print("roti and chicken curry")

elif (day == "saturday"):
    print("lamb")

elif (day == "sunday"):
    print("coddle")

else:
    print("no breakfast")
    while day != "monday" or "tuesday" or "wednesday" or "thursday" or "friday" or "saturday" or "sunday":
        day = input("what day of the week is it? ")
        print("you will only get lamb")




         