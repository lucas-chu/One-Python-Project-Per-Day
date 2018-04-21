from PIL import Image
from bs4 import BeautifulSoup
from googlesearch import hits, get_page
from multiprocessing import Process, Manager
import pytesseract, requests, mss, json, webbrowser, urllib, wikipedia, time, sys

googleapikey = "AIzaSyAvEnHZEX52CdbUeHpCAis5xHiNhf8gAwk"
monitor = {'top': 303, 'left': 1354, 'width': 471, 'height': 836}
replaces = [["|", "I"], ['\n', ' '], ['‘', '\''], ['“', '"'], ["”", '"']]


def clean(text):
	for i in replaces:
		text = text.replace(i[0], i[1])
	return " ".join(text.split( ))

def type1(q, a1, a2, a3, ret):
	r = BeautifulSoup(get_page("https://www.google.com/search?q="+urllib.parse.quote_plus(q)), 'lxml')
	open("text.html", "wb+").write(get_page("https://www.google.com/search?q="+urllib.parse.quote_plus(q)))
	if r.find_all("div", class_="KpMaL") != []:
		ans = str(r.find_all("div", class_="KpMaL")[0])
		o = ans.count(a1)
		t = ans.count(a2)
		th = ans.count(a3)
		if o > t and o > th:
			ret['type1'] = 1
		elif t > o and t > th:
			ret['type1'] = 2
		elif th > o and th > t:
			ret['type1'] = 3
		else:
			ret['type1'] = "error"
	elif r.find_all("div", class_="VBt9Dc hp-xpdbox") != []:
		ans = str(r.find_all("div", class_="VBt9Dc hp-xpdbox")[0])
		o = ans.count(a1)
		t = ans.count(a2)
		th = ans.count(a3)
		if o > t and o > th:
			ret['type1'] = 1
		elif t > o and t > th:
			ret['type1'] = 2
		elif th > o and th > t:
			ret['type1'] = 3
		else:
			ret['type1'] = "error"
	else:
		ret['type1'] = "error"

#MKC1te
def type2(q, a1, a2, a3, ret):
	r = str(get_page("https://www.google.com/search?q="+urllib.parse.quote_plus(q)))
	o = r.count(a1)
	t = r.count(a2)
	th = r.count(a3)
	#print(o)
	#print(t)
	#print(th)x
	if o > t and o > th:
		ret['type2'] = 1
	elif t > o and t > th:
		ret['type2'] = 2
	elif th > o and th > t:
		ret['type2'] = 3
	else:
		ret['type2'] = "error"

def type3(q, a1, a2, a3, ret):
	ores = hits(q+' "'+a1+'"')
	tres = hits(q+' "'+a2+'"')
	thres = hits(q+' "'+a3	+'"')
	if ores > tres and ores > thres:
		ret['type3'] = 1
	elif tres > ores and tres > thres:
		ret['type3'] = 2
	elif thres > ores and thres > tres:
		ret['type3'] = 3
	else:
		ret['type3'] = "error"

def wiki(q, a1, a2, a3, ret):
	page = ""
	for i in wikipedia.search(q):
		if i in q:
			page = i
	r = str(get_page("https://en.wikipedia.org/wiki/"+urllib.parse.quote_plus(page.replace(" ", "_"))))
	o = r.count(a1)
	t = r.count(a2)
	th = r.count(a3)
	#print(o)
	#print(t)
	#print(th)
	if o > t and o > th:
		ret['wiki'] = 1
	elif t > o and t > th:
		ret['wiki'] = 2
	elif th > o and th > t:
		ret['wiki'] = 3
	else:
		ret['wiki'] = "error"

def ocr(img):
	return clean(pytesseract.image_to_string(img, lang="eng"))


if __name__ == '__main__':
	man = Manager()
	output = man.dict()
	#with mss.mss() as sct:
	#	sct_img = sct.grab(monitor)
	#	img = Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX')
	#replace with input from screen capture
	img = Image.open(sys.argv[1])
	#img.save("out.png")

	width = img.size[0]
	height = img.size[1]

	question = ocr(img.crop((width/25, height/16*3, width-width/25, height/8*3)))
	a1 = ocr(img.crop((width/8, height*13/32, width-width/8, height*15/32)))
	a2 = ocr(img.crop((width/8, height*16/32, width-width/8, height*18/32)))
	a3 = ocr(img.crop((width/8, height*19/32, width-width/8, height*21/32)))

	print(question)
	print(a1)
	print(a2)
	print(a3)
	print("ocr done")
	#start = time.time()
	processes = []
	processes.append(Process(target=type1, args=(question,a1,a2,a3,output)))
	processes.append(Process(target=type2, args=(question,a1,a2,a3,output)))
	processes.append(Process(target=type3, args=(question,a1,a2,a3,output)))
	processes.append(Process(target=wiki, args=(question,a1,a2,a3,output)))
	for i in processes:
		i.start()
	for i in processes:
		i.join() 
	#end = time.time()
	#print(end-start)
	if output['type3'] != 'error':
		print("Type 3: "+str(output['type3']))
	if output['type1'] != 'error':
		print("Type 1: "+str(output['type1']))
	if output['type2'] != 'error':
		print("Type 2: "+str(output['type2']))
	if output['wiki'] != 'error':
		print("Wikipedia: "+str(output['wiki']))