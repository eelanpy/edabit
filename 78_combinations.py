# 78_combinations:

def combinations(*items):
		counter = 1
		for i in items:
			counter *= i
		return counter

print(combinations(1,2,3,4,5,6,7))       