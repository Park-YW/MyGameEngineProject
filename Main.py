import pygame
from Things import *
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Object import *
from OBB import *

camera_pos = [0.0, 5.0, 5.0]  # 카메라 위치
camera_target = [0.0, 0.0, 0.0]  # 카메라가 바라보는 점
camera_up = [0.0, 1.0, 0.0]  # 업 벡터


pygame.init()
screen_width = 1280
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Lights in OpenGL')
done = False
white = pygame.Color(255, 255, 255)
glMatrixMode(GL_PROJECTION)
gluPerspective(60, (screen_width / screen_height), 0.1, 100.0)
glMatrixMode(GL_MODELVIEW)
#glTranslatef(0.0, 0.0, -3.0)
glEnable(GL_DEPTH_TEST)
#glEnable(GL_LIGHTING)

#glLight(GL_LIGHT0, GL_POSITION, (5, 5, 5, 1))
#glLightfv(GL_LIGHT0, GL_AMBIENT, (1, 0, 1, 1))
#glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 0, 1))
#glLightfv(GL_LIGHT0, GL_SPECULAR, (0, 1, 0, 1))

gluLookAt(camera_pos[0], camera_pos[1], camera_pos[2],
              camera_target[0], camera_target[1], camera_target[2],
              camera_up[0], camera_up[1], camera_up[2])

glEnable(GL_LIGHT0)

# Change path name to suit your directory structure
meshes = []
cube1 = Cube(0,0.1,0)
#meshes.append(mesh)
cube2 = Cube(0,0,0)
cube2.Translation((1.1, 0.1, 0.1))
#point1.Translation((0, 0 ,1))
meshes.append(cube1)
meshes.append(cube2)

test = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        meshes[0].Translation((0,0,-0.1))
    if key[pygame.K_s]:
        meshes[0].Translation((0,0,0.1))
    if key[pygame.K_a]:
        meshes[0].Translation((-0.1,0,0))
    if key[pygame.K_d]:
        meshes[0].Translation((0.1,0,0))
    if key[pygame.K_q]:
        meshes[0].Translation((0,0.1,0))
    if key[pygame.K_e]:
        meshes[0].Translation((0,-0.1,0))
    
    if key[pygame.K_i]:
        meshes[0].Rotation('z', 5)
    if key[pygame.K_k]:
        meshes[0].Rotation('z', -5)
    if key[pygame.K_j]:
        meshes[0].Rotation('x', 5)
    if key[pygame.K_l]:
        meshes[0].Rotation('x', -5)
    if key[pygame.K_u]:
        meshes[0].Rotation('y', 5)
    if key[pygame.K_o]:
        meshes[0].Rotation('y', -5)

    #test
    if key[pygame.K_m]:
        test = True
    


    

    for models in meshes:
        models.Update()

    if check_obb_collision(meshes[0],meshes[1]):
        test = True
        print("충돌---------------------")
    else:
        test = False
        print("-----------------------------------")
    

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    

    
    #glBegin(GL_POLYGON)
    for models in meshes:
        models.draw(test)
    #glEnd()

    pygame.display.flip()
    pygame.time.wait(50)
pygame.quit()