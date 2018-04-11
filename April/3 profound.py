# profound statement maker
"To move forward, one must take the first step"
import random
type = random.randint(1,2)

verb = ['live', 'move', 'look', 'get to be', 'think', 'become', 'believe', 'focus on being', 'advance', 'dream']
adj = ['forward', 'great', 'in power', 'good', 'victory', 'success', 'the very best']
averb = ["be", 'stay', 'have learned how to be', 'start', 'have had to be', 'ignore those that are', 'step back and go', 'step', 'paradigm-shift', 'show']
aadj = ['at the beginning', 'small', 'odd', 'different', 'at a loss', 'moving', 'forgiveness', 'backwards']

w = random.randint (0,9)
x = random.randint (0,6)
y = random.randint (0,10)
z = random.randint (0,6)

print("To {} {}, one must {} {}.".format(verb[w],adj[x],averb[y],aadj[z]))