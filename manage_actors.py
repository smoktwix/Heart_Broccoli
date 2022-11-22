import const


def update_player_pos(actor):
  '''
    we don't move the player in x-direction
    background moves instead
  '''

  actor.y += actor.vy
  return


def move(actor_list, v):
    '''
        moves all the actors in actor_list by velocity v
        left if v is negative and right if v is positive

        actor_list - list of actors
        v - velocity

    '''
    for a in actor_list:
        a.x = a.x + v

    return



def shift_left_to_right(bg_list, obs_list):
    if len(bg_list) != 0:
        if bg_list[0].right < 0:
            a = bg_list.pop(0)
            a.topleft = (const.WIDTH + a.right, 0)
            bg_list.append(a)
            for i in range(len(obs_list)):
                if obs_list[i].right < 0:
                    obs_list[i].x += 2*const.WIDTH

        if bg_list[-1].left > const.WIDTH:
            a = bg_list.pop(-1)
            a.topright = (a.left - const.WIDTH,0)
            bg_list.insert(0, a)
            for i in range(len(obs_list)):
                if obs_list[i].left > const.WIDTH:
                    obs_list[i].x -= 2*const.WIDTH
            

    return  


def shift_bg_left_to_right(bg_list):
    if len(bg_list) != 0:
        if bg_list[0].right < 0:
            a = bg_list.pop(0)
            a.topleft = (const.WIDTH + a.right, 0)
            bg_list.append(a)

        if bg_list[-1].left > const.WIDTH:
            a = bg_list.pop(-1)
            a.topright = (a.left - const.WIDTH,0)
            bg_list.insert(0, a)

    return



def shift_obs_left_to_right(obs_list):
    for i in range(len(obs_list)):
        if obs_list[i].right < 0:
            obs_list[i].x += 2*const.WIDTH 

    return            
