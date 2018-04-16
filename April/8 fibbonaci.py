# 0,1,1,2,3,5,8,13,21,34,55,89,134
def fibonacci(x):
    a = 0
    b = 1
    if x == 1:
        c = 0
    elif x == 2:
        c = 1
    while x > 2:
        c = a + b
        a = b
        b = c
        x = x - 1
    print(c)

n = int(input("What number of the fibonnaci series: "))
fibonacci(n)