from matplotlib import pyplot as plt
from physics_objects import *
import time


def calculate_pi(n, give_time=False, logging=False):
    """
    Calculates the value of pi to n digits by simulating a system of two boxes and a wall colliding, and counting the
    number of collisions between object 1 and object 2 or the wall before it can no longer collide with another body:

    | Wall
    |
    |           |--------|      init_speed |--------|
    |           |Object 1|     <=========  |Object 2|
    |           |________|                 |________|
    -------------------------------------------------

    :param n: digits of pi to calculate
    :param give_time: if True, prints the time taken in terminal following function call
    :param logging: if True, returns a list of tuples in format (collision#, obj1 vel, obj2, vel), appended after
           every collision
    :return: default: the calculated value of pi
             with logging=True: a tuple with the form (calculated_pi, log)
    """
    init_time = time.perf_counter()
    log = []

    required_weight = 10 ** (1 + ((n - 1) * 2))
    init_speed = 50
    obj1 = PhysicsObject(10, 0)
    obj2 = PhysicsObject(required_weight, -init_speed)

    collisions = 0
    if logging:
        log.append((collisions, obj1.velocity, obj2.velocity))

    while True:
        if elastic_collision(obj1, obj2):
            collisions += 1
            if logging:
                log.append((collisions, obj1.velocity, obj2.velocity))
            vel = obj1.velocity
            if vel < 0:
                obj1.velocity = -vel
                collisions += 1
                if logging:
                    log.append((collisions, obj1.velocity, obj2.velocity))
                # print(f"obj1 bounces off wall. Collisions count: {collisions}")
        else:
            # print("End reached, objects will never collide again")
            if give_time:
                final_time = time.perf_counter()
                print(f"Time taken: {final_time - init_time:0.4f}s")

            calculated_pi = float(collisions / (10 ** (n - 1)))

            if logging:
                return calculated_pi, log
            else:

                return calculated_pi


def plot_results(log, show_polygon=True):
    """
    Plots the points from the given log file, with the velocity of object 1 as the y-axis and the velocity of object 2
    as the x-axis.
    :param log: logfile produced from calculate_pi to use
    :param show_polygon: whether or not to plot the circle that the points make
    :return: none
    """
    collisions, obj1, obj2, = zip(*log)

    def modify_list(li):
        li1 = li[0::2]
        li2 = list(li[1::2])
        li2 = li2[::-1]
        li2.append(li[0])
        return list(li1) + li2

    poly_y = modify_list(obj1)
    poly_x = modify_list(obj2)

    plt.figure(figsize=(5, 5))
    plt.plot(obj2, obj1)
    if show_polygon:
        plt.plot(poly_x, poly_y, label='Polygon', linewidth=2)
    plt.xlabel("Velocity of Object 2")
    plt.ylabel("Velocity of Object 1")

    plt.show()



