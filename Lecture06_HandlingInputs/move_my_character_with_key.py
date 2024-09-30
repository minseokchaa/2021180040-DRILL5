from pico2d import*

open_canvas()
ground = load_image('TUK_GROUND.png')
running_girl = load_image('running_girl.png')
idle_girl = load_image('idle_girl.png')

def handle_events():
    global running, alive
    global x, y
    global dir_x, dir_y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            alive = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
            elif event.key == SDLK_UP:
                dir_y += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1

                
            elif event.key == SDLK_ESCAPE:
                alive = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1
    
    pass

def draw_girl():
    
    pass


alive = True
x = 800//2
frame = 0
dir =0


while alive:
    clear_canvas()
    ground.draw(400,300,800,600)
    #running_girl.draw(400,300,200,200)
    #idle_girl.draw(400,500,200,50)
    #draw_girl()
    update_canvas()
    #handle_events()



close_canvas()
    
