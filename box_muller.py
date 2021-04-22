import random
import math
import cv2
import numpy as np
import time

def generate_gaussian_two():
    # create two randomly generated variables U and V
    U = random.uniform(0, 1)
    V = random.uniform(0, 1)

    N = math.sqrt(-2 * math.log(U)) * math.cos(2 * math.pi * V)
    M = math.sqrt(-2 * math.log(U)) * math.sin(2 * math.pi * V)

    return N, M

if __name__ == "__main__": 
    # Create a canvas
    width = 500
    height = 500
    canvas = np.zeros((width, height), np.uint8)

    # Find a scale.
    # So for a 100x100 canvas
    # The scale is 50 in each direction
    scale = 100
    n = 1000000

    # Generate n values for N and M
    for i in range(n):
        N,M = generate_gaussian_two()

        # Scale them by 50
        N = int(N * scale) + width//2
        M = int(M * scale) + height//2

        if N > 0 and M > 0 and N < width and M < height:
            # Plot them on the canvas with a sleep
            canvas[N, M] = 255

            cv2.imshow("Canvas", canvas)
            key = cv2.waitKey(1)

            if key == ord('q'):
                break

    cv2.waitKey(0)
