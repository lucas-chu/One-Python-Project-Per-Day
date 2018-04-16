# Rock paper scissor versus bot
# random，smart, winner
score = [0,0]
while True:

def win(x):
    if x == p1:
        score += [1,0]
    if x == p2:
        score += [0,1]

def match(p1,p2):
    if p1==r:
        if p2 == p:
            win(p1)
        if p2 == s:
            win(p2)
    elif p1==p:
        if p2 == r:
            return p1
        if p2==s:
            return p2
    elif p1==s:
        if p2==p:
            return p1
        if p2==r:
            return p2
    elif win('tie')

r = 'rock'
p = 'paper'
s = 'scissor'
