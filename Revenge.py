
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

def retry_window(score_display, message, btn):
    global log_rand_pos, log2_rand_pos, score, counter_keep
    window = Tk()
    window.wm_attributes('-type', 'splash')
    window.protocol('WM_DELETE_WINDOW', lambda: None) 
    window.geometry("300x150+550+300")
    window.configure(bg=("#%02x%02x%02x" % (19, 24, 98)))
    temp = tk.Frame(window)
    temp.pack(side='bottom')
    text = Label(temp, text=message)
    text.pack()
    score_dis = Label(temp, text=("Score: " + str(score_display)))
    score_dis.pack()    
    btn_retry = tk.Button(temp, text =btn, command = window.destroy)
    
    btn_retry.pack(side='left')
    btn_cancel = tk.Button(temp, text ="Quit", command = lambda: sys.exit())
    btn_cancel.pack(side='left')
    window.call('wm', 'attributes', '.', '-topmost', '1')
    log_rand_pos = -70.0
    log2_rand_pos = -70.0
    score = -2
    counter_keep = 3
    window.mainloop()

   
def revenge():
    global log_rand_pos, log2_rand_pos, counter_keep, score

    viewport = (800,600)

    # loading the objects

    #this is for the man....20 frames
    man_obj_frame1 = OBJ('assets/man/man_000001.obj', swapyz=True)
    man_obj_frame2 = OBJ('assets/man/man_000002.obj', swapyz=True)
    man_obj_frame3 = OBJ('assets/man/man_000003.obj', swapyz=True)
    man_obj_frame4 = OBJ('assets/man/man_000004.obj', swapyz=True)
    man_obj_frame5 = OBJ('assets/man/man_000005.obj', swapyz=True)
    man_obj_frame6 = OBJ('assets/man/man_000006.obj', swapyz=True)
    man_obj_frame7 = OBJ('assets/man/man_000007.obj', swapyz=True)
    man_obj_frame8 = OBJ('assets/man/man_000008.obj', swapyz=True)
    man_obj_frame9 = OBJ('assets/man/man_000009.obj', swapyz=True)
    man_obj_frame10 = OBJ('assets/man/man_000010.obj', swapyz=True)
    man_obj_frame11 = OBJ('assets/man/man_000011.obj', swapyz=True)
    man_obj_frame12 = OBJ('assets/man/man_000012.obj', swapyz=True)
    man_obj_frame13 = OBJ('assets/man/man_000013.obj', swapyz=True)
    man_obj_frame14 = OBJ('assets/man/man_000014.obj', swapyz=True)
    man_obj_frame15 = OBJ('assets/man/man_000015.obj', swapyz=True)
    man_obj_frame16 = OBJ('assets/man/man_000016.obj', swapyz=True)
    man_obj_frame17 = OBJ('assets/man/man_000017.obj', swapyz=True)
    man_obj_frame18 = OBJ('assets/man/man_000018.obj', swapyz=True)
    man_obj_frame19 = OBJ('assets/man/man_000019.obj', swapyz=True)
    man_obj_frame20 = OBJ('assets/man/man_000020.obj', swapyz=True)

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
    man_obj_frame2.generate()
    man_obj_frame3.generate()
    man_obj_frame4.generate()
    man_obj_frame5.generate()
    man_obj_frame6.generate()
    man_obj_frame7.generate()
    man_obj_frame8.generate()
    man_obj_frame9.generate()
    man_obj_frame10.generate()
    man_obj_frame11.generate()
    man_obj_frame12.generate()
    man_obj_frame13.generate()
    man_obj_frame14.generate()
    man_obj_frame15.generate()
    man_obj_frame16.generate()
    man_obj_frame17.generate()
    man_obj_frame18.generate()
    man_obj_frame19.generate()
    man_obj_frame20.generate()
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
    

    man_frame_list = [man_obj_frame1, man_obj_frame2, man_obj_frame3, man_obj_frame4, man_obj_frame5, man_obj_frame6, man_obj_frame7, man_obj_frame8,
                     man_obj_frame9, man_obj_frame10, man_obj_frame11, man_obj_frame12, man_obj_frame13, man_obj_frame14, man_obj_frame15,
                     man_obj_frame16, man_obj_frame17, man_obj_frame18, man_obj_frame19, man_obj_frame20
    ]
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
        man_frame_list[man_frame_index].render()
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

        # this code makes the counting when the player start playing or retry
        if counter_keep:
            font = pygame.font.SysFont('arial', 64)
            text_surface = font.render(str(counter_keep), True, (0,255,255,255), (0, 19, 24, 98))
            text_data = pygame.image.tostring(text_surface, "RGBA", True)
            glWindowPos2d(350, 350)
            glDrawPixels(text_surface.get_width(), text_surface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_data)
            pygame.display.flip()
            time.sleep(1)
            counter_keep -= 1

        # if the position of the logs and the man is equal, the it's game over
        # call the retry_window functio to display a tkinter window asking if the user wants to play again or quit
        if (log_rand_pos == -100.0 or log2_rand_pos == -100) and man_ver_pos == -7.0:
            retry_window(score, "GAME OVER!!!", "Retry")
        
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

        # changing the frames for the man
        if man_frame_index>= 19:
            man_frame_index= 1
        
        man_frame_index+= 1
        time_comp += 1

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
