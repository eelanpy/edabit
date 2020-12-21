# 27_pig_latin_for_filename:

def pig_ltn_wrd(word):
    if word[0] in 'aeiou':
        return word[0] + 'way' + word[1:]
    else:
        return  word[1:] + word[0] + 'ay'


def pig_latin_files(filename):
    opened_file = open(filename)
    statement = ''
    for i in opened_file:
        print(pig_ltn_wrd(i))
            
    print(statement)

pig_latin_files('example_file.sh')