import pgzrun
import text
import manage_actors
import physics
import const




# screen size
WIDTH = const.WIDTH
HEIGHT = const.HEIGHT

#WIDTH = 1200
#HEIGHT = 600



# Global Variables
state = "state_title"
cutscene_number = 1

# Global Booleans
  # None for now

# Global Constants
TOTAL_CUTSCENES = 17



# Global Rectangles
TITLESCREEN = Rect((200, 50, 800, 180))
INTRODUCTION = Rect((75, 250, 1050, 325))
PREVIOUS_BOX = Rect((840,520,140,40))
NEXT_BOX = Rect((1000,520,80,40))
SKIP_BOX = Rect((1100,520,80,40))
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
obs_list.append(Actor("wide_white_marshmallow", bottomleft=(6875,250)))
obs_list.append(Actor("wide_pink_marshmallow", bottomleft=(6500,const.HEIGHT)))
obs_list.append(Actor("wide_pink_marshmallow", bottomleft=(6685,const.HEIGHT)))
obs_list.append(Actor("wide_pink_marshmallow", bottomleft=(6875,const.HEIGHT)))
obs_list.append(Actor("pink_marshmallow", bottomleft=(7065,const.HEIGHT)))
obs_list.append(Actor("wide_white_marshmallow", bottomleft=(7500,450)))
obs_list.append(Actor("white_marshmallow", bottomleft=(8000,200)))
obs_list.append(Actor("white_marshmallow", bottomleft=(8000,const.HEIGHT)))
obs_list.append(Actor("white_marshmallow", bottomleft=(8500,300)))
obs_list.append(Actor("pink_marshmallow", bottomleft=(8350,const.HEIGHT)))
obs_list.append(Actor("wide_pink_marshmallow", bottomleft=(8750,450)))
obs_list.append(Actor("wide_white_marshmallow", bottomleft=(9500,const.HEIGHT)))
obs_list.append(Actor("white_marshmallow", bottomleft=(8950,260)))
obs_list.append(Actor("golden_marshmallow", bottomleft=(10000,const.HEIGHT)))





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

# Cutscenes 
cutscene = Actor("cutscene1", topleft=(0,0))

# Music
music.play("into_the_great_dream")

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
      color_type = "white"
    elif (color_type == "white") and (title_counter % 20 == 0):
      color_type = "green"
    else:
        pass


    return
  
def on_mouse_down_state_title(pos):
    global state
    if INTRODUCTION.collidepoint(pos):
        music.stop()
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
            music.play("into_the_great_mystery")
        else:
            cutscene_number += 1
    elif SKIP_BOX.collidepoint(pos):
        state = "state_instructions"
        music.play("into_the_great_mystery")


    cutscene.image = "cutscene" + str(cutscene_number)
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
        music.stop()
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
    global player_walk_counter, player_walk_counter2, player_fall_counter, state
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
          state = "state_game_won"
      
  return


def draw_state_game_won():
  screen.fill("dark green")
  screen.draw.text("You Won The Game!", topleft = (25,150), fontsize = 60, color = "gold", shadow = (0.5, 0.5))
  screen.draw.text("The great telling is complete", topleft = (25,200), fontsize = 60, color = "red", shadow = (0.5, 0.5))
  screen.draw.text("The light of the health sphere's chosen messiah", topleft = (25,250), fontsize = 60, color = "red", shadow = (0.5, 0.5))
  screen.draw.text("shines bright on the world despite the darkness that is coming", topleft = (25,300), fontsize = 55, color = "forest green", shadow = (0.5, 0.5))
  screen.draw.text("Thank You For Playing", topleft = (375, 350), fontsize = 60, color = "gold", shadow = (0.5, 0.5))
  return




def draw_game_over():
    screen.draw.text("Broccolis Vison has ended",topleft = (250,150), fontsize = 60, color = "red",shadow=(0.5,0.5))
    screen.draw.text("he will never be able to fulfill",topleft = (250,200), fontsize = 60, color = "red",shadow=(0.5,0.5))
    screen.draw.text("the prophecy and the world is doomed", topleft = (250,250), fontsize = 60, color = "red", shadow = (0.5, 0.5))
    screen.draw.text("JUNK DAY IS COMING GAME OVER!",topleft = (250,300), fontsize = 60, color = "dark red",shadow=(0.5,0.5))
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
    
pgzrun.go()


