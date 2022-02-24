import numpy as np
from collections import deque
from scipy.spatial.transform import Rotation as R
A = [
    [-1,-1,1],
    [-2,-2,2],
    [-3,-3,3],
    [-2,-3,1],
    [5,6,-4],
    [8,0,7]
]
cnt = 0
for _ in range(3):
    i = 1
    for _ in range(2):
        i *= -1
        for j in range(len(A)):
            A[j] = [k*i for k in A[j]]
        for _ in range(4):
            rotation_degrees = 90
            rotation_radians = np.radians(rotation_degrees)
            rotation_axis = np.array([0, 0, 1])
            rotation_vector = rotation_radians * rotation_axis
            rotation = R.from_rotvec(rotation_vector)
            for idx, j in enumerate(A):
                A[idx] = rotation.apply(A[idx])
                print(A[idx])
            cnt += 1
            print(A)
    for idx, j in enumerate(A):
        A[idx] = deque(A[idx])
        A[idx].rotate(1)
        A[idx] = list(A[idx])
print(cnt)