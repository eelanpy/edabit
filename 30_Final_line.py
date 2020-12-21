#30_Final line:

def final_lne(file):
    lines = open(file)
    lst = []
    for line in lines:
        lst.append(line)
    print(lst[-1])

final_lne(file='example_file.sh')
def final_lne1(file):
    lines =list(open(file))
    print(lines[-1])

final_lne1(file='example_file.sh')