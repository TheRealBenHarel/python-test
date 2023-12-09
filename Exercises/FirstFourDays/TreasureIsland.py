#This is a navigation game

print("Welcome to Treasure Island. Your mission is to find the treasure.")
first_decision = input("You're at a crossroad. Where do toy want to go? Type ''left'' or ''right''\n")
if first_decision == "right":
    print("You got run over by Santa's reindeer. Game Over.")
    exit(1)
elif first_decision == "left":
    print("\n")
else:
    print("We didn't understand your answer so it took too long to process and you died of old age.")
    exit(1)
second_decision = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' \
                        to wait for a boat. Type 'swim' to swim across.\n")
if second_decision == "swim":
    print("You got eaten by an alligator. Game Over.")
    exit(1)
elif second_decision == "wait":
    print("\n")
else:
    print("We didn't understand your answer so it took too long to process and you died of old age.")
    exit(1)
        
third_decision = input("You arrived at the island unharmed. There is a house with 3 doors. \
    One red, one yellow, and one blue. Which color do you choose?\n")
if third_decision == "yellow":
    print("You win!.")
elif third_decision == "red" or third_decision == "blue":
    print("A hungry witch was waiting patiently inside. You got eaten. Game Over.")
else:
    print("We didn't understand your answer so it took too long to process and you died of old age.")
    exit(1)
exit(1)