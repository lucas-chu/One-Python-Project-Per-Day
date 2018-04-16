from google import search
import requests

for url in search(ip, stop=10):
            r = requests.get(url)
            title = everything_between(r.text, '<title>', '</title>')
