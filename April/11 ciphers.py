# take a code, and encrypt it
# q => w and so on, shifted one right
import string

def caesar(plaintext, shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table1 = str.maketrans(alphabet, shifted_alphabet)
    print(plaintext.translate(table1))

def qwerty(plaintext,shift):
    keyboard = 'qwertyuiopasdfghjklzxcvbnm'
    shifted_keyboard = keyboard[shift:] + keyboard[:shift]
    table2 = str.maketrans(keyboard, shifted_keyboard)
    print(plaintext.translate(table2))

caesar('potato',22)
qwerty('encrypted',12)
