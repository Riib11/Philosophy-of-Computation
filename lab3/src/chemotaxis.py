from PIL import Image
from PIL import ImageDraw

import matplotlib.pyplot as plt
import numpy as np

from colors import COLORS
from la import *
from util import *
from tqdm import tqdm

from agent import Agent
from surface import *

################################################################################
# Parameters
################################################################################

# window
BG_COLOR = COLORS["white"]
UNIT     = 2
WIDTH    = 300
HEIGHT   = int(phi * WIDTH)

# file system
FILENAME   = "chemotaxi"
OUTPUT_DIR = "figures/"

# simulation
AGENTS = 50
STEPS  = 60
MARGIN = 0.15 # distance of nodes from border

# heat map mode
# HEAT_MODE = "FOOD"
# HEAT_MODE = "ENDPOINTS"
HEAT_MODE = "HISTOGRAM"

# heat map parameters
HEAT_CONTOUR_WIDTH = 20
HEAT_RESOLUTION    = 0.2
HEAT_BINS          = 50

# agent
AGENT_START_POSITION    = vec2([ phi*MARGIN * WIDTH, MARGIN * HEIGHT ])
AGENT_START_ORIENTATION = vec2([1,1]).normalized()

# food FOOD_SURFACE
FOOD_CENTER = vec2([ (1-phi*MARGIN) * WIDTH, (1-MARGIN) * HEIGHT ])
# FOOD_SURFACE = Cone(FOOD_CENTER)
FOOD_SURFACE = Laplace(FOOD_CENTER, r = 6)

# nodes
AGENT_START_NODE_SIZE = 20
AGENT_END_NODE_SIZE   = 5
FOOD_CENTER_NODE_SIZE = 20

def main():

  ################################################################################
  # Initialization
  ################################################################################

  image = Image.new("RGB", (UNIT*WIDTH, UNIT*HEIGHT), BG_COLOR)
  draw  = ImageDraw.Draw(image)

  ################################################################################
  # Setup Food Surface and Agent
  ################################################################################

  # each agent is initialized in the same way
  def make_agent():
    return Agent(FOOD_SURFACE, AGENT_START_POSITION, AGENT_START_ORIENTATION)

  attributes = {
    "agents"    : AGENTS,
    "steps"     : STEPS,
    "surface"   : FOOD_SURFACE.__class__.__name__,
    "heat-mode" : HEAT_MODE,
    "heat-res"  : HEAT_RESOLUTION
  }

  ################################################################################
  # Draw Surface
  ################################################################################

  def draw_nodes():
    # drawing nodes to indicate agent start and food center
    def draw_node(v, size, color):
      r = size/2
      v0, v1 = v - (r * vec2([1,1])), v + (r * vec2([1,1]))
      p0, p1 = UNIT*v0, UNIT*v1
      draw.ellipse([p0.tup(), p1.tup()], fill = color, outline = True)

    draw_node(FOOD_CENTER, FOOD_CENTER_NODE_SIZE, COLORS["red"])
    draw_node(AGENT_START_POSITION, AGENT_START_NODE_SIZE, COLORS["blue"])

  def draw_heat_food():
    print("[*] calculating heights")

    height_min = FOOD_SURFACE.height(vec2([0,0]))
    height_max = abs(height_min)

    heights = [
      FOOD_SURFACE.height(vec2([x,y])) + abs(height_min)
        for x in range(WIDTH)
        for y in range(HEIGHT) ]

    def height_to_color(height):
      x = int(255
        * (height+height_max) / height_max / HEAT_CONTOUR_WIDTH) \
        * HEAT_CONTOUR_WIDTH
      c = (255-x,255,255-x)
      return c

    # shade FOOD_SURFACE by density of food
    step = int(1/HEAT_RESOLUTION)
    for x in tqdm(range(0, WIDTH, step)):
      for y in range(0, HEIGHT, step):
        height = FOOD_SURFACE.height(vec2([x,y]))
        color = height_to_color(height)
        draw.rectangle(
          [(UNIT*x, UNIT*y), (UNIT*x + UNIT*step, UNIT*y + UNIT*step)],
          fill = color)

  ################################################################################
  # Process and Draw Agent Walks
  ################################################################################
  paths = []
  endpoints = []

  def process_walks(do_draw = True):
    if do_draw: print("[*] processing and drawing walks for agents")
    else: print("[*] processing walks for agents")

    def step_to_color(step_i):
      x = int(255 * step_i/STEPS)
      c = (x,0,255-x)
      return c

    for agent_i in tqdm(range(AGENTS)):
      def window_position(v): return (UNIT * v.int()).tup()

      # init agent
      agent = make_agent()

      # store previous window position
      prev_position = window_position(agent.position)

      # steps the agent and draws the corresponding line
      def step(step_i):
        nonlocal prev_position
        agent.step()
        new_position = window_position(agent.position)
        color = step_to_color(step_i)
        if do_draw: draw.line([prev_position, new_position], fill = color)
        prev_position = new_position

      # process all steps
      for step_i in range(STEPS): step(step_i)

      # save walk endpoint
      endpoints.append(agent.position)

  def draw_node_endponts():
    for ep in endpoints:
      # draw endpoint as filled rectangle
      r = AGENT_END_NODE_SIZE/2
      p0 = UNIT*(ep - r*vec2([1,1]))
      p1 = UNIT*(ep + r*vec2([1,1]))
      draw.rectangle([ p0.tup(), p1.tup() ], fill = COLORS["black"])


  ################################################################################
  # Draw Walk Endpoint Distribution
  ################################################################################

  def draw_heat_endpoints():
    print("[*] shading FOOD_SURFACE by endpoint distances")

    def ep_distance(v):
      return sum([ distance_between(v, ep) for ep in endpoints ])

    distance_max = ep_distance(vec2([0,0]))

    def distance_to_color(dist):
      x = int(
        255 * dist / distance_max
        / HEAT_CONTOUR_WIDTH) * HEAT_CONTOUR_WIDTH
      c = (x, 255, x)
      return c

    # shade endpoint distances
    step = int(1/HEAT_RESOLUTION)
    for x in tqdm(range(0, WIDTH, step)):
      for y in range(0, HEIGHT, step):
        dist = ep_distance(vec2([x,y]))
        color = distance_to_color(dist)
        # print(color)
        draw.rectangle(
          [ (UNIT*x, UNIT*y), (UNIT*x + UNIT*step, UNIT*y + UNIT*step) ],
          fill = color)

  ################################################################################
  # Write Results
  ################################################################################

  def write_image():

    file_suffix = "_" + "_".join \
      ([ str(k) + "=" + str(v)
         for k,v in attributes.items() ])
    fullname = OUTPUT_DIR+FILENAME+file_suffix+".jpg"

    print("[*] writing image: "+fullname)
    image.save(fullname)

  ################################################################################
  # 2D Histogram of Endpoints
  ################################################################################

  def histogram_endpoints():
    print("[*] creating histogram of endpoints")
    endpoints_x = []
    endpoints_y = []
    for ep in endpoints:
      endpoints_x.append(ep[0])
      endpoints_y.append(HEIGHT-ep[1])

    plt.figure(figsize=(8, 8*phi), dpi=80, facecolor='w')

    plt.hist2d(endpoints_x, endpoints_y,
      range = [(0, WIDTH), (0, HEIGHT)],
      bins = HEAT_BINS)

    plt.show()

  ################################################################################
  # Run in correct order
  ################################################################################

  if HEAT_MODE == "FOOD":
    draw_heat_food()
    process_walks()
    draw_nodes()
    # draw_node_endponts()
    write_image()

  elif HEAT_MODE == "ENDPOINTS":
    process_walks(do_draw = False)
    draw_heat_endpoints()
    draw_nodes()
    draw_node_endponts()
    write_image()

  elif HEAT_MODE == "HISTOGRAM":
    process_walks(do_draw = False)
    histogram_endpoints()

main()
