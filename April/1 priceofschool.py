#Price per day to go to school calculator
c = int(input("Cost of tuition (without dollar sign or comma): "))
d = int(input("Days of school: "))
b = int(c/d)
print("Each day of tuition costs ${}".format(b))

e = int(input("Money do you spend extra on food compared to public school per month: "))
f = int(input("Money you spend for transportation per month: "))
g = int(10 * (e + f)/d)
print("Each day going to school costs {} for a grand total of {}".format(g, (g+b)))

