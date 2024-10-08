# -*- coding: utf-8 -*-
"""
Created on Mon May  6 20:03:11 2024

@author: Sena Öz
"""

# Adam Asmaca Oyunu
#------------------------------------

import random
import string

WORDLIST_FILENAME = "kelimeler.txt"


def load_words():
    """
    Geçerli kelimelerin bir listesini döndürür.
    Kelimeler küçük harf dizileridir.
    
     Kelime listesinin boyutuna bağlı olarak,
     bu fonksiyonun tamamlanması biraz zaman alabilir.
    """
    print("Dosyadan kelime listesi yükleniyor...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(len(wordlist), "kelimeler yüklendi.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): kelime listesi(strings)
    
    Kelime listesinden rastgele bir kelime döndürür
    """
    return random.choice(wordlist)


wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, kullanıcının tahmin ettiği kelime;
    tüm harflerin küçük olduğunu varsayar
    letter_guessed: şimdiye kadar hangi harflerin tahmin edildiği (harflerin listesi);
     tüm harflerin küçük olduğunu varsayar
     returns: boolean, secret_word'ün tüm harfleri letter_guessed içindeyse True;
     Aksi takdirde yanlış
    '''

    for i in secret_word:
        if i not in letters_guessed:
            return False
    return True



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, kullanıcının tahmin ettiği kelime
    letter_guessed: şimdiye kadar hangi harflerin tahmin edildiği (harflerin listesi)
    returns: harflerden, alt çizgilerden (_) ve şu ana kadar secret_word
     içindeki hangi harflerin tahmin edildiğini gösteren boşluklardan oluşan dize.
    '''

    word=""
    for i in secret_word:
        if i not in letters_guessed:
            word+="_ "
        else:
            word+=i
    return word



def get_available_letters(letters_guessed):
    '''
    letter_guessed: şimdiye kadar hangi harflerin tahmin edildiği (harflerin listesi)
    returns: dize (harfler), hangi harflerin henüz tahmin edilmediğini temsil eden harflerden oluşur.
    '''

    harfler=""
    for i in string.ascii_lowercase:
        if i not in letters_guessed:
            harfler+=i
    return harfler

def adamAsmaca(secret_word):
    '''
    secret_word: string, tahmin edilecek gizli kelime.
    
     Etkileşimli bir Adam Asmaca oyununu başlatır.
    
     * Oyunun başında, kullanıcıya secret_word'ün kaç harf içerdiğini
        ve kaç tahminle başladığını bildirin.
      
     * Kullanıcı 6 tahminle başlamalıdır

     * Her turdan önce kullanıcıya kaç tahmin kaldığını ve
        kullanıcının henüz tahmin etmediği harfleri göstermelisiniz.
    
     * Kullanıcıdan tur başına bir tahmin vermesini isteyin.
        Kullanıcının bir mektup yazdığından emin olmayı unutmayın!
    
     * Kullanıcı, her tahminden hemen sonra tahminlerinin bilgisayarın
        kelimesinde görünüp görünmediği hakkında geri bildirim almalıdır.

     * Her tahminden sonra, o ana kadar kısmen tahmin edilen kelimeyi
         kullanıcıya göstermelisiniz.
    
     Problem yazımında detaylandırılan diğer sınırlamaları takip eder.
    '''

    print("Adam Asmaca Oyununa Hoş Geldiniz!")
    print("Kelimeniz",len(secret_word)," harfilidir.")
    tahmin_hakkı=6
    letters_guessed=[]
    uyarı=3
    ünlü_harfler='aeiou'    
    number_unique_letters=0
    print("Kullanılabilir harfler:",get_available_letters(letters_guessed))
    print("---------------")
    while tahmin_hakkı>0:
        print(f"Tahmin hakkınız {tahmin_hakkı}'dır")
        harf=input("Bir harf tahmin ediniz:")

    
        if str.isalpha(harf)==False:
            uyarı-=1
            print("Hata! Bu geçerli bir harf değil.",uyarı,"uyarınız kaldı ")
            print("---------------")
            if uyarı==0:
                tahmin_hakkı-=1
                uyarı=3
                
        else:
            if harf not in get_available_letters(letters_guessed): 
                if str.islower(harf)==False:
                    harf=str.lower(harf)
                    uyarı-=1
                    print("Hata!Büyük harf kullandınız.",uyarı," uyarınız kaldı")
                    print("---------------")
                    if uyarı==0:
                        tahmin_hakkı-=1
                        uyarı=3
                        
                else:
                    uyarı-=1
                    print("Hata! Bu harfi zaten tahmin ettin.",uyarı," uyarınız kaldı ")
                    print("---------------")
                    if uyarı==0:
                        tahmin_hakkı-=1
                        uyarı=3
                    continue
                        
                    
            letters_guessed.append(harf)
            print("Kullanılabilir harfler: ", get_available_letters(letters_guessed))
            if harf in secret_word:
                print("İyi tahmin:", get_guessed_word(secret_word, letters_guessed))
                number_unique_letters+=1
                if is_word_guessed(secret_word, letters_guessed)==True:
                    print("Oyunu kazandınız.")
                    print("Bu oyun için toplam puanın:", tahmin_hakkı*number_unique_letters) 
                    break
                print("---------------")
            
            else:

                print("Hata! O harf bu kelimede yok:",  get_guessed_word(secret_word, letters_guessed))
                print("---------------")
                if harf in ünlü_harfler:
                    tahmin_hakkı-=2
                else:
                    tahmin_hakkı-=1
                

           
    if tahmin_hakkı==0:
       print("Üzgünüm, tahminleriniz tükendi. Kelime başkaydı.Kelimemiz:", secret_word)






def match_with_gaps(my_word, other_word):
    '''
    my_word: _ karakterli dize, gizli kelimenin geçerli tahmini
    other_word: string, normal İngilizce kelime
    returns: boolean, True, eğer my_word'ün tüm gerçek harfleri other_word'ün karşılık gelen harfleriyle eşleşiyorsa veya harf özel sembol _ ise ve my_word ile other_word aynı uzunluktaysa; Aksi takdirde False:
    '''
# BURAYA KODUNUZU GİRİN VE "pass"ı SİLİN
    my_word=my_word.replace(" ","")
    if len(my_word) != len(other_word):
        return False
    
    for i in range(len(my_word)):
        if my_word[i] == '_':
            if other_word[i] in my_word:
                return False
        elif my_word[i] != other_word[i]:
            return False
    return True



def show_possible_matches(my_word):
    '''
    my_word: _ karakterli dize, gizli kelimenin geçerli tahmini
    returns: hiçbir şey, ancak kelime listesindeki my_word ile eşleşen
        her kelimeyi yazdırmalıdır.
    adamAsmaca ile bir harf tahmin edildiğinde, o harfin gizli kelimede
        geçtiği tüm pozisyonların ortaya çıktığını unutmayın.
    Bu nedenle, gizli harf(_ ) zaten ortaya çıkmış olan kelimedeki
     harflerden biri olamaz.
    '''
    sayaç=0
    for word in wordlist:
        if match_with_gaps(my_word, word):
            sayaç+=1
            print(word)
    if sayaç==0:
        print("Hiçbir sonuç bulunamadı")



def adamAsmaca_ipuclu(secret_word):
    '''
    secret_word: string, tahmin edilecek gizli kelime.
    
     Etkileşimli bir Adam Asmaca oyunu başlatır.
    
     * Oyunun başında, kullanıcıya secret_word'ün kaç harf içerdiğini ve
        kaç tahminle başladığını bildirin.
      
     * Kullanıcı 6 tahminle başlamalıdır
    
     * Her turdan önce kullanıcıya kaç tahmin kaldığını ve kullanıcının
        henüz tahmin etmediği harfleri göstermelisiniz.
    
     * Kullanıcıdan tur başına bir tahmin vermesini isteyin.
        Kullanıcının bir harf tahmin ettiğini kontrol ettiğinizden emin olun.
      
     * Kullanıcı, her tahminden hemen sonra tahminlerinin bilgisayarın
        kelimesinde görünüp görünmediği hakkında geri bildirim almalıdır.

     * Her tahminden sonra, o ana kadar kısmen tahmin edilen kelimeyi
         kullanıcıya göstermelisiniz.
      
     * Tahmin sembolü * ise, kelime listesindeki mevcut tahmin edilen
        kelimeyle eşleşen tüm kelimeleri yazdırın.
    
     Problem yazımında detaylandırılan diğer sınırlamaları takip eder.
    '''

    print("Kelimeniz",len(secret_word)," harfilidir.")
    tahmin_hakkı=6
    letters_guessed=[]
    uyarı=3
    number_unique_letters=0
    ünlü_harfler='aeiou' 
    print("Kullanılabilir harfler:",get_available_letters(letters_guessed))
    print("---------------")
    while tahmin_hakkı>0:
        print(f"Tahmin hakkınız {tahmin_hakkı}'dır")
        harf=input("Bir harf tahmin ediniz:")
        
        if harf=="*":
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            

    
        if str.isalpha(harf)==False:
            if harf!="*":
                uyarı-=1
                print("Hata! Bu geçerli bir harf değil.",uyarı,"uyarınız kaldı ")
                print("---------------")
                if uyarı==0:
                    tahmin_hakkı-=1
                    uyarı=3
                
        else:
            if harf not in get_available_letters(letters_guessed): 
                if str.islower(harf)==False:
                    harf=str.lower(harf)
                    uyarı-=1
                    print("Hata!Büyük harf kullandınız.",uyarı," uyarınız kaldı")
                    print("---------------")
                    if uyarı==0:
                        tahmin_hakkı-=1
                        uyarı=3
                        
                else:
                    uyarı-=1
                    print("Hata! Bu harfi zaten tahmin ettin.",uyarı," uyarınız kaldı ")
                    print("---------------")
                    if uyarı==0:
                        tahmin_hakkı-=1
                        uyarı=3
                    continue
                        
                    
            letters_guessed.append(harf)
            print("Kullanılabilir harfler: ", get_available_letters(letters_guessed))
            if harf in secret_word:
                print("İyi tahmin:", get_guessed_word(secret_word, letters_guessed))
                number_unique_letters+=1
                if is_word_guessed(secret_word, letters_guessed)==True:
                    print("Oyunu kazandınız.")
                    print("Bu oyun için toplam puanın:", tahmin_hakkı*number_unique_letters) 
                    break
                print("---------------")
            else:
                print("Hata! O harf bu kelimede yok:",  get_guessed_word(secret_word, letters_guessed))
                print("---------------")
                if harf in ünlü_harfler:
                    tahmin_hakkı-=2
                else:
                    tahmin_hakkı-=1
                

           
    if tahmin_hakkı==0:
       print("Üzgünüm, tahminleriniz tükendi. Kelime başkaydı.Kelimemiz:", secret_word)




if __name__ == "__main__":
    
    
    secret_word = choose_word(wordlist)
    adamAsmaca(secret_word)

###############
    

    #secret_word = choose_word(wordlist)
    #adamAsmaca_ipuclu(secret_word)
