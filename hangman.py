import random


def read_file():
    global listed_words
    listed_words = []
    word_list_txt = open("word list.txt")
    for lines in word_list_txt:
        listed_words.append(lines.rstrip("\n"))
    word_list_txt.close()

def write_to_file():
    pass

def draw_word():
    global choosen_word
    choosen_word = random.choice(listed_words)
    print(choosen_word)

def game_cycle():
    pass

def main():
    pass

read_file()
draw_word()