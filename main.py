from calcuate_pi import *
from matplotlib import pyplot as plt

n = int(input('Enter the number of digits of pi to calculate (recommend < 8): '))

result, log = calculate_pi(n, True, True)

print(f"Result: {result}")


collisions, obj1, obj2, = zip(*log)

plt.plot(collisions, obj1, label="Object 1")
plt.plot(collisions, obj2, label="Object 2")

plt.xlabel("# of collisions")
plt.ylabel("velocity")
plt.legend()

plt.show()


