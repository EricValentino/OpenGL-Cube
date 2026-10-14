import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

edges = (
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 7), (7, 6), (6, 4),
    (0, 4), (1, 5), (2, 7), (3, 6)
)

surfaces = (
    (0, 1, 2, 3),
    (4, 5, 7, 6),
    (1, 5, 7, 2),
    (0, 4, 6, 3),
    (3, 2, 7, 6),
    (0, 1, 5, 4)
)

colors = (
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 1, 0),
    (1, 0, 1),
    (0, 1, 1)
)

def Cube():
    glBegin(GL_QUADS)
    for i, surface in enumerate(surfaces):
        glColor3fv(colors[i])
        for vertex in surface:
            glVertex3fv(vertices[vertex])
    glEnd()

    glColor3f(0, 0, 0)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    # Setup perspective
    gluPerspective(45, (display[0]/display[1]), 0.1, 100.0)
    glTranslatef(0.0, 0.0, -6)  # Move camera back so cube is visible
    glEnable(GL_DEPTH_TEST)

    clock = pygame.time.Clock()
    rot_x, rot_y = 0, 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glPushMatrix()
        glRotatef(rot_x, 1, 0, 0)
        glRotatef(rot_y, 0, 1, 0)
        Cube()
        glPopMatrix()

        rot_x = (rot_x + 1) % 360
        rot_y = (rot_y + 1) % 360

        pygame.display.flip()
        clock.tick(60)

        # Check for OpenGL errors
        error = glGetError()
        if error != GL_NO_ERROR:
            print("OpenGL Error:", gluErrorString(error))

    pygame.quit()

if __name__ == "__main__":
    main()