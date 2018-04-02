import os
import pyperclip

x = input("What would you like to capsize: ")
x = " ".join(x.upper().split(" "))
print(x)
string = ''
for n in range(0, len(x)):
    string += x[n]
    string += ' '
print(string)

os.system('cls')
pyperclip.copy(string)
input()