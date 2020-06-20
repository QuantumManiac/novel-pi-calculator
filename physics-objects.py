class PhysicsObject:
    def __init__(self):
        self.velocity = 0
        self.mass = 0

    def elastic_collision(self, other_object):
        """
        modifies the velocities of two objects of velocities v1 v2 and masses m1 m2 following a perfectly elastic collision. Friction does not exist.
        Equation: v1F = ((m1 - m2 ) / (m1 + m2)) v1I + ((2 m2 ) / (m1 + m2)) v2I
        
        :param other_object: 
        :return: 
        """
        v1 = self.velocity
        v2 = other_object.velocity
        m1 = self.mass
        m2 = other_object.velocity

        


    def calculate_collision_result(self, other_object):

