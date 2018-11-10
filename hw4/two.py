"""

words


"""

## import statements
import numpy as np


## function definitions
def transform(sequence):
    n = len(sequence)
    counter = 0
    rotation = []

    while counter < n:
        base1 = sequence[0]
        sequence.pop(0)
        sequence.append(base1)
        rotation.append(tuple(sequence))
        counter += 1

    rotation_array = np.array(rotation)
    print(rotation_array)
    return rotation_array

def lex(rotation):
    h = rotation

## main function definition
def main():

    string = ['A', 'C', 'T', 'G', 'C', 'T', 'C', 'G', 'G', 'C', 'T', '$']
    lex(transform(string))

## run main function
if __name__ == "__main__":
    main()