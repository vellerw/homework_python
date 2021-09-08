from multiprocessing import Process

def loop_a():
	i = 2
	while i < 50:
		print(i)
		i = i + 2
print("a")

def loop_b():
	i = 1
	while i < 50:
		print(i)
		i = i + 1
		
print("b")

p1 = Process(target=loop_a)
p2 = Process(target=loop_b)

p1.start()
p2.start()
