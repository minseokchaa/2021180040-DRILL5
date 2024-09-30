from pico2d import*

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
running_girl = load_image('running_girl2.png')
idle_girl = load_image('idle_girl.png')

def handle_events():
    global alive
    global x, y
    global dir_x, dir_y, key_on

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            alive = False
        elif event.type == SDL_KEYDOWN:
            
            if event.key == SDLK_RIGHT:
                    dir_x += 1
                    key_on = 1

            elif event.key == SDLK_LEFT:
                    dir_x -= 1
                    key_on = 2

            elif event.key == SDLK_UP:
                    dir_y += 1
                    key_on = 3

            elif event.key == SDLK_DOWN:
                    dir_y -= 1
                    key_on = 4

            elif event.key == SDLK_ESCAPE:
                alive = False


        elif event.type == SDL_KEYUP:
            
            if event.key == SDLK_RIGHT:
                dir_x -= 1
                key_on = 0
                
            elif event.key == SDLK_LEFT:
                dir_x += 1
                key_on = 0
                
            elif event.key == SDLK_UP:
                dir_y -= 1
                key_on = 0
                
            elif event.key == SDLK_DOWN:
                dir_y += 1
                key_on = 0
    



def draw_girl(x,y):
   
    if key_on == 0:         #기본상태
        idle_girl.clip_draw(frame * 320, 0, 320, 320, x, y, 120, 120)

    elif key_on == 4:       #아래로
        running_girl.clip_draw(frame * 320, 960, 320, 320, x, y, 120, 120)

    elif key_on == 1:       #오른쪽
        running_girl.clip_draw(frame * 320, 650, 300, 300, x, y, 120, 120)

    elif key_on == 2:       #왼쪽
        running_girl.clip_draw(frame * 320, 320, 320, 320, x, y, 120, 120)

    elif key_on == 3:       #위쪽
        running_girl.clip_draw(frame * 320, 0, 320, 320, x, y, 120, 120)
    

        #running_girl을 running_girl = load_image('running_girl1.png')로 바꾸고
        
        #elif key_on == 1:       #오른쪽
        #running_girl.clip_draw(frame * 320, 640, 320, 320, x, y, 120, 120)으로 바꿔도 됨
           

alive = True
x = 800//2
y = 600//2
frame = 0
dir_x = 0
dir_y = 0
key_on = 0

while alive:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH//2, TUK_HEIGHT//2)
    draw_girl(x,y)
    
    update_canvas()
    handle_events()

    if 0 <= x + dir_x * 12 <= TUK_WIDTH:
        x += dir_x * 12
        
    if 0 <= y + dir_y * 12 <= TUK_HEIGHT:    
        y += dir_y * 12
    
    frame = (frame + 1)%4
    delay(0.15)



close_canvas()

#gg
    
