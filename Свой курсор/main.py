import pygame
import os


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()
    return image


width = 500
height = 500
pygame.display.set_caption("Свой курсор мыши")
screen = pygame.display.set_mode((width, height))
running = True
pygame.mouse.set_visible(False)
screen.fill((0, 0, 0))
all_sprites = pygame.sprite.Group()
cursor = pygame.sprite.Sprite(all_sprites)
cursor.image = load_image('arrow.png')
cursor.rect = cursor.image.get_rect()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            cursor.rect.topleft = event.pos
    screen.fill((0, 0, 0))
    if pygame.mouse.get_focused():
        all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()