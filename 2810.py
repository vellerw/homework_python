import matplotlib.pyplot as pt
def draw():
	while True:
		if input('Continue')=='n':
			break
		else:
			xs = input('x: ')
			ys = input('y: ')
			color = input('Color: ')
			try:
				xs_int = [int(xs) for xs in xs.split()]
				ys_int = [int(ys) for ys in ys.split()]
				if color:
					pt.plot(xs_int, ys_int, color)
				else:
					pt.plot(xs_int, ys_int)
			except Exception as e:
				print(e)
	pt.show()
draw()

def draw_plots (*args, **kwargs):
	i = 1
	keys = kwargs.keys()
	for x,y in args:
		color = 'color_'+str(i)
		try:
			if color in keys:
				pt.plot(x,y, color = kwargs[color])
			else:
				pt.plot(x,y)
		except Exception as e:
			print(e)
		i += 1
	pt.show()	
draw_plots(([0,1,2,3,4,5],[5,4,3,2,1,0]), ([0,1,2,3,4,5],[0,1,2,3,4,5]), color_1 = 'red')


def draw_pie(*args):
	size, colors,labels = [], [], []
labels = 'Python','Film', 'Walk','Free.time','Sleep'
sizes = [60, 10, 15, 10, 5]
fig1, ax1 = pt.subplots()
ax1.pie(sizes, labels=labels)
ax1.axis('equal')
pt.show()


def draw_bar(*args, colors):
	x, y = [], []
	for xs, ys, color in args:
		x.append(xs)
		y.append(ys)
		colors.append(color)
	bars = pt.bar(x, y)
	if colors:
		for i in range(len(bars)):
			bars[i].set_color(colors[i])

draw_bar(([8, 18, 32]),([11, 25, 40]), colors =['yellow', 'green'])
pt.show()
