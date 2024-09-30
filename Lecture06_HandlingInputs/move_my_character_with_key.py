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


def draw_girl(x,y):

    events = get_events()

    ax = x
    ay = y
    
    for event in events:
        if event.type == SDL_QUIT:
            alive = False
        elif event.type == SDL_KEYDOWN:         #키를 누르면 running애니메이션 출력
            if event.key == SDLK_RIGHT:
                running_girl.clip_draw(frame*100,100,100,100,ax,ay,150,150)
            elif event.key == SDLK_LEFT:
                running_girl.clip_draw(frame*100,100,100,100,ax,ay,150,150)
            elif event.key == SDLK_UP:
                running_girl.clip_draw(frame*100,100,100,100,ax,ay,150,150)
            elif event.key == SDLK_DOWN:
                running_girl.clip_draw(frame*100,100,100,100,ax,ay,150,150)          
            elif event.key == SDLK_ESCAPE:
                alive = False
                
        elif event.type == SDL_KEYUP:           #키를 때면 idle애니메이션 출력
            if event.key == SDLK_RIGHT:
                idle_girl.clip_draw(frame*100,100,100,100,ax,ay,150,150)
            elif event.key == SDLK_LEFT:
                idle_girl.clip_draw(frame*100,100,100,100,ax,ay,150,150)
            elif event.key == SDLK_UP:
                idle_girl.clip_draw(frame*100,100,100,100,ax,ay,150,150)
            elif event.key == SDLK_DOWN:
                idle_girl.clip_draw(frame*100,100,100,100,ax,ay,150,150)
    
    pass


alive = True
x = 800//2
y = 600//2
frame = 0
dir_x = 0
dir_y = 0

while alive:
    clear_canvas()
    ground.draw(400,300,800,600)
    idle_girl.draw(x,y)
    #draw_girl(x,y)
    update_canvas()
    handle_events()
    x += dir_x * 7
    y += dir_y * 7
    frame = (frame + 1)%4
    delay(0.05)



close_canvas()
    
