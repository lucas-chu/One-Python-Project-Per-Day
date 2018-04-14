# 1.The words at odd position should be reversed.
# 2.The words at even position should have all the vowels(in same order they appear in the word) at the beginning
# followed by the consonants.
import string
vowels = 'aeiou'
consonants = 'qwrtypsdfghjklzxcvbnm'

def scrappr(plaintext):
    list = plaintext.split()
    odd_words = list[0::2]
    for x in list:
        if x in odd_words:
            word = x[::-1]
        if x not in odd_words:
            v = x.strip(consonants)
            c = ''.join([c for c in x if c not in vowels])
            word = v + c
        print(word, end=' ')

scrappr('the quick brown fox jumped over the lazy dog')

