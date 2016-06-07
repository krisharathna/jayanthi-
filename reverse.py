from array import array

def reverse_array(letters, first=0, last=None):
    "reverses the letters in an array in-place"
    if last is None:
        last = len(letters)
    last -= 1
    while first < last:
        letters[first], letters[last] = letters[last], letters[first]
        first += 1
        last -= 1

def reverse_words(string):
    "reverses the words in a string using an array"
    words = array('c', string)
    reverse_array(words, first=0, last=len(words))
    first = last = 0
    while first < len(words) and last < len(words):
        if words[last] != ' ':
            last += 1
            continue
        reverse_array(words, first, last)
        last += 1
        first = last
    if first < last:
        reverse_array(words, first, last=len(words))
    return words.tostring()
