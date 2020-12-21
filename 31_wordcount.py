# 31_word_count:

def word_cnt(file):
    lst = []
    for l in open(file):
        for w in l:
            lst.append(w)

    return len(lst)

print(word_cnt('running_file2.sh'))