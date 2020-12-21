# 43_count_legs:

def legs_cnt(*legs):
    counter = 0
    for i in legs:
        counter += i

    print(counter)

legs_cnt(2,4)