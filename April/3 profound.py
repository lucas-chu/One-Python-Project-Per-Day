# profound statement maker
"To move forward, one must take the first step"
import random
type = random.randint(1,2)
selector = random.randint (1,10)
verb = ['be', 'move', 'look', ' get', 'think', 'become', 'expand','focus' , 'run', 'advance', 'dream']
noun = ['','' ]
averb = [ ]
anoun = [ ]

def chooser(type):
    if type == 1:
        print("to {} {}, one must first {} {}".format(verb,noun,averb,anoun))
        break
    if type == 2:
        print("")