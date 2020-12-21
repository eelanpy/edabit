# 57_unique_sort:

def unique_srt(list1):
    count_item = {}
    for i in list1:
        count_item[i] = 1
        if i in count_item:
            count_item[i] += 1
    print(sorted(count_item.keys()))

unique_srt([1,2,4,4,4,4,4,4,4,3])