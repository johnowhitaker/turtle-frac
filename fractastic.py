##############################################################################
#														                     #
#	"Fractastic - a tiny (~20 lines) program to draw the Mandelbrot set 	 #
#	or a subset of it. Written by mer for use in the Linux Voice competition.#
#	Feel free to use this as part of your entries and contact me with 		 #
#	any questions.												             #
#															                 #
#	Author: Jonathan Whitaker, johnowhitaker@gmail.com. 				     #
#															                 #
##############################################################################

import turtle

# change this to make it faster. Sadly this will mess with the colour and throw an error if it exceeds 1000 - but I'm sure you can fix that!
max_iterations = 500

#Initiate a turtle
bob = turtle.Turtle()

#Make it go as fast as it can
bob.speed(0)
bob.ht()

#calculate the number of iterations required before z excedes 2 for a certain coordinate
def mandel(x, y, xa, xb, ya, yb, xsize, ysize):
	# x, y - the starting point (lower left of the box)
	# xa, xb, ya, yb - the lower and upper limits to plot. Some good samples are at the end
	# xsize, ysize - the size to draw (in pixels)
	
	#the mandelbrot magic!!
	zy = y * (yb - ya) / ysize  + ya
	zx = x * (xb - xa) / xsize  + xa
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
			m = 1000*(1-mandel(x, y, xa, xb, ya, yb, xsize, ysize)/float(max_iterations))
			#This makes much more interesting colours, but is a little hard to understand.
			#Set the R, G and B components of the colour depending on the thousandths, hundredths and tenths in (i/max_iterations)
			#If you want a simpler version then comment out the following 5 lines and uncomment the sixth one
			colour_small = (m-(10*int(m/10)))*0.1 
			colour_medium = (m-(100*int(m/100)))*0.01
			colour_large = (m-int(m/1000))/1000
			colour = (colour_small, colour_medium, colour_large)
			bob.color(colour) #english spelling rules!
			#bob.colour(0.0, (mandel(x, y, xa, xb, ya, yb, xsize, ysize)/float(max_iterations)), 0.0)
			bob.forward(1)

#The whole set:
draw_plot(0, 0, 100, 100, -2.0, 1.0, -1.5, 1.5)

#Zoomed in a bit:
#draw_plot(100, 0, 100, 100, -0.5, 0.25, -0.375, 0.375)

#Nice, really zoomed in:
#draw_plot(-300, -300, 500, 500, -0.2034, -0.1992, -0.8163, -0.8127)
