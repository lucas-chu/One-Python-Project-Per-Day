import random
#dOeS sTuFf tO yOuR wOrDs
#  first letter is lower case
# randomly upper or lower case
x = input("Enter what you want to sMaCk: ")
string = ''
for n in range(0, len(x)):
    y = random.randint(0,1)
    if y == 0:
        string += x[n].upper()
    else:
        string += x[n].lower()
print(string)