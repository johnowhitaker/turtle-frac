# This shows off the use of some of the methods in utils.py. Please do not steal my idea as this will be my enrty to the competition - just use this to see how some things work.
# the grass takes ages so I didn't do much but for a final render time is not an issue
import turtle

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

commands = [["W", "HELLO WORLD"],["F", 60], ["R", 60], ["REP", [["F", 60], ["R", 60]], 8], ["G", [-200, -200]], ["H", 90], ["S", 20], ["PU"], ["F", 60], ["PD"], ["R", 90], ["C", (0, 1, 0)], ["F", 100]]
bob = turtle.Turtle()
bob.speed(50)

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
		elif command[0] == "SF":	
			turt.begin_fill()
		elif command[0] == "EF":	
			turt.end_fill()
		elif command[0] == "W":
			turt.write(command[1], font=("eufm10", 16, "normal"))
		elif command[0] == "REP":
			i = 0
			while i <= command[2]:
				do_my_will(turt, command[1])
				i += 1
				
#Sky
do_my_will(bob, [["S", 1100], ["C", (0.4, 0.4, 1)], ["G", [0, 0]], ["S", 1]])

#grass for now
do_my_will(bob, [["S", 250], ["PU"], ["G", [-400, -80]], ["C", "green"], ["PD"], ["G", [400, -80]], ["S", 1]])
#grass for now
do_my_will(bob, [["S", 400], ["PU"], ["G", [0, 0]], ["C", "green"], ["PD"], ["G", [400, 0]], ["S", 1]])

#Black top and bottom
do_my_will(bob, [["C", "black"],["PU"], ["G", [-400, 290]],["PD"], ["S", 140], ["G", [400, 290]], ["PU"], ["G", [400, -300]], ["PD"], ["S", 60], ["G", [-400, -300]], ["S", 1], ["PU"]])

#text
do_my_will(bob, [["PU"], ["C", "white"], ["G", [-340, 220]], ["PD"], ["W", "'In a hole in the ground there lived a hobbit...'"], ["PU"]])

#door
do_my_will(bob, [["C", "yellow"],["PU"], ["G", [0, 20]],["PD"], ["S", 300], ["G", [200, 20]], ["PU"]])
do_my_will(bob, [["C", "green"],["PU"], ["G", [0, 20]],["PD"], ["S", 160], ["G", [-3, 25]], ["C", "brown"], ["S", 16],["G", [-3, 25]],["PU"]])
do_my_will(bob, [["C", "red"], ["S", 1],["PU"], ["G", [-75, 20]],["H", 180], ["PD"], ["REP", [["SF"], ["F", 25], ["R", 90], ["F",10], ["R", 90], ["F", 25], ["R", 90], ["F", 10],["EF"], ["R", 180], ["F", 10], ["R", 278]], 45]])

#window
do_my_will(bob, [["C", "grey"],["PU"], ["G", [143, 74]],["PD"], ["S", 47], ["G", [143, 75]], ["PU"]])
do_my_will(bob, [["C", "red"], ["S", 1],["PU"], ["G", [120, 70]],["H", 180], ["PD"], ["REP", [["SF"], ["F", 15], ["R", 90], ["F",7], ["R", 90], ["F", 15], ["R", 90], ["F", 7],["EF"], ["R", 180], ["F", 10], ["R", 294]], 15]])


#fence (sin(x) = (2.718281828459045**(x*1j)).imag, cos(x) = (2.718281828459045**(x*1j)).real
do_my_will(bob, [["G", [80, -280]], ["H", 90], ["C", "white"], ["S", 18], ["PD"]])
for i in xrange(30):
	do_my_will(bob, [["F",  (90+(20*(2.718281828459045**(((bob.pos()[0] + 400)*2*3.14159265/480)*1j)).real))], ["PU"], ["R", 180], ["F",  (90+(20*(2.718281828459045**(((bob.pos()[0] + 400)*2*3.14159265/480)*1j)).real))], ["R", 180], ["R", -90], ["F", 20], ["R", -270], ["PD"]])
bob.penup()
def grass(bbox, xint, yint, length, angle):
	for y in range(bbox[2], bbox[3], yint):
		#go to the beginning of a line
		bob.goto(bbox[0], (bbox[2]+(bbox[3]-y)))
		for x in range(bbox[0], bbox[1], xint):
			do_my_will(bob, [["G", [(x+int(rnd())/10000), (y+int(rnd())/10000)]], ["H", (70+(rnd()/800))], ["PD"], ["S", 2], ["C", ((0.5+rnd()/100000.0), 1.0, 0.2)]])
			for i in xrange(length):
				do_my_will(bob, [["R", (angle-rnd()/8500)], ["F", 1]])
			do_my_will(bob, [["PU"], ["G", [x+rnd()/10000, y+rnd()/10000]], ["H", ((70+(rnd()/800)))], ["PD"], ["C", ((0.2+rnd()/66000.0), 0.8, 0.4)], ["S", 1]])
			for i in xrange(length):
				do_my_will(bob, [["R", angle], ["F", 1]]) #angle or rnd()???
			do_my_will(bob, [["PU"], ["F", xint]])

bboxes = [[-250, -230, 0, 20], [-194, -187, 70, 80], [-187, -180, 15, 30]]
for bbox in bboxes:
	grass(bbox, 3, 5, 20, 2)
	
	
turtle.exitonclick()
