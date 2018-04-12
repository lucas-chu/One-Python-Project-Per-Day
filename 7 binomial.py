import math
# expand to polynomial
print("This will solve a binomial such that ax^2 + bx + c = 0")
a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
root1 = (-b + (b**2-4*a*c)**.5)/(2*a)
root2 = (-b - (b**2-4*a*c)**.5)/(2*a)
print("The roots of the equation are:")
print("{} and {}".format(root1,root2))