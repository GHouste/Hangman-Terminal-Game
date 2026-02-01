import random


def read_file():
    
    word_list_txt = open("word list.txt")
    x = 0
    for lines in word_list_txt:
        print(f"{x} {lines}")
        x = x + 1
    word_list_txt.close()

def write_to_file():
    pass

def game_cycle():
    pass

def main():
    pass

read_file()