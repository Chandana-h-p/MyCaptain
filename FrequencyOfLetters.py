
text = 'mississippi'

def dict(x):
    diction = {}
    for letter in x:
        diction[letter] = 1 + diction.get(letter, 0)
    return diction

def most_frequent(text):
    letters = [letter.lower() for letter in text if letter.isalpha()]
    diction = dict(letters)
    result = []
    for key in diction:
        result.append((diction[key], key))
    result.sort(reverse=True)
    for count, letter in result:
        print(letter, count)

most_frequent(text)
