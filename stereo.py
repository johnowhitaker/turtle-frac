import turtle
#~ from matplotlib import pyplot as plt #<<<<<If you want to see results fast

#Generates numbers randomly distributed between 0 and 32767 (7 lines)
def msvcrt_rand(seed):
	def rand():
		rand.seed = (214013*rand.seed + 2531011) & 0x7fffffff
		return rand.seed >> 16
	rand.seed = seed
	return rand
rnd = msvcrt_rand(50) #use any seed here, try Bens birthday for extra points!

# Madelbrot function
def mandel(zx, zy):
	# Get the number of iterations before it escapes above two
	z = zx + zy * 1j
	c = z
	for i in xrange(400): #max_iterations
		if abs(z) > 2.0: break
		z = z * z + c
	return i

#Generate a matrix of a bit of the mandelbrot set to make the stereogram with. Random noise also works but this looks nice.
def gen_strip_mandel(width, height):
	xstart, ystart, xsize, ysize, xa, xb, ya, yb = 0, 0, 800, 800, -0.2034, -0.1995, -0.8163, -0.8127
	img = []
	for y in range(height):
		row = []
		for x in range(width):
			m = 1000*(1-mandel((x * (xb - xa) / xsize  + xa),(y * (yb - ya) / ysize  + ya))/float(400)) #max ierations - CHANGE
			(r,g,b) = ((m-(10*int(m/10)))*0.1, (m-(100*int(m/100)))*0.01, (m-int(m/1000))/1000)
			row.append((int(r*255), int(g*255), int(b*255)))
		img.append(row)
	return img	


# Function that may come in useful (remove at the end)
def cos(x):
	return (2.718281828459045**(x*1j)).real
	
def sin(x):
	return (2.718281828459045**(x*1j)).imag

def func(x, y):
	return ((int(125.5*rnd()/32767.0 + x/3), int(255*rnd()/32767.0), int(255*rnd()/32767.0)))

def depth_func(a, b):
	#Try different ones - any z = x(something)y(something) function will work. Make sure you scale it right
	#x, y = (a-400)/30.0, (b-300)/30.0
	#p = ((x*x+y*y)**0.5)+3*cos(((x*x+y*y)**0.5))+5
	#~ x, y = (a-400)/120.0, (b-300)/120.0
	#~ p = sin(x**2+y**2)/(abs(x*y)+1)
	#~ q = (p+1)*125
	x, y = (a-400)/30.0, (b-300)/30.0
	p = (x*x+y*y)**0.5+3*cos((x*x+y*y)**0.5)+5
	q = abs(255-((p-3)*(14)))
	#print q
	return (int(q))


	
def gen_depth():
	img = []
	for y in xrange(640):
		row = []
		for x in xrange(800):
			r = depth_func(x, y)
			row.append(int(r))

		img.append(row)
	#plt.matshow(img)
	#plt.show() #see a preview of the depth plot
	return img	

#different alternative, random noise with a bit of a gradient. Even plain randomness works but is hard on the eyes
def gen_strip(width, height):
	img = []
	for y in range(height):
		row = []
		for x in range(width):
			(r,g,b) = func(x, y)
			row.append((r, g, b))
		img.append(row)
	return img	


#The real work. Some stolen from a forgotten github repo called python stereogram something
def gen_stereogram(depth, strips=8, levels=48, zoom = 1):
	strip_width = len(depth[0])// (strips - 5)
	print strip_width
	width = strip_width * strips
	height = len(depth)


	strip = gen_strip_mandel(strip_width, height)	#replace with gen_strip for just random noise with a bit of a gradient
	strip_pix = strip

	depth = depth
	depth_pix = depth
	img_pix2 = []
	for y in xrange(height):
		row = []
		for x in xrange(width):
			row.append((0, 0, 0))
		img_pix2.append(row)
		
	for y in range(height):
		for x in range(strip_width):
			img_pix2[y][x] = strip_pix[y][x]
		
		for x in range(strip_width, strip_width*3):
			img_pix2[y][x] = img_pix2[y][x-strip_width]
		
		for x in range(len(depth[0])):
			depth_offset = round(depth_pix[y][x] / 255.0 * levels) * zoom
			tx = x + strip_width*3
			img_pix2[y][tx] = img_pix2[y][int(tx-strip_width+depth_offset)]
		
		for x in range(strip_width*3 + len(depth[0]), width):
			img_pix2[y][x] = img_pix2[y][x-strip_width]
		
	return img_pix2
#depth = Image.open(gen_depth()).load #to use an external depth map
a = gen_stereogram(gen_depth())
#~ p =plt.im_show(a)
#~ plt.show()

bob = turtle.Turtle()
turtle.tracer(8000)

for y in xrange(640):
	bob.penup()
	bob.goto(-400, y-320)
	bob.pendown()
	for x in xrange(800):
		bob.color(a[2*y][2*x+200][0]/255.0, a[2*y][2*x+200][1]/255.0, a[2*y][2*x+200][2]/255.0)
		bob.forward(1)
	
