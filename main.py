from calcuate_pi import *


n = 0
while n <= 0:
    n = int(input('Enter the number of digits of pi to calculate (recommend < 8): '))

result, log = calculate_pi(n, True, True)

print(f"Result: {result}")

plot_results(log, False)








