import turtle
turtle.speed(8)

def selection_sort(list1):
	turtle.penup()
	turtle.hideturtle()
	turtle.sety(200)
	t1 = turtle.Turtle()
	t2 = turtle.Turtle()
	t1.penup()
	t2.penup()
	turtle.isvisible()
	turtle.left(90)
	t1.left(90)
	t2.left(90)
	for i in range(len(list1)):
		for j in range(len(list1)):
			if (list1[j] > list1[i]):
				list1[i],list1[j] = list1[j],list1[i]
			ty = turtle.ycor()-20
			t1.setx(i*18+2)
			t1.sety(ty)
			t2.sety(ty)
			turtle.sety(ty)
			t2.setx(j*18+2)
			turtle.write(list1,font = '24')			
			turtle.delay(50)
	return list1

if __name__ == "__main__":
	print(selection_sort([2,4,3,6,8]))
	turtle.mainloop()