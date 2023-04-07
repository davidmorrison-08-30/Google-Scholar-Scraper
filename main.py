from ScholarAPI import *
from AuthorID import *

author_name = input("Enter the author's name whose articles you would like to scrape: ")

author_id = GetAuthorId(author_name)

ScrapeGScholar(author_id)