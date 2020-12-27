# 89_more_vote:

def majority_vote(list1):
    num_vote = {}
    for i in list1:
        if i not in num_vote:
            num_vote[i] = 1
        elif i in num_vote:
            num_vote[i] += 1
    big_vote = max(num_vote.values())
    # print("big_vote: ", big_vote)
    key_vote = []
    for i in num_vote.keys():
        if num_vote[i] == big_vote:
            key_vote.append(i)
    if len(key_vote) == 1:
        print(key_vote[0])
       
    else:
        print(None)
        
majority_vote(["A", "A", "B"]) 
# "A"

majority_vote(["A", "A", "A", "B", "C", "A"])
# "A"

majority_vote(["A", "B", "B", "A", "C", "C"])
# None