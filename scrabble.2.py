# -*- coding: utf-8 -*-


import math
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    "a": 1,
    "b": 3,
    "c": 3,
    "d": 2,
    "e": 1,
    "f": 4,
    "g": 2,
    "h": 4,
    "i": 1,
    "j": 8,
    "k": 5,
    "l": 1,
    "m": 3,
    "n": 1,
    "o": 1,
    "p": 3,
    "q": 10,
    "r": 1,
    "s": 1,
    "t": 1,
    "u": 1,
    "v": 4,
    "w": 4,
    "x": 8,
    "y": 4,
    "z": 10,
    "*":0,
}

# -----------------------------------
# Yardımcı kod
# (bu yardımcı kodu anlamanıza gerek yok)

WORDLIST_FILENAME = "wordlist.txt"




def load_words():
    """
    Geçerli sözcüklerin bir listesini döndürür. Kelimeler küçük harflerden oluşan dizelerdir.

    Sözcük listesinin boyutuna bağlı olarak, bu işlev
    bitirmek biraz zaman alabilir.
    """

    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, "r")
    # wordlist:dizelerin listesi
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "kelimeler yüklendi.")
    return wordlist


def get_frequency_dict(sequence):
    """
    Anahtarları dizinin elemanları olan bir sözlük döndürür ve değerler,
    bir öğenin dizide tekrarlanma sayısı için tamsayı sayılarıdır.
    sequence: dize veya liste
    return: sözlük
    """

    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq



def get_word_score(word, n):
    
    word=word.lower()
    first_value=0
    second_value=(7*len(word))-(3*(n-len(word)))
    for i in word:
        for j in SCRABBLE_LETTER_VALUES:
            if i==j:
                first_value+=SCRABBLE_LETTER_VALUES[j]
    if second_value<1:
        second_value=1
    
    point=first_value*second_value
    
    return point
def display_hand(hand):
    
    hand_str=""
    for letter in hand.keys():
        for j in range(hand[letter]):
            hand_str += letter + " "
    return hand_str

def deal_hand(n):
    
    hand = {}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels, n):
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand

def update_hand(hand, word):
   
    word=word.lower()
    hand2=hand.copy()
    for i in word:
        for j in hand2.keys():
            if i==j:
                hand2[i]-=1
    return hand2
  

def is_valid_word(word, hand, word_list):

    word=word.lower()
    hand2=hand.copy()
    if word in word_list:
        for i in word:
            if i not in hand2.keys():
                return False
                break
            else:
                if hand2[i]<=0:
                    return False
                    break
                else: 
                    hand2[i]-=1
                    
        return True
    else:
        return False


def calculate_handlen(hand):
   
    handlen=0
    for i in hand.keys():
        handlen+=hand[i]
    return handlen      


def play_hand(hand, word_list):
    
    total_score=0
    n=HAND_SIZE
    
    print("Mevcut el:",display_hand(hand))
    while True:
        
        word= input("Kelime veya bitirdiğinizi belirtmek için '!!' giriniz: ")
        if word=="!!":
            print("Toplam puan: ", total_score)
            break
        else:
            if is_valid_word(word, hand, word_list)==True:
                total_score+=get_word_score(word, n)
                print(word,get_word_score(word, n),"puan kazandı. Toplam puanınız:", total_score)
                

            else:
                print("Bu geçerli bir kelime değil. Lütfen başka bir kelime seçin.")
                
            print("Mevcut el:",display_hand(update_hand(hand, word)))
            hand=update_hand(hand, word)
            if calculate_handlen(hand)<=0:
                print("Harfler tükendi. Toplam puan:", total_score)
                break
    return total_score
            


def substitute_hand(hand, letter):
    
    new_hand=hand.copy()
    new_letter=random.choice(VOWELS + CONSONANTS)
    count=new_hand[letter]
    if new_letter not in new_hand.keys():
        del new_hand[letter]
        new_hand[new_letter]=count
        
    return new_hand
      

def play_game(word_list):
   
    rounnd=int(input("Toplam el sayısını giriniz:"))
    rounnd_score=0
    for i in range(rounnd):
        hand=deal_hand(n)
        print("Mevcut el: ", display_hand(hand))
        replace=input("Bir harfi değiştirmek ister misiniz, yes or no?:")
        if replace=="yes":
            letter=input("Hangi harfi değiştirmek istersiniz:")
            hand=substitute_hand(hand, letter)
        first_again=play_hand(hand, word_list)
        print("Bu turdaki toplam puan:",first_again)
        print("----------------")
        
        again=input("Bu eli tekrardan oynamak siter misiniz,yes or no?: ")
        if again=="yes":
            second_again=play_hand(hand, word_list)
            print("Bu turdaki toplam puan:",second_again)
            if first_again<second_again:
                rounnd_score+=second_again
            else:
                rounnd_score+=first_again
        else: 
            rounnd_score+=first_again
            
        print("----------------")
            
    print("Tüm ellerde toplam puan:", rounnd_score)
 
if __name__ == "__main__":
    n=HAND_SIZE
    word_list = load_words()
    play_game(word_list)