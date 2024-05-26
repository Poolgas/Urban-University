def single_root_words(root_words, *other_words):
    same_words = []
    for i in other_words:
        if (i.lower()).count(root_words.lower()) == 1 or (root_words.lower()).count(i.lower()) == 1:
            same_words.append(i)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablemet', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
