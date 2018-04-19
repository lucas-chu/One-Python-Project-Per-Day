from google import *
'''
GoogleResult:
    self.name # The title of the link
    self.link # The external link
    self.google_link # The google link
    self.description # The description of the link
    self.thumb # The link to a thumbnail of the website (NOT implemented yet)
    self.cached # A link to the cached version of the page
    self.page # What page this result was on (When searching more than one page)
    self.index # What index on this page it was on
'''
num_page = 3
query = input("This is my query: ")
search_results = google.search(query, num_page)