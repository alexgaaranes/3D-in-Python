# Framework to use to have a window for showing the figure
import pygame

# PARAMETERS
WIDTH = 800
HEIGHT = 600

WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)

# Shape vectors
cube = [[0,1,0],[1,1,0],[1,0,0],[0,0,0],[0,1,1],[0,0,1],[1,1,1],[1,0,1]]

# Setup pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
running = True

# Main program loop
while running:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(WHITE)

    # Render the cube vertices
    for i in range(7):
        pygame.draw.circle(screen, RED, [cube[i][0]*100+300,cube[i][1]*100+150], 5)

    # Render the cube edges
    # FRONT FACE
    pygame.draw.line(screen, BLACK, [cube[0][0]*100+300,cube[0][1]*100+150],[cube[1][0]*100+300,cube[1][1]*100+150])
    pygame.draw.line(screen, BLACK, [cube[1][0]*100+300,cube[1][1]*100+150],[cube[2][0]*100+300,cube[2][1]*100+150])
    pygame.draw.line(screen, BLACK, [cube[2][0]*100+300,cube[2][1]*100+150],[cube[3][0]*100+300,cube[3][1]*100+150])
    pygame.draw.line(screen, BLACK, [cube[3][0]*100+300,cube[3][1]*100+150],[cube[0][0]*100+300,cube[0][1]*100+150])


    # Show changes
    pygame.display.flip()



pygame.quit()
