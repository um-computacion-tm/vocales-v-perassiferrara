def count_vocals(word):

    tuple_accents = ("á","é","í","ó","ú")
    tuple_vocals = ("a","e","i","o","u")
    result = {}
    
    word = word.lower()
    
    for i in range(len(tuple_vocals)):
        if tuple_accents[i] in word:
            word = word.replace(tuple_accents[i],tuple_vocals[i]) 

    for letter in word:
        if letter in tuple_vocals:
            if letter not in result:
                result[letter] = 0
            result[letter] += 1
    return result