#04_pig_latin_word:

def pig_ltn_wrd(word):
    if word[0] in 'aeiou':
        return word + 'way'
    else:
        return  word[1:] + word[0] + 'ay'
    

print(pig_ltn_wrd('googled'))