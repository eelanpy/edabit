def change_to_question(string,n):
    new_str = ''
    for i in range(len(string)):
        if  i + 1 % n  == 0:
            new_str += '?'
        else:
            new_str += string[i]
    return new_str
print(change_to_question('david is the best',3 ))