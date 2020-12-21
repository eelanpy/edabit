# 12_sorting_a_string.py:

def str_sort(word):
    word = list(word)
    new_word = []

    while len(word) > 0:
        min = word[0]
        for i in word:
            if i <= min:
                min = i
        new_word.append(min)
        word.remove(min)
    return "".join(new_word)

print(str_sort('cba'))
assert str_sort('cba') == 'abc'