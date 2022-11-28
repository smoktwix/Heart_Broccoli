import const


def gravity_update(actor):

    if actor.bottom < const.HEIGHT:
        if not actor.ontop:
            actor.vy += const.GRAVITY_ACC
     
    else:
      actor.vy = 0
    return




def friction_update(actor):
    if actor.vx > 0:
        actor.vx -= const.FRICTION_ACC
        actor.vx = max(0, actor.vx)
    if actor.vx < 0:
        actor.vx += const.FRICTION_ACC
        actor.vx = min(0, actor.vx)
    
    if actor.vx > const.MAX_X_SPEED:
        actor.vx = const.MAX_X_SPEED
    if actor.vx < -const.MAX_X_SPEED:
        actor.vx = -const.MAX_X_SPEED

    return




def check_collision(obs_list, player):
    '''
    - Updates player.vy and player.vx on whether it had a collision
    - returns True if there was a collision
    - returns False otherwise

    '''
    for obs in obs_list:
        if player.colliderect(obs):
            if (player.bottom - 14 < obs.top) and (player.vy >= 0): # hitting the top of the obs
                player.vy = 0
                player.ontop = True
                return True
            elif (player.top > obs.bottom - 14)  and (player.vy <= 0): # hitting from the bottom
                player.vy = - const.FRAC_SPEED * player.vy
                player.ontop = False
                return True
            else: # hitting the side of the obs
                player.vx = -const.FRAC_SPEED * player.vx
                player.ontop = False
                return True

    player.ontop = False
    return False
            
