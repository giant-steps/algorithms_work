"""

words


"""

import numpy as np



sequence = ['A','C','T','G','C','T','C','G','G','C','T','$']

n = len(sequence)
counter = 0

rotation = [tuple(sequence)]

while counter < n:
    base1 = sequence[0]
    sequence.pop(0)
    sequence.append(base1)

    #print(sequence)


    rotation.append(tuple(sequence))
    #rotation.append(tuple(b))

    #print(rotation)

    counter += 1

#print(rotation)

rotation_array = np.array(rotation)

print(rotation_array)

