# 33_reverse_lines:

def reverse_lines(file):
    file2 = open(file)
    reversed_line = []
    for i in file2:
        reversed_line.append(i[::-1])
    print("\n".join(reversed_line))

reverse_lines("33_reverse_lines.py")