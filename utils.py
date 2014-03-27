##########################################
#	A bunch of functions which might come in useful for the	      #
#	Linux Voice python competition. Note that none of them       #
#	use any external libraries apart from the turtle module. 	      #
#	Questions? email me: johnowhitaker@gmail.com		      #
#	Enjoy!										      #
##########################################

import turtle

#Initialize our turtle for use in the examples
bob = turtle.Turtle()

### RANDOM NUMBER GENERATOR ###
#Generates numbers randomly distributed between 0 and 32767 (7 lines)
#Stolen from rosetta code - look up LCG
def msvcrt_rand(seed):
	def rand():
		rand.seed = (214013*rand.seed + 2531011) & 0x7fffffff
		return rand.seed >> 16
	rand.seed = seed
	return rand
rnd = msvcrt_rand(50) #use any seed here, try Bens birthday for extra points!
#~ for i in xrange(150):
	#~ print rnd()

### COMMAND SHORTENER ###
# allows executing multiple commands on one line e.g. [["F", 60], ["PD"], ["REP", ["F", 20], ["R", 30]]]
# add your own special commands
# all following methods will include a version for this as well
def do_my_will(turt, commands):
	for command in commands:
		if command[0] == "F":
			turt.forward(command[1])
		elif command[0] == "R":
			turt.right(command[1])
		elif command[0] == "G":
			turt.goto(command[1][0], command[1][1])
		elif command[0] == "H":
			turt.seth(command[1])
		elif command[0] == "PU":
			turt.penup()
		elif command[0] == "PD":
			turt.pendown()
		elif command[0] == "S":
			turt.pensize(command[1])
		elif command[0] == "C":
			turt.color(command[1])
		elif command[0] == "W":
			turt.write(command[1], font=("eufm10", 16, "normal"))
		elif command[0] == "REP":
			i = 0
			while i <= command[2]:
				do_my_will(turt, command[1])
				i += 1

### MANDELBROT PLOTTER ###
# Draws the madelbrot set, or a subset of it, in a variety of colour schemes
# ****************REPLACE bob with your turtles name or add a turtle argument ***********************
# ->max_iterations is fairly self-explanatory - this will determine how fast it draws and how detailed the final plot will be.
# ->xa, xb, ya, yb - these define what portion of the mandelbrot set to draw. The full set is contained in -2, 1, -1.5, 1.5
#    but you can zoom in 10000000000000000000 times before this function will start giving problems...
# -> xstart, ystart, xsize and ysize determine how big the plot will be BUT it will not actually draw a plot withing these bounds - 
#     the actual box to be drawn is set by bbox. This allows you to draw adjacent boxes that match up where they overlap.
# -> bbox - the coords of where the box will be drawn (X1, X2, Y1, Y2)
# -> xint and yint allow you to move across and up in creative ways = see some of the examples.
def mandel(zx, zy):
	# Get the number of iterations before it escapes above two
	z = zx + zy * 1j
	c = z
	for i in xrange(max_iterations):
		if abs(z) > 2.0: break
		z = z * z + c
	return i
def draw_plot(xstart, ystart, xsize, ysize, xa, xb, ya, yb, bbox, xint, yint):
	bob.pensize(yint)
	for y in range(bbox[2], bbox[3], yint):
		#go to the beginning of a line
		bob.penup()
		bob.goto(bbox[0], y)
		bob.pendown()
		# go along, changing colour depending on mandel(x, y)
		# This way of doing it creates some cool effects, but can give wacky colours depending on max_iterations
		# its much simpler to set colour to (0, 1-(m/max_iterations), 0) or come up with your own method...
		# It can also be shortened further but then it would be unintelligible...
		for x in range(bbox[0], bbox[1], xint):
			m = 1000*(1-mandel((x * (xb - xa) / xsize  + xa),(y * (yb - ya) / ysize  + ya))/float(max_iterations))
			colour = ((m-(10*int(m/10)))*0.1, (m-(100*int(m/100)))*0.01, (m-int(m/1000))/1000)
			bob.color(colour) #english spelling rules! 
			bob.forward(xint)
#make the screen black
#do_my_will(bob, [["S", 1100], ["C", "black"], ["G", [0, 0]], ["S", 5]])
#examples - uncomment to run

#~ #draw the full set in high detail (takes quite a while...
#~ max_iterations = 500
#~ draw_plot(-200, -150, 200, 150, -2.0, 1.0, -1.5, 1.5, [0, 200, -0, 150], 1, 1)

#~ #draw a fun plot
#~ max_iterations = 100
#~ draw_plot(-400, -320, 800, 640, -0.2034, -0.1995, -0.8163, -0.8127, [-400, 400, -320, 340], 10, 10)

#~ #draw a fun plot with better colours
#~ max_iterations = 500
#~ draw_plot(-400, -320, 800, 640, -0.2034, -0.1995, -0.8163, -0.8127, [-400, 400, -320, 340], 10, 10)

### L-SYSTEM EXECUTOR ###
# L systems are a way of notating fractal generation in biological modelling.
# The following is a very basic L system interpreter
# THIS IS CURRENTLY RUBBISH, come back later...
bob.color("white")
def execute_L(turtle, state, command_array):
	saved_state = []
	for command in command_array:
		if command == "F" or command == "f":
			turtle.forward(10)
		elif command == "+":
			turtle.right(5)
		elif command == "-":
			turtle.right(355)
		elif command == "[":
			saved_state=[turtle.heading(), turtle.pos()]
		elif command ==  "]":
			turtle.goto(saved_state[1])
			turtle.seth(int(saved_state[0]))

bob.pensize(1)
for i in range(1, 444):
	bob.color((1-i/444.0), 0 , 0)
	bob.right((36+ i/100.0 + i%3.0))
	bob.forward((1+i/10.0))

turtle.exitonclick()





