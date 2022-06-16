
import sys, pygame
from pygame.locals import *
from pygame.constants import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random


from load_models import *
import time
from tkinter import *
import tkinter as tk

def init():
    pygame.init()
    viewport = (800,600)
    surface = pygame.display.set_mode(viewport, OPENGL | DOUBLEBUF)
    glLightfv(GL_LIGHT0, GL_POSITION,  (-40, 200, 200, 100.0))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.5, 1.0))
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHTING)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)       
    glClearColor(19/255, 24/255, 98/255, 0.0)


log_rand_pos = -300
log2_rand_pos = -400
score = 0
counter_keep = 3


   
def revenge():
    global log_rand_pos, log2_rand_pos, counter_keep, score

    viewport = (800,600)

    # loading the objects

    #this is for the man
    man_obj_frame1 = OBJ('assets/man/man_000001.obj', swapyz=True)

    # loading the road model
    road_model = OBJ('assets/road/road.obj', swapyz=True)

    # loading the dinasour model
    dinasour_model = OBJ('assets/dinosaur/dinosaur.obj', swapyz=True)

    # loading the building model 
    building_model = OBJ('assets/building/building.obj', swapyz=True)

    # loading the moon model
    moon_model = OBJ('assets/moon/moon.obj', swapyz=True)

    # loading the tree logs
    tree_log_model = OBJ('assets/Tree_Logs/log.obj', swapyz=True)

    # loading the grass surface
    grass = OBJ('assets/Grass/grass.obj')

    # generating the objects
    man_obj_frame1.generate()
   
    road_model.generate()
    dinasour_model.generate()
    building_model.generate()
    moon_model.generate()
    tree_log_model.generate()
    grass.generate()

    # clock for pygame display
    clock = pygame.time.Clock()
    # setting opengl window
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    width, height = viewport
    gluPerspective(35.0, width/float(height), 1, 450.0)
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_MODELVIEW)

    # setting initial position for the game entities
    dina_pos =  -15.0
    man_ver_pos = -7.0
    man_frame_index = 0
    comp_man_ver_pos = -7.0
    time_comp = 0
    

    
    left_bld_pos = [-680, 580.0, -360.0, -230.0, -100.0]
    comp_left_bld_pos = [-820, 720.0, -660.0, -620.0, -500.0]
    right_bld_pos = [-600, 520.0, -360.0, -230.0, -100.0]
    comp_right_bld_pos = [-820, 720.0, -660.0, -580.0, -500.0]
    
    while 1:
        clock.tick(30)  
        for e in pygame.event.get():
            if e.type == QUIT:
                retry_window(score, "Quit?", "Cancel")
            elif e.type == KEYDOWN and e.key == K_UP:
                if man_ver_pos < 1:
                    man_ver_pos += 4
                    if log_rand_pos >= -130:
                        log_rand_pos += 30
                    if log2_rand_pos >= -130:
                        log2_rand_pos += 30
                else:
                    man_ver_pos = -7.0

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        font = pygame.font.SysFont('arial', 18)
        text_surface = font.render("score: " + str(score), True, (0,255,255,255), (0, 19, 24, 98))
        text_data = pygame.image.tostring(text_surface, "RGBA", True)
        glWindowPos2d(700, 550)
        glDrawPixels(text_surface.get_width(), text_surface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_data)


        #Rendering the road
        glTranslate(120.0, -30.0, 0.0)
        glRotate(90.0, 0.0, 1.0, 0.0)
        road_model.render()
        glRotate(90.0, 0.0, -1.0, 0.0)
        glTranslate(-120.0, 30.0, 0.0)

        glTranslate(120.0, -30.0, -310.0)
        glRotate(90.0, 0.0, 1.0, 0.0)
        road_model.render()
        glRotate(90.0, 0.0, -1.0, 0.0)
        glTranslate(-120.0, 30.0, 310.0)

        # Rendering tree logs
        glTranslate(-5.0, -15.0, log_rand_pos)
        glRotate(45.0, 0.0, 0.0, 1.0)
        glRotate(15.0, 0.0, -1.0, 0.0)
        tree_log_model.render()
        glRotate(15.0, 0.0, 1.0, 0.0)
        glRotate(45.0, 0.0, 0.0, -1.0) 
        glTranslate(5.0, 15.0, -1*log_rand_pos)

        glTranslate(-5.0, -15.0, log2_rand_pos)
        glRotate(45.0, 0.0, 0.0, 1.0)
        glRotate(15.0, 0.0, -1.0, 0.0)
        tree_log_model.render()
        glRotate(15.0, 0.0, 1.0, 0.0)
        glRotate(45.0, 0.0, 0.0, -1.0) 
        glTranslate(5.0, 15.0, -1*log2_rand_pos)

        # Rendering grass
        glTranslate(-4.0, -32.0,-440.0 )
        grass.render()
        glTranslate(4.0, 32.0, 440.0)
        glTranslate(-4.0, -32.0,-640.0 )
        grass.render()
        glTranslate(4.0, 32.0, 640.0)


        #Rendering the building
        glTranslate(120.0, -30.0, left_bld_pos[4])
        glRotate(85.0, 0.0, 1.0, 0.0)
        building_model.render()
        glRotate(85.0, 0.0, -1.0, 0.0)
        glTranslate(-120.0, 30.0, -1 * left_bld_pos[4])

        glTranslate(-120.0, -30.0, right_bld_pos[4])
        glRotate(85.0, 0.0, -1.0, 0.0)
        building_model.render()
        glRotate(85.0, 0.0, 1.0, 0.0)
        glTranslate(120.0, 30.0, -1 *  right_bld_pos[4])

        glTranslate(120.0, -30.0, left_bld_pos[3])
        glRotate(85.0, 0.0, 1.0, 0.0)
        building_model.render()
        glRotate(85.0, 0.0, -1.0, 0.0)
        glTranslate(-120.0, 30.0, -1 * left_bld_pos[3])

        glTranslate(-120.0, -30.0, right_bld_pos[3])
        glRotate(85.0, 0.0, -1.0, 0.0)
        building_model.render()
        glRotate(85.0, 0.0, 1.0, 0.0)
        glTranslate(120.0, 30.0, -1 * right_bld_pos[3])

        glTranslate(120.0, -30.0, left_bld_pos[2])
        glRotate(85.0, 0.0, 1.0, 0.0)
        building_model.render()
        glRotate(85.0, 0.0, -1.0, 0.0)
        glTranslate(-120.0, 30.0, -1 * left_bld_pos[2])

        glTranslate(-120.0, -30.0, right_bld_pos[2])
        glRotate(85.0, 0.0, -1.0, 0.0)
        building_model.render()
        glRotate(85.0, 0.0, 1.0, 0.0)
        glTranslate(120.0, 30.0, -1 * right_bld_pos[2])

        glTranslate(120.0, -30.0, left_bld_pos[1])
        glRotate(85.0, 0.0, 1.0, 0.0)
        building_model.render()
        glRotate(85.0, 0.0, -1.0, 0.0)
        glTranslate(-120.0, 30.0, -1 * left_bld_pos[1])

        glTranslate(-120.0, -30.0, right_bld_pos[1])
        glRotate(85.0, 0.0, -1.0, 0.0)
        building_model.render()
        glRotate(85.0, 0.0, 1.0, 0.0)
        glTranslate(120.0, 30.0, -1 * right_bld_pos[1])

        glTranslate(120.0, -30.0, left_bld_pos[0])
        glRotate(85.0, 0.0, 1.0, 0.0)
        building_model.render()
        glRotate(85.0, 0.0, -1.0, 0.0)
        glTranslate(-120.0, 30.0, -1 * left_bld_pos[0])

        glTranslate(-120.0, -30.0, right_bld_pos[0])
        glRotate(85.0, 0.0, -1.0, 0.0)
        building_model.render()
        glRotate(85.0, 0.0, 1.0, 0.0)
        glTranslate(120.0, 30.0, -1 *  right_bld_pos[0])

        #Rendering the man
        glTranslate(0.0, man_ver_pos, -40.0) 
        glRotate(90.0, -1.0, 0.0, 0.0) 
        man_frame_obj1.render()
        glRotate(90.0, 1.0, 0.0, 0.0)  
        glTranslate(0.0, -1*man_ver_pos, 40.0)  

        #Rendering the dinosaur
        glTranslate(0.0, -7.0, dina_pos)  
        glRotate(5.0, 1.0, 0.0, 0.0)
        dinasour_model.render() 
        glRotate(5.0, -1.0, 0.0, 0.0)
        glTranslate(0.0, 7.0, -1*dina_pos) 

        #Rendering the moon
        glTranslate(15.0, 18.0, -70.0)  
        moon_model.render() 
        glTranslate(-15.0, -18.0, 70.0) 
        
        # loop for the buildings to re-appear in the game screen
        for i in range(len(right_bld_pos)):
            right_bld_pos[i] += 3
        for i in range(len(left_bld_pos)):
            left_bld_pos[i] += 3

        pygame.display.flip()
        pygame.time.wait(20)

       

        
        # when the logs reach to the dinosaur's position we remove them from the screen
        if log_rand_pos >= -80:
            log_rand_pos = -1*random.randint(150, 300)
            score += 1
        log_rand_pos += 2
        if log2_rand_pos >= -80:
            log2_rand_pos = -1*random.randint(200, 350)
            score += 1
        log2_rand_pos += 2

        # when the game starts the dinosaur appears closer to the man
        # as time goes we need to give the man some space by moving the dinosaur backwards
        if dina_pos < -5:
                dina_pos += 0.05

        

        # while the position of the buildings is out of the viewport, we need to bring them back to their first position
        if left_bld_pos[0] >= -60:
            right_bld_pos = comp_right_bld_pos.copy()
            left_bld_pos = comp_left_bld_pos.copy()

        if man_ver_pos > comp_man_ver_pos:
            man_ver_pos = comp_man_ver_pos
            
        
        pygame.display.flip()


# initializing pygame and taking the created surface
init()

# passing the surface to the enviroment maker
revenge()
