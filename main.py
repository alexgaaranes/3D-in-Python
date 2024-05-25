# Framework to use to have a window for showing the figure
import pygame
import matrix as mat
import math

# WINDOWS SIZE PARAMETERS
WIDTH = 800
HEIGHT = 600
SCALE = 100

angle = 0.025    # Speed of rotation

# CONSTANTS
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
PINK = (255,105,180)
ORANGE = (255,165,0)
YELLOW = (255,255,0)
CYAN = (0,255,255)


# Variables
SCREEN_CENTER = (WIDTH/2,HEIGHT/2)
x_rot: bool = False
y_rot: bool = False
z_rot: bool = False
nx_rot: bool = False
ny_rot: bool = False
nz_rot: bool = False
first_boot: bool = True

# Figure vertices
cube = [
    [[-1],[1],[-1]],
    [[1],[1],[-1]],
    [[1],[-1],[-1]],
    [[-1],[-1],[-1]],
    [[1],[1],[1]],
    [[-1],[1],[1]],
    [[-1],[-1],[1]],
    [[1],[-1],[1]]
]

# Projection Matrix
projectionMat = [
    [1,0,0],
    [0,1,0],
    [0,0,0]
]

# Identity matrix
identity = [
    [1,0,0],
    [0,1,0],
    [0,0,1]
]

# Setup pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
running = True

# for i in range(8):
#     # Events
#     rotatedPoint = mat.matMult(identity,cube[i])
# Main program loop
while running:
    # Render the cube vertices
    # X-axis Matrix Rotation
    rotateX = [
        [1,0,0],
        [0, math.cos(angle), -math.sin(angle)],
        [0, math.sin(angle), math.cos(angle)]
    ]

    rotateNX = [
        [1,0,0],
        [0, math.cos(-angle), -math.sin(-angle)],
        [0, math.sin(-angle), math.cos(-angle)]
    ]

    # Y-axis Matrix Rotation
    rotateNY = [
        [math.cos(-angle), 0, math.sin(-angle)],
        [0, 1, 0],
        [-math.sin(-angle), 0, math.cos(-angle)]
    ]

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

    rotateNZ = [
        [math.cos(-angle), -math.sin(-angle),0],
        [math.sin(-angle), math.cos(-angle), 0],
        [0,0,1]
    ]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_a:
                ny_rot = True
            if event.key == pygame.K_d:
                y_rot = True
            if event.key == pygame.K_w:
                nx_rot = True
            if event.key == pygame.K_s:
                x_rot = True
            if event.key == pygame.K_e:
                z_rot = True
            if event.key == pygame.K_q:
                nz_rot = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                ny_rot = False
            if event.key == pygame.K_d:
                y_rot = False
            if event.key == pygame.K_w:
                nx_rot = False
            if event.key == pygame.K_s:
                x_rot = False
            if event.key == pygame.K_e:
                z_rot = False
            if event.key == pygame.K_q:
                nz_rot = False

    projectedPoints = []
    z_points = []
    for i in range(8):
        rotatedPoint = mat.matMult(identity,cube[i])
        
        screen.fill(WHITE)
        if x_rot:
            rotatedPoint = mat.matMult(rotateX,rotatedPoint)
        if nx_rot:
            rotatedPoint = mat.matMult(rotateNX,rotatedPoint)
        if y_rot:
            rotatedPoint = mat.matMult(rotateY,rotatedPoint)
        if ny_rot:
            rotatedPoint = mat.matMult(rotateNY,rotatedPoint)
        if z_rot:
            rotatedPoint = mat.matMult(rotateZ,rotatedPoint)
        if nz_rot:
            rotatedPoint = mat.matMult(rotateNZ,rotatedPoint)

        cube[i] = rotatedPoint
        z = rotatedPoint[2][0]
        #print(z)
        z_points.append(z)
        projectedPoint = mat.matMult(projectionMat,rotatedPoint)
        # projectedPoint = mat.rotateMult(projectionMat,cube[i])
        x = projectedPoint[0][0]*SCALE + SCREEN_CENTER[0]
        y = projectedPoint[1][0]*SCALE + SCREEN_CENTER[1]
        # pygame.draw.circle(screen, GREEN, (x,y), 5)
        projectedPoints.append((x,y))

    for j in range(len(projectedPoints)):
        pygame.draw.circle(screen, GREEN, projectedPoints[j], 5)

    # Render the cube edges
    pygame.draw.line(screen, BLACK, projectedPoints[0], projectedPoints[1])
    pygame.draw.line(screen, BLACK, projectedPoints[1], projectedPoints[2])
    pygame.draw.line(screen, BLACK, projectedPoints[2], projectedPoints[3])
    pygame.draw.line(screen, BLACK, projectedPoints[3], projectedPoints[0])
    pygame.draw.line(screen, BLACK, projectedPoints[0], projectedPoints[5])
    pygame.draw.line(screen, BLACK, projectedPoints[4], projectedPoints[5])
    pygame.draw.line(screen, BLACK, projectedPoints[5], projectedPoints[6])
    pygame.draw.line(screen, BLACK, projectedPoints[6], projectedPoints[7])
    pygame.draw.line(screen, BLACK, projectedPoints[7], projectedPoints[4])
    pygame.draw.line(screen, BLACK, projectedPoints[4], projectedPoints[1])
    pygame.draw.line(screen, BLACK, projectedPoints[3], projectedPoints[6])
    pygame.draw.line(screen, BLACK, projectedPoints[2], projectedPoints[7])

    if (z_points[0] > z_points[5]):
        pygame.draw.polygon(screen, RED, [projectedPoints[0], projectedPoints[1], projectedPoints[2], projectedPoints[3]])

        if (z_points[0] > z_points[4]):
            pygame.draw.polygon(screen, ORANGE, [projectedPoints[0], projectedPoints[5], projectedPoints[6], projectedPoints[3]])
            pygame.draw.polygon(screen, CYAN, [projectedPoints[7], projectedPoints[4], projectedPoints[1], projectedPoints[2]])
        else:
            pygame.draw.polygon(screen, CYAN, [projectedPoints[7], projectedPoints[4], projectedPoints[1], projectedPoints[2]])
            pygame.draw.polygon(screen, ORANGE, [projectedPoints[0], projectedPoints[5], projectedPoints[6], projectedPoints[3]])

        pygame.draw.polygon(screen, PINK, [projectedPoints[5], projectedPoints[6], projectedPoints[7], projectedPoints[4]])
    else:
        pygame.draw.polygon(screen, PINK, [projectedPoints[5], projectedPoints[6], projectedPoints[7], projectedPoints[4]])

        if (z_points[0] > z_points[4]):
            pygame.draw.polygon(screen, ORANGE, [projectedPoints[0], projectedPoints[5], projectedPoints[6], projectedPoints[3]])
            pygame.draw.polygon(screen, CYAN, [projectedPoints[7], projectedPoints[4], projectedPoints[1], projectedPoints[2]])
        else:
            pygame.draw.polygon(screen, CYAN, [projectedPoints[7], projectedPoints[4], projectedPoints[1], projectedPoints[2]])
            pygame.draw.polygon(screen, ORANGE, [projectedPoints[0], projectedPoints[5], projectedPoints[6], projectedPoints[3]])
            
        pygame.draw.polygon(screen, RED, [projectedPoints[0], projectedPoints[1], projectedPoints[2], projectedPoints[3]])
        
    first_boot = False
    # Show changes
    pygame.display.flip()
    clock.tick(60)



pygame.quit()