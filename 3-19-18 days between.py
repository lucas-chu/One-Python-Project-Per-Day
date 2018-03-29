daysbetween = input()
def daysbetween(m1,d1,y1,m2,d2,y2):
    daysinmonths = [0,31,59,90,120,151,181,212,243,273,304,334,365];
    dm1 = daysinmonths[m1-1];
    dy1 = y1 * 365
    leap1=0
    if y1 % 4 == 0 and m1 <= 1:
        y1 -= 1
    if y1 % 4 == 0 and m1 == 2 and d1 <= 28:
        y1 -= 1
    while y1 >= 4:
        y1 = y1 - 4
        leap1 = leap1 + 1
    x = dy1 + dm1 + d1 + leap1

    dm2 = daysinmonths[m2-1];
    dy2 = y2 * 365

    leap2=0
    if y2 % 4 == 0 and m2 <= 1:
        y2 -= 1
    if y2 % 4 == 0 and m2 == 2 and d2 <= 28:
        y2 -= 1
    while y2 >= 4:
        y2 = y2 - 4
        leap2 = leap2 + 1
    y= dy2 + dm2 + d2 + leap2
    answer = y - x
    print(answer)