#screensaver 

#Import Modules
import simplegui
import random

#global state
message = "Python"
position = [50,50]
width = 500
height = 500 
interval = 2000

#handler for text
def update(text):
	global message
	message = text
	
#handler for timer
def tick():
	x = random.randrange(0, width)
	y = random.randrange(0, height)
	position[0] = x
	position[1] = y

#handler to draw on canvas
def draw(canvas):
	canvas.draw_text(message, position, 36, "Green")
	
#create a frame
frame = simplegui.create_frame("Home", width, height)

#Register event handlers
text = frame.add_input ("Message:", update, 150)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, tick)

#start the frame animation 
frame.start()
timer.start()
