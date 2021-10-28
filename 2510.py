import random
import matplotlib.pyplot as pt
import time

def bubble(inp_list):
    for i in range(len(inp_list)):
        for k in range(len(inp_list)-1-i):
            if inp_list[k] > inp_list[k+1]:
                inp_list[k], inp_list[k+1] = inp_list[k+1], inp_list[k]
                
def quicksort(nums):
	if len(nums) <= 1:
		return nums
	else:
		q = random.choice(nums)
		s_nums = []
		m_nums = []
		e_nums = []
		for n in nums:
			if n < q:
				s_nums.append(n)
			elif n>q:
				m_nums.append(n)
			else:
				e_nums.append(n)
		return quicksort(s_nums) + e_nums + quicksort(m_nums)
 
 
times, nam = [], []
times_2, nam_2 = [], []

for n in range(100,3001,100):
 elements = [random.randrange(0,n) for _ in range(n)]
 elements_2 = elements.copy()
 t = time.time()
 bubble(elements)
 work_time = time.time()-t
 times.append(work_time)
 nam.append(n)
 
 t_2 = time.time()
 quicksort(elements_2)
 work_time_2 = time.time()-t_2
 times_2.append(work_time_2)
 nam_2.append(n)
 
 print (n)
 
fig, ax = pt.subplots()
ax2 = ax.twinx()
ax = pt.plot(nam, times, label='Bubble', color='b')
ax2 = pt.plot (nam_2, times_2, label='Quick', color='g')
fig = pt.title('Bubble, Quick')

pt.show()
