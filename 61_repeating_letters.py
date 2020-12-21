# 61_repeating_letters:

def repeat_lett(wrd):
    new_word = ''
    for i in range(len(wrd)):
       new_word = new_word + wrd[i] * 2
    print(new_word)

repeat_lett("congratulations")