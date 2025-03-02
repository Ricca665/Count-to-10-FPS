# import package pygame 
import pygame as pg
import pygame.freetype
from time import sleep
from utils import render_text

import argparse
import logging as lg

lg.basicConfig(level=lg.DEBUG)

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("--debug", help="Enable debug.", action="store_true")
args = parser.parse_args()

# Set window resolution to 1200 x 600
pg.init()
pg.font.init()

screen = pg.display.set_mode((1200, 600)) 
GAME_FONT = pygame.freetype.SysFont("ARIAL.TTF", 24)

pg.display.set_caption('Click to 10 FPS') 
clock = pg.time.Clock()

# Initial variables
fps = 60
counter = 0
red = (255, 0, 0)

# Ball settings
ball_radius = 40
ball_speed = [3, 3]  # Faster to make motion clearer at low FPS
ball_rect = pg.Rect(100 - ball_radius, 100 - ball_radius, ball_radius*2, ball_radius*2)

if args.debug:
    lg.debug("Initialization complete")

# Main loop
running = True
while running:
    screen.fill((0, 0, 0))  # Clear screen each frame

    center = screen.get_rect().center  # Get center of screen for text

    # Event handling
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:  # Lower FPS on click
            counter += 1
            fps = max(5, fps - 5)  # Minimum FPS 5
            if args.debug:
                lg.debug(f"Lowered FPS to {fps}")

    # Check if game over (counter hits 10)
    if counter > 9:
        render_text(screen, GAME_FONT, center, counter, fps)
        pg.display.flip()
        sleep(0.2)
        running = False
        break

    # Draw FPS and counter text
    render_text(screen, GAME_FONT, center, counter, fps)

    # Move ball
    ball_rect = ball_rect.move(ball_speed)

    # Ball bouncing off walls
    if ball_rect.left <= 0 or ball_rect.right >= 1200:
        ball_speed[0] = -ball_speed[0]
    if ball_rect.top <= 0 or ball_rect.bottom >= 600:
        ball_speed[1] = -ball_speed[1]

    # Draw the ball
    pg.draw.circle(screen, red, ball_rect.center, ball_radius)

    # Update screen
    pg.display.flip()

    # Cap frame rate
    clock.tick(fps)

if args.debug:
    lg.warning("Exiting...")

pg.quit()
