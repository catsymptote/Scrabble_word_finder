from app.word_finder import Word_Finder


wf = Word_Finder()
search_phrase = input("Input search phrase:")
results = wf.search(search_phrase)
print(results)
