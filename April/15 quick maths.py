from decimal import *
# 1 term
# derivatives
# indefinite integrals
# definite integrals
def derivative():
    coeff=Decimal(input("Enter the coefficient assuming there is one: "))
    exp=Decimal(input("Enter the exponent of the coefficient: "))
    if exp == 0:
        print("The derivative is: ", coeff)
    else:
        print("The derivative is: ", abs(coeff * exp), "x^", exp - 1, ")")

def fnint():
    coeff=Decimal(input("Enter the coefficient assuming there is one: "))
    exp=Decimal(input("Enter the exponent of the coefficient: "))
    if exp == -1:
        print("The indefinite integral is: ", coeff, "ln(x)")
    else:
        print("The indefinite integral is: ", coeff / exp, "x^", exp + 1)

derivative()
fnint()