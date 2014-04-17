import turtle
def mandel(zx, zy):
	z = zx + zy * 1j
	c = z
	for i in xrange(400): #max_iterations
		if abs(z) > 2.0: break
		z = z * z + c
	return i
def gen_strip_mandel(width, height):
	xstart, ystart, xsize, ysize, xa, xb, ya, yb = 0, 0, 800, 640, -0.2034, -0.1995, -0.8163, -0.8127
	img = []
	for y in range(height):
		row = []
		for x in range(width):
			m = 1000*(1-mandel((x * (xb - xa) / xsize  + xa),(y * (yb - ya) / ysize  + ya))/float(400)) #max ierations - CHANGE
			(r,g,b) = ((m-(10*int(m/10)))*0.1, (m-(100*int(m/100)))*0.01, (m-int(m/1000))/1000)
			row.append((int(r*255), int(g*255), int(b*255)))
		img.append(row)
	return img
def cos(x):
	return (2.718281828459045**(x*1j)).real
def depth_func(a, b):
	return (int(abs(255-(((((a-400)/30.0)*((a-400)/30.0)+((b-340)/30.0)*((b-340)/30.0))**0.5+3*cos((((a-400)/30.0)*((a-400)/30.0)+((b-340)/30.0)*((b-340)/30.0))**0.5)+5-3)*(14)))))		
def gen_stereogram(depth, strips=8, levels=48, zoom = 1):
	strip_width = len(depth[0])// (strips - 5)
	width = strip_width * strips
	height = len(depth)
	strip_pix = gen_strip_mandel(strip_width, height)
	img_pix2 = [[(0, 0, 0) for i in xrange(width)] for i in xrange(height)]
	for y in range(height):
		for x in range(strip_width):
			img_pix2[y][x] = strip_pix[y][x]
		for x in range(strip_width, strip_width*3):
			img_pix2[y][x] = img_pix2[y][x-strip_width]
		for x in range(len(depth[0])):
			depth_offset = round(depth[y][x] / 255.0 * levels) * zoom
			tx = x + strip_width*3
			img_pix2[y][tx] = img_pix2[y][int(tx-strip_width+depth_offset)]
		for x in range(strip_width*3 + len(depth[0]), width):
			img_pix2[y][x] = img_pix2[y][x-strip_width]
	return img_pix2
a = gen_stereogram([[int(depth_func(x, y)) for x in xrange(800)] for y in xrange(640)])
bob = turtle.Turtle()
turtle.tracer(8000)
for y in xrange(320):
	bob.penup()
	bob.goto(-400, y-160)
	bob.pendown()
	for x in xrange(800):
		bob.color(a[2*y][2*x+200][0]/255.0, a[2*y][2*x+200][1]/255.0, a[2*y][2*x+200][2]/255.0)
		bob.forward(1)
turtle.exitonclick()
