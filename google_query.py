from googlesearch import search
query = input("Enter your query: ")
for url in search(query, lang='en', stop=16):
	print(url)
