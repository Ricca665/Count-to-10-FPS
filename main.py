# import package pygame 
import pygame as pg
import pygame.freetype
from time import sleep
from utils import render_text

import argparse
import logging as lg

lg.basicConfig(level=lg.DEBUG)

#We check for a debug flag, in that case we enable it
parser = argparse.ArgumentParser()
parser.add_argument("--debug", help="Enable debug.", type=bool)
args = parser.parse_args()

# Set window resolution to 1200 x 600
screen = pg.display.set_mode((1200, 600)) 
counter = 0

pg.init()
pg.font.init()

GAME_FONT = pygame.freetype.SysFont("ARIAL.TTF", 24)
if args.debug: lg.debug("Initialized")

# Set title
pg.display.set_caption('Click to 10 FPS') 
if args.debug: lg.debug("Setted title")

# Run
running = True
if args.debug: lg.debug("Now running...")

fps = 60
counter = 0

clock = pg.time.Clock()
if args.debug: lg.debug("Set clock")

while running:
    """Main function of the script"""
    events = pg.event.get() # Get events
    center = screen.get_rect().center # Get center of the screen to render counter

    for event in events:
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.MOUSEBUTTONDOWN: # In case we press the left mouse button we lower the fps
            counter += 1
            fps = fps-5
            if args.debug: lg.debug(f"lowering fps to {fps}")
            clock.tick(fps)

        """
           The render_text function is found in the utils.py file
           Imported at the start of the script
        """
        if counter > 9: # In case counter is bigger than 10 we render it and then quickly close it
            render_text(screen, GAME_FONT, center, counter, fps)
            sleep(0.2)
            running = False
            break
        else:
            render_text(screen, GAME_FONT, center, counter, fps)

 
if args.debug: lg.warning(f"Exiting...")

pg.quit() # Quit game