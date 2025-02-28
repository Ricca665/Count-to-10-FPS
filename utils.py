import pygame as pg

def render_text(screen, GAME_FONT, center, counter, fps):
    screen.fill((0,0,0))
    GAME_FONT.render_to(screen, center, str(counter), (255, 255, 255))
    GAME_FONT.render_to(screen, (0,0), str(fps), (255, 255, 255))
    pg.display.flip()