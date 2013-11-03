# import math
import sys

sys.setrecursionlimit(10000)

two_squared = 4 # For semantic purposes

max_iterations = 80

def is_in_mandelbrot_set(c):
    def iterate(zn, c, i):

        z = zn ** 2 + c
        # magnitude = math.sqrt(z.real**2 + z.imag**2)
        magnitude_squared = z.real**2 + z.imag**2

        if magnitude_squared > two_squared:
            return (False, i)
        if i >= max_iterations:
            return (True, None)
        else:
            return iterate(z, c, i + 1)

    return iterate(0, c, 1)
