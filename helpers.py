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


def draw_info(screen, screen_width, screen_font, spaceship):
    speed_s = "{:.2e}".format(spaceship.speed)
    gamma_s = "{:.2e}".format(spaceship.get_gamma())
    xx_s = "{:.2e}".format(spaceship.position.x)
    yy_s = "{:.2e}".format(spaceship.position.y)
    vx_s = "{:.2e}".format(spaceship.velocity.x)
    vy_s = "{:.2e}".format(spaceship.velocity.y)
    speed_text = screen_font.render(str(f'sp: {speed_s}'), True, (0, 155, 0))
    gamma_text = screen_font.render(str(f'ga: {gamma_s}'), True, (0, 155, 0))
    xx_text = screen_font.render(str(f' x: {xx_s}'), True, (0, 155, 0))
    yy_text = screen_font.render(str(f' y: {yy_s}'), True, (0, 155, 0))
    vx_text = screen_font.render(str(f'vx: {vx_s}'), True, (0, 155, 0))
    vy_text = screen_font.render(str(f'vy: {vy_s}'), True, (0, 155, 0))

    draw_centered(speed_text, screen,(screen_width-speed_text.get_width(), speed_text.get_height()+10))
    draw_centered(gamma_text, screen,(screen_width-speed_text.get_width(), gamma_text.get_height()+60))
    draw_centered(vx_text, screen,(screen_width-vx_text.get_width(), vx_text.get_height()+110))
    draw_centered(vy_text, screen,(screen_width-vy_text.get_width(), vy_text.get_height()+160))
    draw_centered(xx_text, screen,(screen_width-xx_text.get_width(), xx_text.get_height()+210))
    draw_centered(yy_text, screen,(screen_width-yy_text.get_width(), yy_text.get_height()+260))