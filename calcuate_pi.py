from physics_objects import *
import time


def calculate_pi(n, give_time=False, logging=False):
    """
    Calculates the value of pi to n digits by simulating a system of two boxes and a wall colliding
    :param n: digits of pi to calculate
    :param give_time: if True, prints the time taken in terminal following function call
    :param logging: if True, returns a list of tuples in format (collision#, obj1 vel, obj2, vel), appended after
           every collision
    :return: default:
    """
    init_time = time.perf_counter()
    log = []

    if n <= 0:
        return -1
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




