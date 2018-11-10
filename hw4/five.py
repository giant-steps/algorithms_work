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
    #print(rotation_array)
    return rotation

def lex(matrix):

    weights = {'$':0,'A':1,'C':2,'G':3,'T':4}

    count = 0
    ender = False

    while ender == False:
        ender = True
        while count < len(matrix[0]) - 1:

            #print(weights[matrix[count][0]])   #############

            if weights[matrix[count][0]] > weights[matrix[count+1][0]]:

                ender = False

                end = matrix[count]
                matrix.pop(count)
                matrix.append(end)

                #print(end)



            elif weights[matrix[count][0]] == weights[matrix[count+1][0]]:
                if weights[matrix[count][1]] > weights[matrix[count + 1][1]]:
                    ender = False

                    end = matrix[count]
                    matrix.pop(count)
                    matrix.append(end)

            count += 1

    count = 0

    print(np.array(matrix))


## main function definition
def main():

    string = ['A', 'C', 'T', 'G', 'C', 'T', 'C', 'G', 'G', 'C', 'T', '$']
    lex(transform(string))

## run main function
if __name__ == "__main__":
    main()

