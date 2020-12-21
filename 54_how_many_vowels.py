# 54_how_many_vowels:

def count_vowels(str):
    count_vow = 0
    for i in str:
        if i in 'aeiou':
            count_vow += 1

    print("{} vowels in your string.".format(count_vow))

count_vowels("Celebration")