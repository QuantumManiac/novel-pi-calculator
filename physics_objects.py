class PhysicsObject:
    def __init__(self, mass, velocity):
        self.mass = mass
        self.velocity = velocity


def elastic_collision(object_l, object_r):
    """
    Calculates the resulting velocity of object_l, with mass m1 and velocity v1, after a perfectly elastic collision on
    a frictionless surface with object_r with v2 and m2. object_l is to the left of object_r
    Standard equations for perfectly elastic collisions are used

    :param object_l: object on the left
    :param object_r: object on the right
    :return: whether or not a collision occurred
    """
    v1 = object_l.velocity
    v2 = object_r.velocity
    m1 = object_l.mass
    m2 = object_r.mass

    if ((v1 < 0 < v2) or          # v1 and v2 going opposite directions away from each other
       (v2 >= v1 and v2 >= 0) or  # v2 going to the right at same speed or faster than v1
       (v1 <= v2 <= 0)):          # v1 going to the left at same speed or faster than v2
        object_l.velocity, object_r.velocity = v1, v2
        return False
    else:
        final_1 = (v1 * ((m1 - m2) / (m1 + m2))) + (v2 * ((2 * m2) / (m1 + m2)))
        final_2 = (v1 * ((2 * m1) / (m1 + m2))) - (v2 * ((m1 - m2) / (m1 + m2)))
        object_l.velocity, object_r.velocity = final_1, final_2
        return True

