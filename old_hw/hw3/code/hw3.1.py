"""

This program is for algorithms HW #3.

"""

## import statements
import sys
from math import log10 as log

## function definitions
def entropy(seqs):
    entropy = 0
    if len(seqs[0]) == len(seqs[1]) == len(seqs[2]):    ## ensures sequences are same length
        counter = 0
        while counter < len(seqs[0]):   ## iterate through columns of aligned sequences
            if seqs[0][counter] == seqs[1][counter] == seqs[2][counter]:  ## if all values in column are equal, column entropy is zero
                pass
            elif seqs[0][counter] == '-' or seqs[1][counter] == '-' or seqs[2][counter] == '-': ##If a column has a gap, for this assignment ignore the column.
                #print(seqs[0][counter] + seqs[1][counter] + seqs[2][counter])
                pass
            else:   ## there is a non-zero entropy to be calculated -- calculate and add to 'entropy'

                aminos = [seqs[0][counter],seqs[1][counter],seqs[2][counter]]

                first = []
                second = []
                third = []

                for aa in aminos:
                    if first == []:
                        first.append(aa)
                    elif first[0] == aa:
                        first.append(aa)
                    elif second == []:
                        second.append(aa)
                    elif second[0] == aa:
                        second.append(aa)
                    else:
                        third.append(aa)

                p1 = len(first) / (len(aminos))
                p2 = len(second) / (len(aminos))
                p3 = len(third) / (len(aminos))
                #print(p3)

                if p3 != 0:
                    entropy_column = ((p1 * log(p1)) + (p2 * log(p2)) + (p3 * log(p3))) * (-1)
                else:
                    entropy_column = ((p1 * log(p1)) + (p2 * log(p2))) * (-1)
                entropy += entropy_column

            counter += 1

    return entropy


"""
This function needs to calculate sum of pairs for the multiple sequence alignment, utilizing 
a BLOSUM62 substitution matrix. 

I need a dictionary with the BLOSUM62 substitution matrix in it

key is, e.g. 'NT' while value is score, e.g. 0
"""
def sum_of_pairs(seqs):
    pass

## main function definition
def main():
    with open(sys.argv[1], 'r') as sequences:
        strings = []
        for line in sequences:
            line = line.rstrip()
            if line != "":
                strings.append(line)

        print(entropy(strings))

        sum_of_pairs(strings)       ########

## run main function
if __name__ == "__main__":
    main()

