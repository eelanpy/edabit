
def is_disarium(n):
		num_disarium = 0
		for i,j in enumerate(str(n)):
			num_disarium += int(j) ** int(i+1)
		print(num_disarium == n)

arg_is_disar =   [1, 518, 6, 135, 75, 876, 175, 466, 372, 598, 696, 89]
correct_value = [True, False, True, False, False, True, True, False, False, True, True, True]
dict_arg_true_false = {}

for i,j in enumerate(arg_is_disar):
    dict_arg_true_false[j] = correct_value[i]



print(dict_arg_true_false)