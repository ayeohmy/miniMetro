# events-example3.py
# Demos timer, mouse, and keyboard events

from Tkinter import *

def mousePressed(event):
    newCircleCenter = (event.x, event.y)
    canvas.data.circleCenters.append(newCircleCenter)
    redrawAll()

def keyPressed(event):
    if (event.char == "d"):
        if (len(canvas.data.circleCenters) > 0):
            canvas.data.circleCenters.pop(0)
        else:
            print "No more circles to delete!"
    elif (event.char == "p"):
        canvas.data.isPaused = not canvas.data.isPaused
    elif (event.char == "s"):
        doTimerFired()
    if (event.keysym == "Left"):
        moveLeft()
    elif (event.keysym == "Right"):
        moveRight()
    redrawAll()

def moveLeft():
    canvas.data.squareLeft -= 20

def moveRight():
    canvas.data.squareLeft += 20

def moveUp():
    canvas.data.squareTop -= 20

def moveDown():
    canvas.data.squareTop += 20

def doTimerFired():
    canvas.data.counter += 1
    if (canvas.data.counter % 5 == 0):
        if (canvas.data.squareFill == "green"):
            canvas.data.squareFill = "yellow"
        else:
            canvas.data.squareFill = "green"
    if (canvas.data.headingRight == True):
        if (canvas.data.squareLeft + canvas.data.squareSize > canvas.data.canvasWidth):
            canvas.data.headingRight = False
        else:
            moveRight()
    else:
        if (canvas.data.squareLeft < 0):
            canvas.data.headingRight = True
        else:
            moveLeft()
    if (canvas.data.headingDown == True):
        if (canvas.data.squareTop + canvas.data.squareSize > canvas.data.canvasHeight):
            canvas.data.headingDown = False
        else:
            moveDown()
    else:
        if (canvas.data.squareTop < 0):
            canvas.data.headingDown = True
        else:
            moveUp()
    redrawAll()

def timerFired():
    if (canvas.data.isPaused == False):
        doTimerFired()
    delay = 50 # milliseconds
    canvas.after(delay, timerFired) # pause, then call timerFired again

def redrawAll():
    canvas.delete(ALL)
    # draw the square
    canvas.create_rectangle(canvas.data.squareLeft,
                            canvas.data.squareTop,
                            canvas.data.squareLeft + canvas.data.squareSize,
                            canvas.data.squareTop + canvas.data.squareSize,
                            fill=canvas.data.squareFill)
    # draw the circles
    for circleCenter in canvas.data.circleCenters:
        (cx, cy) = circleCenter
        r = 20
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill="cyan")
    # draw the text
    canvas.create_text(150,20,text="events-example3.py")
    canvas.create_text(150,40,text="Mouse clicks create circles")
    canvas.create_text(150,60,text="Pressing 'd' deletes circles")
    canvas.create_text(150,80,text="Pressing 'p' pauses/unpauses timer")
    canvas.create_text(150,100,text="Pressing 's' steps the timer once")
    canvas.create_text(150,120,text="Left arrow moves square left")
    canvas.create_text(150,140,text="Right arrow moves square right")
    canvas.create_text(150,160,text="Timer changes color of square")

def init():
    canvas.data.squareLeft = 50
    canvas.data.squareTop = 50
    canvas.data.squareFill = "yellow"
    canvas.data.squareSize = 25
    canvas.data.circleCenters = [ ]
    canvas.data.counter = 0
    canvas.data.headingRight = True
    canvas.data.headingDown = True
    canvas.data.isPaused = False

def run():
    # create the root and the canvas
    global canvas
    root = Tk()
    canvasWidth = 300
    canvasHeight = 200
    canvas = Canvas(root, width=canvasWidth, height=canvasHeight)
    canvas.pack()
    # Set up canvas data and call init
    class Struct: pass
    canvas.data = Struct()
    canvas.data.canvasWidth = canvasWidth
    canvas.data.canvasHeight = canvasHeight
    init()
    # set up events
    root.bind("<Button-1>", mousePressed)
    root.bind("<Key>", keyPressed)
    timerFired()
    # and launch the app
    root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)

run()