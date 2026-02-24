import random


def read_file():
    global listed_words
    listed_words = []
    word_list_txt = open("word list.txt")
    for lines in word_list_txt:
        listed_words.append(lines.rstrip("\n"))
    word_list_txt.close()

def add_word():
    read_file()
    word_list_txt = open("word list.txt", "a")
    user_input = input(" What word you want to add: ")
    user_input.lower()
    if user_input in listed_words:
        print("Word already is on the list")
    else:
        word_list_txt.write(f"\n{user_input}")
        print(f'Word "{user_input}" have benn added to the list')
    word_list_txt.close()

def draw_word():
    read_file()
    global choosen_word
    choosen_word = random.choice(listed_words)
    print(choosen_word)

def print_word():
    print_word = []
    for letter in choosen_word:
        if letter in quessed_letters:
            print_word.append(letter)
        else:
            print_word.append("#")
    print(f"your word: {print_word}") #delete later

def draw_hangman(chances):
    match chances:
        case 7:
             pass
        case 6:
             print("""
                      
                      
                         
                     
                           
                     
                            
                        ___/|\_
                    """)
        case 5:
             print("""
                    
                            
                            
                            
                            |
                            |
                            |
                        ___/|\_
                    """)
        case 4:
             print("""
                     
                            |
                            |
                            |
                            |
                            |
                            |
                        ___/|\_
                    """)
        case 3:
             print("""
                      _______
                           \|
                            |
                            |
                            |
                            |
                            |
                        ___/|\_
                    """)
        case 2:
             print("""
                      _______
                      |    \|
                            |
                            |
                            |
                            |
                            |
                        ___/|\_
                    """)
        case 1:
             print("""
                      _______
                      |    \|
                     ( )    |
                     /|\    |
                            |
                            |
                            |
                        ___/|\_
                    """)
        case 0:
            print("""
                      _______
                      |    \|
                     ( )    |
                     /|\    |
                      |     |
                     / \    |
                            |
                        ___/|\_
                    """)

def game_cycle():
    chances = 7
    global quessed_letters
    quessed_letters = []
    choosen_word_list = list(choosen_word)
    while len(quessed_letters) != len(choosen_word_list):
        print_word()
        print (len(choosen_word_list))
        print(len(quessed_letters))
        user_input = input("Choose letter: ")
        user_input.lower()
        if user_input in choosen_word :
            if user_input not in quessed_letters:
                quessed_letters.append(user_input)
                print(quessed_letters)

        else:
            chances = chances - 1
            draw_hangman(chances)

    if len(quessed_letters) == len(choosen_word_list):
        print("You Guessed!!!")
    elif chances == 0:
        print("You Lose!!!")


def main():
    player_choosen = False

    while player_choosen == False:
        
        print("------HangMan------")
        print("(1) Start game")
        print("(2) add word")
        print("(3) exit game")
        user_input = input("your choice: ")

        match user_input:
            case "1":
                game_on = True
                player_choosen = True
                draw_word()
                game_cycle()
            case "2":
                player_choosen = True
                add_word()
            case "3":
                player_choosen = True
            case _:
                print("error try normal option")

main()