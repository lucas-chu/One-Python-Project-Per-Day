import os, random, zipfile, shutil

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""
def pause():
    programPause = input("Press the <ENTER> key to continue...")


os.makedirs("tmp")
os.chdir("tmp")
with zipfile.ZipFile("../r.saz", 'r') as z:
    z.extractall()

files = []
for v in os.listdir("raw"):
    if "_c.txt" in v:
        files.append(v)
print(files)
for v in files:
    data= ""
    with open("raw/"+v, "r") as f:
        data = f.read()
        f.close()
    data = data.replace("<complete>false</complete>", "<complete>true</complete>")
    total = int(find_between(data, "<number_of_challenges>", "</number_of_challenges>"))
    if total == '':
        break
    correct = total-random.randrange(0,round(total/10))
    data = data.replace("<score_skipped>"+find_between(data,"<score_skipped>","</score_skipped>")+"</score_skipped>", "<score_skipped>0</score_skipped>")
    data = data.replace("<score_correct>"+find_between(data,"<score_correct>", "</score_correct>")+"</score_correct>", "<score_correct>"+str(correct)+"</score_correct>")
    data = data.replace("<score_incorrect>"+find_between(data,"<score_incorrect>","</score_incorrect>")+"</score_incorrect>", "<score_incorrect>"+str(total-correct)+"</score_incorrect>")
    with open("raw/"+v, "w") as f:
        f.write(data)
with zipfile.ZipFile("../r.saz", 'w') as z:
    for v in os.listdir("../tmp"):
        z.write(v)
    for v in os.listdir("raw"):
        z.write("raw/"+v)
os.chdir("..")
shutil.rmtree("tmp")
