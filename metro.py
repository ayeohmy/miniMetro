# events-example1-no-globals.py
# Demos timer, mouse, and keyboard events

# Search for "DK" in comments for all the changes
# required to eliminate globals.

# Fixing Git


from Tkinter import *
from Track import *
from Station import *

# The init function stores all important game data in the data struct
def init(canvas):
    canvas.data.isPaused = False
    canvas.data.gameSpeed = 1
    canvas.data.mouseText = "No mousePresses yet"
    canvas.data.keyText = "No keyPresses yet"
    canvas.data.timerText = "No timerFired calls yet"
    canvas.data.stationText = "No Stations yet"
    canvas.data.timerCounter = 0
    canvas.data.stations = []
    canvas.data.tracks = []
    initStations(canvas)
    initTracks(canvas)



def mousePressed(canvas, event):
    canvas.data.mouseText = "last mousePressed: " + str((event.x, event.y))
    redrawAll(canvas)

def keyPressed(canvas, event):
    # Pause Control:
    if (event.keysym == "space" or event.keysym == "p"):
        canvas.data.isPaused = not canvas.data.isPaused
    canvas.data.keyText = "The Game is Paused:" + str(canvas.data.isPaused)

    # Speed Control:
    # TODO: Remove the magic numbers
    if (event.keysym == "Left" and canvas.data.gameSpeed > 1):
        canvas.data.gameSpeed = canvas.data.gameSpeed - 1
    elif (event.keysym == "Right" and canvas.data.gameSpeed < 3):
        canvas.data.gameSpeed = canvas.data.gameSpeed + 1

    redrawAll(canvas)

def timerFired(canvas):
    if(canvas.data.isPaused == False):
        canvas.data.timerCounter += 1
        canvas.data.timerText = "timerCounter = " + str(canvas.data.timerCounter)
        redrawAll(canvas)

    # TODO: remove magic number
    delay = 60/canvas.data.gameSpeed # milliseconds
    def f():
        timerFired(canvas) # DK: define local fn in closure
    canvas.after(delay, f) # pause, then call timerFired again

def redrawAll(canvas): # DK: redrawAll() --> redrawAll(canvas)
    canvas.delete(ALL)
    # draw stations
    drawStations(canvas)
    #draw tracks

    # draw the text
    canvas.create_text(150,40,text=canvas.data.mouseText)
    canvas.create_text(150,60,text=canvas.data.keyText)
    canvas.create_text(150,80,text=canvas.data.timerText)
    canvas.create_text(150,100,text=canvas.data.gameSpeed)
    canvas.create_text(400, 120, text = str(canvas.data.stations))

###############################################################################
#                       P R I V A T E    H E L P E R                          #
#                             F U N C T I O N S                               #
###############################################################################

def initStations(canvas):
    canvas.data.stations.append(Station("square"))
    canvas.data.stations.append(Station("circle"))
    canvas.data.stations.append(Station("triangle"))

def initTracks(canvas):
    canvas.data.tracks.append(Track("#000000"))
    canvas.data.tracks.append(Track("#FFFFFF"))
    canvas.data.tracks.append(Track("#0F0F0F"))

def drawStations(canvas):
    stationText = ""
    for station in canvas.data.stations:
        stationText = stationText + str(station.shape) + " "
    canvas.create_text(150, 300, text = stationText)


###############################################################################
#                                  R U N                                      #
#                             F U N C T I O N S                               #
###############################################################################

def run():
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=800, height=600)
    canvas.pack()
    # Set up canvas data and call init
    class Struct: pass
    canvas.data = Struct()
    init(canvas) # DK: init() --> init(canvas)
    # set up events
    # DK: You can use a local function with a closure
    # to store the canvas binding, like this:
    def f(event): mousePressed(canvas, event)    
    root.bind("<Button-1>", f)
    # DK: Or you can just use an anonymous lamdba function,
    # like this:
    root.bind("<Key>", lambda event: keyPressed(canvas, event))
    timerFired(canvas) # DK: timerFired() --> timerFired(canvas)
    # and launch the app
    root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)

run()
