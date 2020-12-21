#05_pig_latin_sentence:

def pig_ltn_wrd(word):
    if word[0] in 'aeiou':
        return word + 'way'
    else:
        return  word[1:] + word[0] + 'ay'

def pl_sentence(sentence):
    sentence = sentence.split()
    new_sentence = [pig_ltn_wrd(w) for w in sentence]
    print(" ".join(new_sentence))
    #print(new_sentence)

pl_sentence('bla bla bla')       
