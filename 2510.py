import matplotlib.pyplot as pt
import random
import time

def bubble(a):
	i = 0
	while i < len(a) - 1:
		j = 0
		while j < len(a) - 1 - i:
			if a[j] > a[j+1]:
				a[j], a[j+1] = a[j+1], a[j]
			j += 1
		i += 1
		
def quicksort(s):
	if len(s) <= 1:
		return s
	else:
		q = random.choice(s)
		l = []
		m = []
		r = []
		for elem in s:
			if elem < q:
				l.append(elem) 
			elif elem > q: 
				r.append(elem) 
			else: 
				m.append(elem)
		return quicksort(l) + m + quicksortr
	
	
times, ns = [], []
times2, ns2 = [], []

for n in range(100,5001,100):
	elements = [random.randrange(0,n) for _ in range(n)]
	t = time.time()
	bubble(elements)
	work_time = time.time()-t
	times.append(work_time)
	ns.append(n)
	
	t2 = time.time()
	bubble(elements)
	work_time = time.time()-t
	times2.append(work_time)
	print (n)
	
fig, ax = pt.subplots()
ax2 = ax.twinx()
ax = pt.plot(ns, times, label='Bubble', color='g')
ax2 = pt.plot (ns2, times2, label='Quick')
ax.text
pt.show()
