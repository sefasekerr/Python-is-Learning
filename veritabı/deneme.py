import pygame


pygame.init()
width = 600
height = 400

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Benim İlk Pygame Pencerem")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # pencereyi kapatma
            running = False

    screen.fill((0, 50, 0))  # pencereyi maviye boyar
    pygame.display.flip()       # ekranı günceller