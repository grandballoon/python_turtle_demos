import turtle
import random
import math

"""A simulation of an animal finding food by tracking its scent"""

tom = turtle.Turtle()
distance_last_time = None
distance_now = None
food_pos_x = random.randrange(-turtle.window_width() // 2, turtle.window_width() // 2)
food_pos_y = random.randrange(-turtle.window_height() // 2, turtle.window_height() // 2)
food_pos = (food_pos_x, food_pos_y)
STRONGER = "stronger"
WEAKER = "weaker"
food = turtle.Turtle()
food.shape("circle")
food.penup()
food.setpos(food_pos)

def distance_to_food():
    answer = math.sqrt((int(tom.xcor()) - food_pos_x)**2 + (int(tom.ycor()) - food_pos_y)**2)
    return answer

distance_last_time = distance_to_food()
distance_now = distance_to_food()

def random_move(a1, a2, d1, d2):
    while True:
        tom.lt(random.randrange(a1, a2))
        tom.fd(random.randrange(d1, d2))

def check_forward_and_move(dist):
    old_position = tom.pos()
    tom.penup()
    tom.ht()
    tom.fd(dist)
    foreward_failed = out_of_bounds()
    tom.setpos(old_position)
    tom.pd()
    tom.st()
    if foreward_failed:
        tom.rt(180)
    tom.fd(dist)

def out_of_bounds():
    if abs(tom.xcor()) > turtle.window_width() // 2:
        return True
    elif abs(tom.ycor()) > turtle.window_height() // 2:
        return True
    return False

def bounded_random_move(a1, a2, d1, d2):
    while True:
        tom.lt(random.randrange(a1, a2))
        check_forward_and_move(random.randrange(d1, d2))

def scent():
    global distance_last_time
    if distance_to_food() < distance_last_time:
        result = STRONGER
    else:
        result = WEAKER
    distance_last_time = distance_to_food()
    return result


def find_by_scent(d1, d2, scent_turn, rand_turn):
    while distance_to_food() > 0:

        tom.fd(random.randrange(d1, d2)) # move forward random amount

        tom.left(random.randrange(-rand_turn, rand_turn)) # turn left random amount

        if scent() == WEAKER: # turn right some amount
            tom.right(scent_turn)

tom.speed(3)
find_by_scent(5, 15, 35, 15)

turtle.done()
