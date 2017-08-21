import turtle

class Circle(object):
	def __init__(self,x,y,r):
		self.x = x
		self.y = y
		self.r = r

	@property
	def r(self):
		return self._r

	@r.setter
	def r(self, value):
		assert value > 0
		self._r = value

	@property
	def diameter(self):
		self._diameter = (2 * self._r)
		return self._diameter

	@property
	def perimeter(self):
		self._perimeter = 2 * 3.14 * self._r
		return self._perimeter

	@property
	def area(self):
		self._area = 3.14 * self._r**2
		return self._area

def display_circle(circle):
	turtle.penup()
	turtle.setx = circle.x
	turtle.sety = circle.y
	turtle.pendown()
	turtle.circle(circle.r)

def if_inside(circle,x,y):
	if (((circle.x-x)**2+(circle.y-y)**2)<circle.r**2):
		return True
	else:
		return False

def iterate_circle(x,y):
	for i in circle_array:
		display_circle(i)

def print_prop(x,y):
	for i in circle_array:
		if if_inside(i,x,y):
			print(i.x,i.y,i.r,i.diameter,i.perimeter,i.area)

if __name__ == '__main__':
	x = Circle(1,1,40)

	circle_array = [Circle(i*5,i*5,i*10) for i in range(1,10)]
	# display_circle(x)
	print(if_inside(x,1,2))

	for i in circle_array:
		display_circle(i)
		
	turtle.onscreenclick(print_prop)
	turtle.mainloop()
	