import pgzrun
import text
import instructions
import manage_actors
import physics
import const


# screen size
WIDTH = const.WIDTH
HEIGHT = const.HEIGHT

#WIDTH = 1200
#HEIGHT = 600



# Global variables
state = "state_title"
cutscene_number = 1

# Global Constants
TOTAL_CUTSCENES = 2



# Global Rectangles
TITLESCREEN = Rect((250, 100, 800, 180))
INTRODUCTION = Rect((150, 300, 1100, 450))
PREVIOUS_BOX = Rect((840,520,140,40))
NEXT_BOX = Rect((1000,520,80,40))
SKIP_BOX = Rect((1100,520,80,40))
INSTRUCTIONS = Rect(200,100,800,400)
PLAY_BOX = Rect((1025, 520, 150, 40))




# Backgrounds
bg_0 = Actor("background_test", topleft=(0,0))
bg_1 = Actor("background_test", topleft=(const.WIDTH,0))
bg_list = [bg_0, bg_1]

# Marsmallow Obstacles
# I am making a change here
obs_list = []
obs_list.append(Actor("marshmallow", bottomleft=(100,const.HEIGHT)))
obs_list.append(Actor("marshmallow", bottomleft=(350,const.HEIGHT)))
obs_list.append(Actor("marshmallow", bottomleft=(650,const.HEIGHT)))
obs_list.append(Actor("marshmallow", bottomleft=(900,const.HEIGHT)))
obs_list.append(Actor("marshmallow", bottomleft=(1200,const.HEIGHT)))
obs_list.append(Actor("marshmallow", bottomleft=(1600,const.HEIGHT)))
obs_list.append(Actor("marshmallow", bottomleft=(2000,const.HEIGHT)))
obs_list.append(Actor("marshmallow", bottomleft=(2300,const.HEIGHT)))


# Player
player = Actor("broccoli", center=(600,460))
player.vx = 0
player.vy = 0

# Cutscenes 
cutscene = Actor("cutscene1", topleft=(0,0))

color_type = None
new_color_type = False
def draw_title():
    global color_type, new_color_type
    screen.fill("white")
    screen.draw.filled_rect(TITLESCREEN, "dark green")
    screen.draw.filled_rect(INTRODUCTION, "dark red")
    screen.draw.textbox("Heart and Broccoli", TITLESCREEN,color = color_type,shadow=(0.5,0.5))
    screen.draw.textbox(text.intro_text, INTRODUCTION, color = "gold",shadow=(0.5,0.5))
    if new_color_type:
      color_type = "red"
      new_color_type = False
    else:
      color_type = "green"
      new_color_type = True
    return
  
def on_mouse_down_state_title(pos):
    global state
    if INTRODUCTION.collidepoint(pos):
        state = "state_cutscene"


def draw_cutscene():
  cutscene.draw()
  screen.draw.filled_rect(PREVIOUS_BOX, "dark red")
  screen.draw.textbox("Previous", PREVIOUS_BOX,color="red",shadow=(0.5,0.5))
  screen.draw.filled_rect(NEXT_BOX, "dark green")
  screen.draw.textbox("Next", NEXT_BOX,color="green",shadow=(0.5,0.5))
  screen.draw.filled_rect(SKIP_BOX, "white")
  screen.draw.textbox("Skip", SKIP_BOX,color="grey",shadow=(0.5,0.5))


def on_mouse_down_state_cutscene(pos):
    global state, cutscene_number
    if PREVIOUS_BOX.collidepoint(pos):
        if cutscene_number == 1:
            state = "state_title"
        else:
            cutscene_number -= 1
    elif NEXT_BOX.collidepoint(pos):
        if cutscene_number == TOTAL_CUTSCENES:
            state = "state_instructions"
        else:
            cutscene_number += 1
    elif SKIP_BOX.collidepoint(pos):
        state = "state_instructions"


    cutscene.image = "cutscene" + str(cutscene_number)
    return


def draw_instructions():
    screen.fill("grey")
    screen.draw.filled_rect(INSTRUCTIONS, "dark red")
    screen.draw.textbox(instructions.instructions_text, INSTRUCTIONS, color = "orange",shadow=(0.5,0.5))
    screen.draw.filled_rect(PLAY_BOX, "dark green")
    screen.draw.textbox("Click to Play", PLAY_BOX,color="gold",shadow=(0.5,0.5))
    return


def on_mouse_down_state_instructions(pos):
    global state
    if PLAY_BOX.collidepoint(pos):
        state = "state_play"
    return



def draw_play():
    '''
      Draws the screen in the play state
    '''  
    screen.fill("yellow")
    
    for bg in bg_list:
        bg.draw()

    for obs in obs_list:
        obs.draw()

    player.draw()

    return



def update_play_player():
    if player.vy == 0:
        if keyboard.left:
            player.vx += -const.HORZ_ACC
        if keyboard.right:
            player.vx += const.HORZ_ACC
    return



def update_play():
    manage_actors.update_player_pos(player)
    vx = player.vx
    manage_actors.move(bg_list, -vx)
    manage_actors.move(obs_list, -vx)
    
    update_play_player()
    physics.gravity_update(player)
    physics.friction_update(player)
    manage_actors.shift_left_to_right(bg_list, obs_list)

    return





def draw():
    if state == "state_title":
        draw_title()
    elif state == "state_cutscene":
        draw_cutscene()
    elif state == "state_instructions":
        draw_instructions()
    elif state == "state_play":
        draw_play()
    elif state == "state_game_over":
        draw_game_over()
    elif state == "state_game_won":
        draw_state_game_won()
    else:
        print("something is wrong")
    return


def update():
    if state == "state_play":
        update_play()




def on_key_down_play(key):
    if key == keys.SPACE:
        if player.vy == 0:
            player.vy = -const.VERT_LAUNCH_SPEED

    return





def on_key_down(key):
    if state == "state_play":
        on_key_down_play(key)

    return

def on_mouse_down(pos):
  if state == "state_title":
    on_mouse_down_state_title(pos)
  elif state == "state_cutscene":
    on_mouse_down_state_cutscene(pos)
  elif state == "state_instructions":
    on_mouse_down_state_instructions(pos)
    
pgzrun.go()


