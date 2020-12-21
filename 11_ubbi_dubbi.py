# 11_ubbi_dubbi:

def ubbi_dubbi(word):
    new_word = ''
    for letter in word:
        if letter in 'aeiou':
            new_word +=  'ub' 
        new_word += letter  
    return new_word

print(ubbi_dubbi('milk'))

