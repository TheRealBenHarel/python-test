from PiglatinGenerator import to_piglatin_wi, to_piglatin_woi
from PiglatinTranslator import from_piglatin_wi, from_piglatin_woi

user_list_to_translate = 

print("Hello and welcome to the Piglatin Translator/Generator!\n What would you like to do?\n")
decision = (input("1. Translate a single word from Piglatin\n \
                  2. Translate a list of words from Piglatin\n \
                      3. Translate a single word to Piglatin\n \
                  4. Translate a list of words to Piglatin\n"))

match decision:
    
    case 1:
        from_piglatin_woi()
    case 2: 
        from_piglatin_wi(piglatin_word)
    case 3:
        to_piglatin_woi()
    case 4:
        to_piglatin_wi(user_word)  
    case _: 
        print("Enter 1, 2, 3 or 4 you stupid")
        decision = (input("1. Translate a single word from Piglatin\n \
                  2. Translate a list of words from Piglatin\n \
                      3. Translate a single word to Piglatin\n \
                  4. Translate a list of words to Piglatin\n"))
        