from pico2d import*

open_canvas()
ground = load_image('TUK_GROUND.png')
running_girl = load_image('running_girl.png')
idle_girl = load_image('idle_girl.png')

def handle_events():
    global running
    global x, y
    global dir_x, dir_y

    
    pass


running = True
x = 800//2
frame = 0
dir =0


while running:
    clear_canvas()
    ground.draw(400,300,800,600)
    running_girl.draw(400,300,200,200)
    idle_girl.draw(400,500,200,50)
    #character.clip_draw(~~)
    update_canvas()
    #handle_events()



close_canvas()
    
