from pico2d import*

open_canvas()
ground = load_image('TUK_GROUND.png')
girl = load_image('running_girl.png')

def handle_events():
    pass


running = True
x = 800//2
frame = 0
dir =0


while running:
    clear_canvas()
    ground.draw(400,300,800,600)
    girl.draw(400,300)
    #character.clip_draw(~~)
    update_canvas()
    #handle_events()



close_canvas()
    
