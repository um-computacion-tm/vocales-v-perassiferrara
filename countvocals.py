def count_vocals(word):
    tuple_vocals = ("a","e","i","o","u")
    result = {}
    for letter in word.lower():
        if letter in tuple_vocals:
            if letter not in result:
                result[letter] = 0
            result[letter] += 1
    return result