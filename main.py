# Framework to use to have a window for showing the figure
import pygame
import matrix as mat
import math

# WINDOWS SIZE PARAMETERS
WIDTH = 800
HEIGHT = 600
SCALE = 100

angle = 0

# CONSTANTS
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)

SCREEN_CENTER = (WIDTH/2,HEIGHT/2)

# Figure vertices
cube = [
    [-1,1,-1],
    [1,1,-1],
    [1,-1,-1],
    [-1,-1,-1],
    [1,1,1],
    [-1,1,1],
    [-1,-1,1],
    [1,-1,1]
]

# Projection Matrix
projectionMat = [
    [1,0,0],
    [0,1,0],
    [0,0,0]
]



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
        if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE):
            running = False
    
    screen.fill(WHITE)

    # Render the cube vertices
    # X-axis Matrix Rotation
    rotateX = [
        [1,0,0],
        [0, math.cos(angle), -math.sin(angle)],
        [0, math.sin(angle), math.cos(angle)]
    ]

    # Y-axis Matrix Rotation
    rotateY = [
        [math.cos(angle), 0, math.sin(angle)],
        [0, 1, 0],
        [-math.sin(angle), 0, math.cos(angle)]
    ]

    # Z-axis Matrix Rotation
    rotateZ = [
        [math.cos(angle), -math.sin(angle),0],
        [math.sin(angle), math.cos(angle), 0],
        [0,0,1]
    ]


    angle += 0.01
    for i in range(8):
            rotatedPoint = mat.rotateMult(rotateX,cube[i])
            rotatedPoint = mat.matMult(rotateY,rotatedPoint)
            rotatedPoint = mat.matMult(rotateZ,rotatedPoint)
            projectedPoint = mat.matMult(projectionMat,rotatedPoint)
            # projectedPoint = mat.rotateMult(projectionMat,cube[i])
            x = projectedPoint[0][0]*SCALE + SCREEN_CENTER[0]
            y = projectedPoint[1][0]*SCALE + SCREEN_CENTER[1]
            pygame.draw.circle(screen, RED, (x,y), 5)
            pygame.draw.circle(screen, RED, (x,y), 5)

    # Render the cube edges

    # Show changes
    pygame.display.flip()
    clock.tick(60)



pygame.quit()
