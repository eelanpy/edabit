#32_longest_word_per_file:

def find_longest_word(file):
    str = ''
    for l in open(file):
        for w in l.split():
            if len(w) > len(str):
                str = w

    print(str)

find_longest_word('running_file2.sh')