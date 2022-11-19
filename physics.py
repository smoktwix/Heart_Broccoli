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
    for obs in obs_list:
        if player.colliderect(obs):
            if player.bottom - 5 < obs.top: # hitting the top of the obs
                player.vy = 0
                player.ontop = True
                return
            
            else: # hitting the side of the obs
                player.vx = 0
                player.ontop = False
                return

    player.ontop = False
    return
            
