# 71_first_letter_shift:

def shift_sentence(sentence):
    a = sentence.split()
    d = []
    f = []
    for i,j in enumerate(a[:-1]):
        d.append(j[0])
    d.insert(0,a[-1][0])
    for i,j in enumerate(a):
        f.append(d[i] + a[i][1:])
    print("{}".format(" ".join(f)))
    
shift_sentence("create a function")

