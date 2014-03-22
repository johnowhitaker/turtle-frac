#Same as fractastic.py but squeezed down to 20 lines

import turtle

max_iterations = 500
bob = turtle.Turtle()
bob.speed(0)

def mandel(zx, zy):
	z = zx + zy * 1j
	c = z
	for i in xrange(max_iterations):
		if abs(z) > 2.0: break
		z = z * z + c
	return i

def draw_plot(xstart, ystart, xsize, ysize, xa, xb, ya, yb):

	for y in range(ystart, ystart+ysize):
		#go to the beginning of a line
		bob.penup()
		bob.goto(xstart, y)
		bob.pendown()
		#go along, changing colour depending on mandel(x, y)
		for x in range(xstart, xstart+xsize):
			m = 1000*(1-mandel((x * (xb - xa) / xsize  + xa),(y * (yb - ya) / ysize  + ya))/float(max_iterations))
			bob.color((m-(10*int(m/10)))*0.1, (m-(100*int(m/100)))*0.01, (m-int(m/1000))/1000)
			bob.forward(1)

#The whole set:
draw_plot(0, 0, 100, 100, -2.0, 1.0, -1.5, 1.5)

#Zoomed in a bit:
#draw_plot(100, 0, 100, 100, -0.5, 0.25, -0.375, 0.375)

#Nice, really zoomed in:
#draw_plot(-300, -300, 500, 500, -0.2034, -0.1992, -0.8163, -0.8127)
