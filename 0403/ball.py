import PySimpleGUI as sg
import pymunk
import random

"""
    Demo that shows integrating PySimpleGUI with the pymunk library.  This combination
    of PySimpleGUI and pymunk could be used to build games.
    Note this exact same demo runs with PySimpleGUIWeb by changing the import statement
"""

class Ball():
    def __init__(self, x, y, r, *args, **kwargs):
        mass = 10
        self.body = pymunk.Body(mass,
                                pymunk.moment_for_circle(mass, 0, r, (0, 0)))  # Create a Body with mass and moment
        self.body.position = x, y
        self.shape = pymunk.Circle(self.body, r, offset=(0, 0))  # Create a box shape and attach to body
        self.shape.elasticity = 0.99999
        self.shape.friction = 0.8
        self.gui_circle_figure = None

space = pymunk.Space()
space.gravity = 0, 200

# ground
ground_body = pymunk.Body(body_type=pymunk.Body.STATIC)
ground_shape = pymunk.Segment(ground_body, (0, 400), (600, 400), 0.0)
ground_shape.friction = 0.8
ground_shape.elasticity = .99
space.add(ground_shape)
#left side
side_body = pymunk.Body(body_type=pymunk.Body.STATIC)
side_body = pymunk.Segment(side_body, (0, 0), (0, 400), 0.0)
side_body.friction = 0.8
side_body.elasticity = .99
space.add(side_body)
# right side
side_body2 = pymunk.Body(body_type=pymunk.Body.STATIC)
side_body2 = pymunk.Segment(side_body2, (400, 0), (600, 400), 0.0)
side_body2.friction = 0.8
side_body2.elasticity = .99
space.add(side_body2)

# -------------------  Build and show the GUI Window -------------------
graph_elem = sg.Graph((600, 400), (0, 400), (600, 0), enable_events=True, key='_GRAPH_', background_color='lightblue')
layout = [[sg.Text('Ball Test')],
          [graph_elem],
          [sg.Button('Exit')]]

window = sg.Window('Window Title', layout, ).Finalize()

# Add balls
arena_balls = []
for i in range(1, 200):
    x = random.randint(0, 400)
    y = random.randint(0, 400)
    r = random.randint(1, 10)
    # x,y = 100,10
    ball = Ball(x, y, r)
    arena_balls.append(ball)
    space.add(ball.body, ball.shape)
    ball.gui_circle_figure = graph_elem.DrawCircle((x, y), r, fill_color='black', line_color='red')

# ------------------- GUI Event Loop -------------------
while True:  # Event Loop
    event, values = window.Read(timeout=0)
    # print(event, values)
    if event in (None, 'Exit'):
        break
    space.step(0.04)
    for ball in arena_balls:
        graph_elem.RelocateFigure(ball.gui_circle_figure, ball.body.position[0], ball.body.position[1])

window.Close()
