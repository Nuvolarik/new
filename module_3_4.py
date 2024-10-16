def single_root_words(root_word, *other_words):
    same_words = []

    root_word = root_word.lower()

    for same_word in other_words:
        if same_word.lower() in root_word or root_word in same_word.lower():
            same_words.append(same_word)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)