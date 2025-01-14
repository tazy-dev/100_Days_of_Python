print("Welcome To Treasure Island")
print("Your job is to find the treasure.")
direction = input('You are at a cross road. Where do you want to go? Type "left" or "right"\n').lower()
if direction == "right":
    print("You fell into a hole, Game Over")
else :
    action = input('You come to a lake. There is an island at the middle of lake.  Type "wait" to wait for a boat or "swim" to swim across\n').lower()
    if action == "swim":
        print("You got attacked by an angry trout, Game Over")
    else:
        door = input("You arive at the island unharmed. There is house with three doors. One red, one yellow and one blue. Which color do you choose?\n").lower()
        if door == "red":
            print("It's a room full of Fire, Game Over")
        elif door == "blue":
            print("It's a room Full of Beasts, Game Over")
        else:
            print("You Found the treasure, You Win!")


