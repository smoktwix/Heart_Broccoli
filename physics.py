import const


def gravity_update(actor):

    if actor.bottom < 500:
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
