from random import choice 

#list_1 = [i for i in range(65, 89)]
#list_2 = [i for i in range(97, 122)]


def gen_name(num):
	i = 0
	while i < num:
		s = ''
		for x in range(0, 3):
			s += chr(choice(range(65, 91)))
			s += chr(choice(range(97, 123))) * 6
			s += ' '

		yield s
		i += 1
		
result = [i for i in gen_name(10)]
print(result)
