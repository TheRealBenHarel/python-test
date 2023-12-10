import random
def display():
    #print(dash_list)
    dash_print = ""
    for i in range(0, len(random_word)):
        dash_print += dash_list[i] + " "
    print(dash_print)
    
def victory_checker():
    if  "_" not in dash_list:
        print("You won!")
        exit(1)

word_list = ["ardvark", "baboon", "camel"]
dash_list = []
wrong_guesses = 0
random_word = word_list[random.randint(0, len(word_list) - 1)]
for i in range(0, len(random_word)):
    dash_list.append("_")
dash_print = ""
for i in range(0, len(random_word)):
    dash_print += dash_list[i] + " "
#print(random_word)
#print(dash_list)
print(dash_print)

while wrong_guesses <= 7:
    guess = input("Please choose a letter:\n").lower()
    correct_guesses = 0
    for i in range(0, len(random_word)):
        if guess == random_word[i]:
            correct_guesses += 1
            dash_list.insert(i, guess)
            del dash_list[i+1]
    if correct_guesses >= 1:
        print("This letter exists!")
        correct_guesses = 0
        display()
        victory_checker()
    else:
        print("This letter doesn't exist!")
        wrong_guesses += 1
        display()
print("You lost!")




