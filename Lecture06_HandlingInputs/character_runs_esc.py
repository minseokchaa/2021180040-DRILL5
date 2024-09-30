from pico2d import *

open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')


running = True



def handle_events():
  global running                    #밖에 있는 running 과 안에 있는 running을 같다고 알려주는 것.
                                    #안 적으면 안에 있는 running은 지역변수가 되어 밖에 있는 running에 영향을 주지 못한다.
  events = get_events()             #키 입력
  for event in events:
      if event.type == SDL_QUIT:
          running = False
      elif event.tpye == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
          running = False




frame = 0
for x in range(0, 800, 5):

    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 100, 100, 100, x, 90)
    update_canvas()

    handle_events()
    if not running:      #running 값이 false가 되면 for 문을 벗어난다.
        break



    frame = (frame + 1) % 8
    delay(0.05)


close_canvas()
