import pygame

pygame.init()
print('Setup start')
# janela do jogo
window = pygame.display.set_mode(size=(600, 480))
print('Setup end')

print('Start loop')
while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # CLose window
            quit()  # end pygame
