import pygame
import math
import os
        

def load_image_convert_alpha(filename):
    """Load an image with the given filename from the images directory"""
    return pygame.image.load(os.path.join('images', filename)).convert_alpha()


def load_sound(filename):
    """Load a sound with the given filename from the sounds directory"""
    return pygame.mixer.Sound(os.path.join('sounds', filename))


def draw_centered(surface1, surface2, position):
    """Draw surface1 onto surface2 with center at position"""
    rect = surface1.get_rect()
    rect = rect.move(position[0]-rect.width//2, position[1]-rect.height//2)
    surface2.blit(surface1, rect)


def rotate_center(image, rect, angle):
        """rotate the given image around its center & return an image & rect"""
        rotate_image = pygame.transform.rotate(image, angle)
        rotate_rect = rotate_image.get_rect(center=rect.center)
        return rotate_image,rotate_rect


def distance(p, q):
    """Helper function to calculate distance between 2 points"""
    return math.sqrt((p[0]-q[0])**2 + (p[1]-q[1])**2)


def draw_info(screen, screen_width, screen_font, planet, spaceship):
    speed_s = "{:.2f}".format(100*spaceship.get_speed_as_per_c())
    gamma_s = "{:.2f}".format(spaceship.get_gamma())
    xx_s = "{:.2e}".format(spaceship.position.x)
    yy_s = "{:.2e}".format(spaceship.position.y)
    vx_s = "{:.2e}".format(spaceship.velocity.x)
    vy_s = "{:.2e}".format(spaceship.velocity.y)
    sp_t = "{:.2f}".format(spaceship.object_time/365.0)
    pl_t = "{:.2f}".format(planet.object_time/365.0)

    speed_text = screen_font.render(str(f'speed [%c]: {speed_s}'), True, (0, 155, 0))
    gamma_text = screen_font.render(str(f'gamma: {gamma_s}'), True, (0, 155, 0))
    r_text = screen_font.render(str(f' r: ({xx_s}, {yy_s})'), True, (0, 155, 0))
    v_text = screen_font.render(str(f'v: ({vx_s}, {vy_s})'), True, (0, 155, 0))
    sp_text = screen_font.render(str(f'ship time (yrs):   {sp_t}'), True, (0, 155, 0))
    pl_text = screen_font.render(str(f'planet time (yrs): {pl_t}'), True, (0, 155, 0))


    draw_centered(speed_text, screen,(screen_width-speed_text.get_width(), speed_text.get_height()+10))
    draw_centered(gamma_text, screen,(screen_width-speed_text.get_width(), gamma_text.get_height()+60))
    # draw_centered(v_text, screen,(screen_width-v_text.get_width(), v_text.get_height()+110))
    # draw_centered(r_text, screen,(screen_width-r_text.get_width(), r_text.get_height()+160))

    draw_centered(sp_text, screen, (sp_text.get_width(), screen.get_height()-60))
    draw_centered(pl_text, screen, (pl_text.get_width(), screen.get_height()-110))

