x = input("What would you like to capsize: ")
x = " ".join(x.upper().split(" "))
for n in range(0,len(x)):
    print(x[n], end=' ')
