# 52_remove_vowels:

def remove_vow(str):
    new_word = []
    for i in str:
        if i not in 'aeiou':
            new_word.append(i)
    print("".join(new_word))

remove_vow("Hello world")
