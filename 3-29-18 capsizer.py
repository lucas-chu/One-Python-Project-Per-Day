x = input()
def capsizer(x):
    x = str(x)
    x = x.upper()
    n = 0
    s = []
    for x in range (0,len(x)):
        s[n] = x[n]
        s.append(' ')
        n = n + 1
    return s
