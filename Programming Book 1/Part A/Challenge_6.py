rain = input("Is it rainy? ")

if rain.lower() != "yes":
    print("Enjoy your day")

else:
    wind = input("Is it windy? ")
    if wind.lower() == "yes":
        print("It is too windy to take an umbrella")
    else:
        print("Take an umbrella")
