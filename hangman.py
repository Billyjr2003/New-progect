import random
from project import words
import string

def get_valid_word(words) :
    word = random.choice(words)


    return word

def hang_man():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    
    while len(used_letters) >= 0:
        print("you have used these letters : " , " ".join(used_letters))
        

        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("current word is : " , " ".join(word_list))

        user_letter = input("guess a letter : ")
        if user_letter in alphabet or user_letter not in used_letters :
            used_letters.add(user_letter)
            if user_letter in word_letters :
                word_letters.remove(user_letter)
        elif user_letter in used_letters :
            print("you have used this character before . try again ") 
        else : 
            print ("invalid character . please tr again")           

hang_man()
          

