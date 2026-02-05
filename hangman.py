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
    print(f"your word: {print_word}")

def game_cycle():
    pass

def main():
    game_on = False
    player_choosen = False
    global played_letters
    played_letters = []
    global quessed_letters
    quessed_letters = []

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
                read_file()
                draw_word()
                print_word()
            case "2":
                player_choosen = True
                add_word()
            case "3":
                player_choosen = True
            case _:
                print("error try normal option")

    while game_on == True:
        pass

main()