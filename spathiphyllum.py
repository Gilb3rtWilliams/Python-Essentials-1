name = input("Enter the name of my favorite flower: ")

if name == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever")
elif name == "spathiphyllum":
    print("No! I want a big Spathiphyllum")
    name = input("Enter the name of my favorite flower properly: ")
    if name == "Spathiphyllum":
        print("Yes - Spathiphyllum is the best plant ever")

else:
    print("Spathiphyllum!!! Not ", name + "!")
