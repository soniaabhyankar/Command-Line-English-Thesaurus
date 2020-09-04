import json
from difflib import get_close_matches

data = json.load(open('data.json'))


def translate(w):
    w = w.lower()
    words_list = data.keys()

    if w in data:
        return data[w]
    elif len(get_close_matches(w, words_list)) > 0:
        return "Did you mean '%s' instead?" % get_close_matches(w, words_list)[0]
    else:
        return 'The word does not exist. Please enter a valid word.'


word = input("Enter word: ")

print(translate(word))
