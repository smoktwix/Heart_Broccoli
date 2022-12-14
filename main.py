import pgzrun
import text
import manage_actors
import physics
import const



# Hello World
# 5:29 pm december 11
# screen size
WIDTH = const.WIDTH
HEIGHT = const.HEIGHT

#WIDTH = 1200
#HEIGHT = 600



# Global Variables
state = "state_title"
cutscene_number = 1
end_cutscene_number = 18

# Global Booleans
  # None for now

# Global Constants
TOTAL_CUTSCENES = 17
START_END_CUTSCENE = 18
END_END_CUTSCENE = 34



# Global Rectangles
TITLESCREEN = Rect((200, 50, 800, 180))
INTRODUCTION = Rect((75, 250, 1050, 325))
PREVIOUS_BOX = Rect((840,520,140,40))
NEXT_BOX = Rect((1000,520,80,40))
SKIP_BOX = Rect((1100,520,80,40))
PREVIOUS_BOX2 = Rect((25,520,140,40))
NEXT_BOX2 = Rect((185,520,80,40))
SKIP_BOX2 = Rect((285,520,80,40))
INSTRUCTIONS = Rect(200,100,800,400)
PLAY_BOX = Rect((1025, 520, 150, 40))




# Backgrounds
bg_0 = Actor("mm_background_1", topleft=(0,0))
bg_1 = Actor("mm_background_2", topleft=(const.WIDTH,0))
bg_list = [bg_0, bg_1]

# Marsmallow Obstacles
# I am making a change here
obs_list = []
obs_list.append(Actor("white_marshmallow", bottomleft=(100,const.HEIGHT)))
obs_list.append(Actor("white_marshmallow", bottomleft=(350,350)))
obs_list.append(Actor("white_marshmallow", bottomleft=(650,450)))
obs_list.append(Actor("white_marshmallow", bottomleft=(900,250)))
obs_list.append(Actor("white_marshmallow", bottomleft=(1200,const.HEIGHT)))
obs_list.append(Actor("white_marshmallow", bottomleft=(1600,500)))
obs_list.append(Actor("white_marshmallow", bottomleft=(1850,336)))
obs_list.append(Actor("white_marshmallow", bottomleft=(2173,176)))
obs_list.append(Actor("wide_white_marshmallow", bottomleft=(2100,467)))
obs_list.append(Actor("pink_marshmallow", bottomleft=(2400,const.HEIGHT)))
obs_list.append(Actor("white_marshmallow", bottomleft=(2750,400)))
obs_list.append(Actor("white_marshmallow", bottomleft=(3075,545)))
obs_list.append(Actor("wide_white_marshmallow", bottomleft=(3500,389)))
obs_list.append(Actor("wide_pink_marshmallow", bottomleft=(3850,225)))
obs_list.append(Actor("pink_marshmallow", bottomleft=(4282,const.HEIGHT)))
obs_list.append(Actor("wide_white_marshmallow", bottomleft=(4700,const.HEIGHT)))
obs_list.append(Actor("pink_marshmallow", bottomleft=(5300,const.HEIGHT)))
obs_list.append(Actor("pink_marshmallow", bottomleft=(5700,450)))
obs_list.append(Actor("wide_pink_marshmallow", bottomleft=(6000,250)))
obs_list.append(Actor("wide_white_marshmallow", bottomleft=(6500,250)))
obs_list.append(Actor("wide_white_marshmallow", bottomleft=(6685,250)))
obs_list.append(Actor("wide_white_marshmallow", bottomleft=(6870,250)))
obs_list.append(Actor("wide_white_marshmallow", bottomleft=(6310,650)))
obs_list.append(Actor("wide_pink_marshmallow", bottomleft=(6500,const.HEIGHT)))
obs_list.append(Actor("wide_pink_marshmallow", bottomleft=(6685,const.HEIGHT)))
obs_list.append(Actor("wide_pink_marshmallow", bottomleft=(6875,const.HEIGHT)))
obs_list.append(Actor("pink_marshmallow", bottomleft=(7065,const.HEIGHT)))
obs_list.append(Actor("wide_white_marshmallow", bottomleft=(7500,450)))
obs_list.append(Actor("white_marshmallow", bottomleft=(8000,200)))
obs_list.append(Actor("white_marshmallow", bottomleft=(8000,const.HEIGHT)))
obs_list.append(Actor("white_marshmallow", bottomleft=(8500,325)))
obs_list.append(Actor("pink_marshmallow", bottomleft=(8350,const.HEIGHT)))
obs_list.append(Actor("wide_pink_marshmallow", bottomleft=(8750,450)))
obs_list.append(Actor("wide_white_marshmallow", bottomleft=(9500,const.HEIGHT)))
obs_list.append(Actor("white_marshmallow", bottomleft=(9110,260)))
obs_list.append(Actor("white_marshmallow", bottomleft=(10250,300)))
obs_list.append(Actor("wide_white_marshmallow", bottomleft=(10550,400)))
obs_list.append(Actor("white_marshmallow", bottomleft=(11000,300)))
obs_list.append(Actor("white_marshmallow", bottomleft=(11500,300)))
obs_list.append(Actor("wide_white_marshmallow", bottomleft=(12000,300)))
obs_list.append(Actor("white_marshmallow", bottomleft=(13000,450)))
obs_list.append(Actor("pink_marshmallow", bottomleft=(13625,250)))
obs_list.append(Actor("wide_pink_marshmallow", bottomleft=(14200,450)))
obs_list.append(Actor("pink_marshmallow", bottomleft=(14557,300)))
obs_list.append(Actor("wide_white_marshmallow", bottomleft=(14457,const.HEIGHT)))
obs_list.append(Actor("wide_white_marshmallow", bottomleft=(14642,const.HEIGHT)))
obs_list.append(Actor("wide_pink_marshmallow", bottomleft=(15758,const.HEIGHT)))
obs_list.append(Actor("pink_marshmallow", bottomleft=(15227,const.HEIGHT)))
obs_list.append(Actor("wide_white_marshmallow", bottomleft=(16050,325)))
obs_list.append(Actor("white_marshmallow", bottomleft=(16643,200)))
obs_list.append(Actor("wide_white_marshmallow", bottomleft=(17850,const.HEIGHT)))
obs_list.append(Actor("pink_marshmallow", bottomleft=(17175,460)))
obs_list.append(Actor("wide_pink_marshmallow", bottomleft=(18345,300)))
obs_list.append(Actor("white_marshmallow", bottomleft=(19150,const.HEIGHT)))
obs_list.append(Actor("wide_pink_marshmallow", bottomleft=(19800,const.HEIGHT)))
obs_list.append(Actor("pink_marshmallow", bottomleft=(20300,350)))
obs_list.append(Actor("wide_pink_marshmallow", bottomleft=(20700,350)))
obs_list.append(Actor("pink_marshmallow", bottomleft=(21250,300)))
obs_list.append(Actor("pink_marshmallow", bottomleft=(21700,350)))
obs_list.append(Actor("wide_pink_marshmallow", bottomleft=(22100,450)))
obs_list.append(Actor("white_marshmallow", bottomleft=(22700,const.HEIGHT)))
obs_list.append(Actor("wide_white_marshmallow", bottomleft=(23250,const.HEIGHT)))
obs_list.append(Actor("wide_white_marshmallow", bottomleft=(23435,const.HEIGHT)))
obs_list.append(Actor("pink_marshmallow", bottomleft=(23625,const.HEIGHT)))
obs_list.append(Actor("wide_pink_marshmallow", bottomleft=(23400,325)))
obs_list.append(Actor("wide_white_marshmallow", bottomleft=(23750,200)))
obs_list.append(Actor("wide_white_marshmallow", bottomleft=(23935,200)))
obs_list.append(Actor("wide_white_marshmallow", bottomleft=(24120,200)))
obs_list.append(Actor("wide_white_marshmallow", bottomleft=(24305,200)))
obs_list.append(Actor("wide_white_marshmallow", bottomleft=(24490,200)))
obs_list.append(Actor("wide_white_marshmallow", bottomleft=(24675,200)))
obs_list.append(Actor("golden_marshmallow", bottomleft=(25500,const.HEIGHT)))


#obs_list = obs_list[:3]
#obs_list.append(Actor("golden_marshmallow", bottomleft=(900,const.HEIGHT)))


# Player
player = Actor("broccoli", center=(150,400))
# actual x position of player
player.actual_left = player.left
# vx - speed in the x-direction
player.vx = 0
# vy - speed in the y-direction
player.vy = 0
# ontop - are you on top of a marshmallow
player.ontop = False

player_walk_counter = 0
player_walk_counter2 = 0
player_fall_counter = 0
player_jump_counter = 0

# Cutscenes 
cutscene = Actor("cutscene1", topleft=(0,0))
doomed_world = Actor("cutscene30", topleft=(0,0))
saved_world = Actor("end_image", topleft=(0,0))

end_cutscene = Actor("cutscene18", topleft=(0,0))

# Music there won't be any music the original was scrapped for not fitting in the game and being bad

color_type = "green"
title_counter = 1

def draw_title():
    global color_type
    global title_counter
    cutscene.draw()
    title_counter += 1
    screen.draw.filled_rect(TITLESCREEN, "dark green")
    screen.draw.filled_rect(INTRODUCTION, "dark red")
    screen.draw.textbox("Broccoli The Great Telling", TITLESCREEN,color = color_type,shadow=(0.5,0.5))
    screen.draw.textbox(text.intro_text_prophecy, INTRODUCTION, color = "gold",shadow=(0.5,0.5))
    if (color_type == "green") and (title_counter % 20 == 0):
      color_type = "red"
    elif (color_type == "red") and (title_counter % 20 == 0):
      color_type = "green"
    else:
        pass


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


def draw_end_cutscene():
  end_cutscene.draw()
  if end_cutscene_number != START_END_CUTSCENE:
      screen.draw.filled_rect(PREVIOUS_BOX2, "dark red")
      screen.draw.textbox("Previous", PREVIOUS_BOX2,color="red",shadow=(0.5,0.5))
  screen.draw.filled_rect(NEXT_BOX2, "dark green")
  screen.draw.textbox("Next", NEXT_BOX2,color="green",shadow=(0.5,0.5))
  screen.draw.filled_rect(SKIP_BOX2, "white")
  screen.draw.textbox("Skip", SKIP_BOX2,color="grey",shadow=(0.5,0.5))



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
  

def on_mouse_down_state_end_cutscene(pos):
    global state, end_cutscene_number
    if PREVIOUS_BOX2.collidepoint(pos) and (end_cutscene_number > START_END_CUTSCENE):
        end_cutscene_number -= 1
    if NEXT_BOX2.collidepoint(pos):
        if end_cutscene_number == END_END_CUTSCENE:
            state = "state_game_won"
        else:
            end_cutscene_number += 1
    elif SKIP_BOX2.collidepoint(pos):
        state = "state_game_won"


    end_cutscene.image = "cutscene" + str(end_cutscene_number)
    return



def draw_instructions():
    for bg in bg_list:
      bg.draw()
    screen.draw.filled_rect(INSTRUCTIONS, "dark red")
    screen.draw.textbox(text.instructions_text_prophecy, INSTRUCTIONS, color = "orange",shadow=(0.5,0.5))
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
    for bg in bg_list:
        bg.draw()

    for obs in obs_list:
        obs.draw()

    player.draw()

    return



def update_play_player():
    global player_walk_counter, player_walk_counter2, player_fall_counter, state, player_jump_counter
    #if player.vy == 0:
    #this was changed because it was annoying not to be able to move in air and causes gameplay issues
    if keyboard.left:
         player.vx += -const.HORZ_ACC
    if keyboard.right:
        player.vx += const.HORZ_ACC

    if player.vy > 0:
      player_fall_counter += 1
      fall_image_counter = (player_fall_counter % 5) + 1
      player.image = "broccoli_fall" + str(fall_image_counter)
    elif player.vy < 0:
      player_jump_counter += 1
      jump_image_counter = (player_jump_counter % 2) + 1
      player.image = "broccoli_jump" + str(jump_image_counter)
    elif player.vx > 0:
      player_walk_counter += 1
      image_counter = (player_walk_counter % 4) + 1
      player.image = "broccoli_walk_right" + str(image_counter)
    elif player.vx < 0:
      player_walk_counter2 += 1
      image_counter2 = (player_walk_counter2 % 4) + 1
      player.image = "broccoli_walk_left" + str(image_counter2)
    else:
      player.image = "broccoli"
    if player.bottom >= 600:
      state = "state_game_over"
      
    
    return


def check_collision_pink_and_gold(player, obs_list):
  global state
  for obs in obs_list:
    if obs.image == "pink_marshmallow":
      if player.ontop and player.colliderect(obs):
          player.vy -= const.VERT_LAUNCH_SPEED
          player.ontop = False
    elif obs.image == "wide_pink_marshmallow":
      if player.ontop and player.colliderect(obs):
          player.vy -= const.VERT_LAUNCH_SPEED
          player.ontop = False
    elif obs.image == "golden_marshmallow":
      if player.ontop and player.colliderect(obs):
          state = "state_end_cutscenes"
      
  return


def draw_state_game_won():
  saved_world.draw()

  screen.draw.text("The great telling is complete", topleft = (25,200), fontsize = 60, color = "red", shadow = (0.5, 0.5))
  screen.draw.text("The light of the health sphere's chosen messiah", topleft = (25,250), fontsize = 60, color = "red", shadow = (0.5, 0.5))
  screen.draw.text("shines bright on the world despite the darkness that is coming", topleft = (25,300), fontsize = 55, color = "red", shadow = (0.5, 0.5))
  screen.draw.text("Will you shut up people are trying to sleep!", topleft = (25, 350), fontsize = 60, color = "gold", shadow = (0.5, 0.5))
  



def draw_game_over():
    doomed_world.draw()
    screen.draw.text("Broccoli's Vison has ended",topleft = (250,100), fontsize = 60, color = "red",shadow=(0.5,0.5))
    screen.draw.text("He will never be able to fulfill",topleft = (250,150), fontsize = 60, color = "red",shadow=(0.5,0.5))
    screen.draw.text("the prophecy and the world is doomed!", topleft = (250,200), fontsize = 60, color = "red", shadow = (0.5, 0.5))
    screen.draw.text("JUNK DAY IS COMING!",topleft = (250,250), fontsize = 60, color = "red",shadow=(0.5,0.5))
    return





          
def update_play():
    manage_actors.update_player_pos(player)
    vx = player.vx
    player.actual_left = player.actual_left + vx
    manage_actors.move(bg_list, -vx)
    manage_actors.move(obs_list, -vx)

    check_collision_pink_and_gold(player, obs_list)
  
    physics.check_collision(obs_list, player)
    update_play_player()
    physics.gravity_update(player)
    physics.friction_update(player)
    manage_actors.shift_left_to_right(bg_list)#, obs_list)


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
    elif state == "state_end_cutscenes":
        draw_end_cutscene()
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
        #if player.vy == 0 and player.ontop:
        # changed for testing purposes
        if player.vy == 0: # player is on the ground or on white marshmallow
            player.vy = -const.VERT_LAUNCH_SPEED
            player.ontop = False
        #else:
            #player.vy = player.vy - 2

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
  elif state == "state_end_cutscenes":
    on_mouse_down_state_end_cutscene(pos)

    
pgzrun.go()


