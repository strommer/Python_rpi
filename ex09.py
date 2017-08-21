import pickle
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

	def if_inside(self,x,y):
		if (((self.x-x)**2+(self.y+self.r-y)**2) < self.r**2):
			print(self.x,self.y,self.r,self.diameter,self.perimeter,self.area)
	
	def display(self):
		turtle.penup()
		print(self.x, self.y)
		turtle.goto(self.x,self.y)
		turtle.pendown()
		turtle.circle(self.r)
		turtle.penup()

	def properties(self):
		return ("circle",self.x,self.y,self.r,self.diameter,self.perimeter,self.area)

class Polygon(object):
	"""Creates a Polygon"""
	def __init__(self, list_cord):
		self.list_cord = list_cord

	@property
	def list_cord(self):
	    return self._list_cord

	@list_cord.setter
	def list_cord(self, value):
	    self._list_cord = value

	def if_inside(self,x,y):
		min_x, min_y = min(i[0] for i in self.list_cord), min(i[1] for i in self.list_cord)
		max_x, max_y = max(i[0] for i in self.list_cord), max(i[1] for i in self.list_cord)
		if (min_x <= x <= max_x) and (min_y <= y <= max_y):
			print("In polygon")

	def display(self):
		turtle.penup()
		turtle.setx = self.list_cord[0][0]
		turtle.sety = self.list_cord[0][1]

		turtle.pendown()
		for i in self.list_cord:
			turtle.goto(i)
		turtle.penup()

	def properties(self):
		return(i for i in self.list_cord)
			
		
class Rectangle(Polygon):
	def if_inside(self,x,y):
		min_x, min_y = min(i[0] for i in self.list_cord), min(i[1] for i in self.list_cord)
		max_x, max_y = max(i[0] for i in self.list_cord), max(i[1] for i in self.list_cord)
		if (min_x <= x <= max_x) and (min_y <= y <= max_y):
			print("In rectangle")


class Car_shape(Rectangle, Circle):
	"""Enter only the coordinates of the rectangle and 
		the radius of the wheels"""

	def __init__(self, list_cord, radius):
		self.list_cord = list_cord
		self.radius = radius

		self.rect = Rectangle(self.list_cord)
		self.circle1 = Circle(self.list_cord[0][0], self.list_cord[0][1]-2*self.radius, self.radius)
		self.circle2 = Circle(self.list_cord[3][0], self.list_cord[3][1]-2*self.radius, self.radius)
		self.shape_array = [self.rect, self.circle1, self.circle2]

	def display(self):
		for i in self.shape_array:
			i.display()

	def properties(self):
		return ([i.properties for i in self.shape_array])

	def if_inside(self,x,y):
		for i in self.shape_array:
			i.if_inside(x,y)


def print_prop(x,y):
	for i in array:
		if(i.if_inside(x,y)):
			print(i.properties)

if __name__ == '__main__':
	x = Circle(500,0,40)

	# array = [Circle(50,i*10,50) for i in range(1,3)]

	# turtle.speed(0)
	turtle.onscreenclick(print_prop)
	coords = [(50,0),(50,50), (0,50),(0,0)]
	coords2 = [(200,150),(200,0), (0,0)]
	y = Polygon(coords2)
	y.display()
	# for i in array:
	# 	i.display()

	array = []
	z = Car_shape(coords,10)
	array.append(y)
	array.append(z)
	z.display()

	turtle.onscreenclick(print_prop)
	turtle.mainloop()