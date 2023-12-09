
def to_piglatin_wi(user_word):
    piglatin_word = (user_word[-1] + user_word[:-1] + "ay")
    return piglatin_word

def to_piglatin_woi():
    user_word = input("Enter Your Word:\n")
    piglatin_word = (user_word[-1] + user_word[:-1] + "ay")
    return piglatin_word


