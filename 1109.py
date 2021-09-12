import random
import string
def create_str(width):
	l = [random.choice(string.ascii_letters) for i in range (width)]
	s = ''
	for el in l:
		s += el
	return s
#print(string.ascii_lowercase)
def count_str(s):
	big = 0
	small = 0
	for sym in s:
		if sym.isupper():
			big += 1
	else:
			small += 1
	if big > small:
		upper.append(i)
		return 1
	elif small>big:
		lower.append(i)
		return 0
	else:
		middle.append(i)
		return -1

	s = create_str(9)
up_num = (len(upper) / len(a)) * 100
low_num = (len(lower) / len(a)) * 100
mid_num = (len(middle) / len(a)) * 100

print(up_num)
print(low_num)
print(mid_num)
