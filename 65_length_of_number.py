# 65_length_of_number:

def len_num(num):
    num_str = str(num)
    count_nums = 0
    for _ in num_str: 
        count_nums += 1
    print(count_nums)

len_num(10000000000000000000000000000000000000000000)
