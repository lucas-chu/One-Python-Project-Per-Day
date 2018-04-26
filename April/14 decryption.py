# take a code, and encrypt it
# q => w and so on, shifted one right
import string

def caesar(plaintext, shift):
    plaintext = plaintext.lower()
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table1 = str.maketrans(alphabet, shifted_alphabet)
    print(plaintext.translate(table1))

def qwerty(plaintext,shift):
    plaintext = plaintext.lower()
    keyboard = 'qwertyuiopasdfghjklzxcvbnm'
    shifted_keyboard = keyboard[shift:] + keyboard[:shift]
    table2 = str.maketrans(keyboard, shifted_keyboard)
    print(plaintext.translate(table2))
# learn to import
def decaesar(code, x):
    code = code.lower()
    shift = -x
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table1 = str.maketrans(alphabet, shifted_alphabet)
    print(code.translate(table1))

def deqwerty(code, x):
    shift = -x
    keyboard = 'qwertyuiopasdfghjklzxcvbnm'
    shifted_keyboard = keyboard[shift:] + keyboard[:shift]
    table2 = str.maketrans(keyboard, shifted_keyboard)
    print(code.translate(table2))

print(len('npnyioelsqmnyunccverefpgithcgembfd'))
print(len('200809190919190913161205192102192009202120091514011404200805011419230518091920080523151804192102192009202120091514'))
caesar('ZKDW LV D IRUXP WZRXP SOXV WZRXP', -3)
