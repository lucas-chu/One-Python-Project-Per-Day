def stamps(x):
    f=t=o=0
    while x>5:
        x=x-5
        f=f+1
    while x>1:
        x=x-2
        t=t+1
    while x==1:
        x=x-1
        o=o+1
        break
    return (f,t,o)
