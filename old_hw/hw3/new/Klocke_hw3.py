"""
Christopher Klocke
Homework 3
Submitted: October 19th, 2018

The input for this program should be a file containing one peptide sequence per line.

To run:     $python Klocke_hw3.py sequences.txt

    where "sequences.txt" contains peptide sequences of interest

This file contains two functions. The first ("entropy()") will calculate the entropy of a set of peptides. The second
("sum_of_pairs()") will calculate the sum of pairs for the peptides using a BLOSUM62 substitution matrix. This
substitution matrix was imported from BioPython.

For entropy and sum of pairs, if there was a gap / missing amino acid in a column, this column was disregarded per the
instructions for the assignment.

"""

## import statements
import sys      ## imports sys to take input file as command line argument
from math import log2 as log    ## imports log function to use log base 2 in entropy calculation
from Bio.SubsMat.MatrixInfo import blosum62 as blosum   ## imported BLOSUM62 substitution matrix from BioPython

## function definitions
def entropy(seqs):  ## this function will calculate the entropy of input sequences, and output this value
    entropy = 0     ## this variable is overall entropy
    if len(seqs[0]) == len(seqs[1]) == len(seqs[2]):    ## ensures sequences are same length (at least w/ placeholders)
        counter = 0
        while counter < len(seqs[0]):   ## iterate through columns of aligned sequences
            if seqs[0][counter] == seqs[1][counter] == seqs[2][counter]:  ## if all values in column are equal, column entropy is zero
                pass    ## add nothing to entropy in this case
            elif seqs[0][counter] == '-' or seqs[1][counter] == '-' or seqs[2][counter] == '-':
                pass    ## remove columns with blanks based on assignment prompt
            else:   ## there is a non-zero entropy to be calculated -- calculate and add to 'entropy'

                aminos = [seqs[0][counter],seqs[1][counter],seqs[2][counter]]  ## list of 3 AAs in column

                first = []
                second = []
                third = []

                for aa in aminos:    ## group common amino acids in lists
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

                p1 = len(first) / (len(aminos))     ## calculate fractions of total (e.g. 1/3, 2/3)
                p2 = len(second) / (len(aminos))
                p3 = len(third) / (len(aminos))

                if p3 != 0:     ## calculate column entropy score using entropy formula
                    entropy_column = ((p1 * log(p1)) + (p2 * log(p2)) + (p3 * log(p3))) * (-1)
                else:
                    entropy_column = ((p1 * log(p1)) + (p2 * log(p2))) * (-1)
                entropy += entropy_column   ## add column entropy score to total entropy score

            counter += 1

    else:
        print("sequences are not the same length")

    return entropy

def sum_of_pairs(seqs): ## this function will calculate the entropy of input sequences, and output this value

    total_score = 0     ## this variable is total of sum of pairs scores

    if len(seqs[0]) == len(seqs[1]) == len(seqs[2]):    ## ensures sequences are same length (at least w/ placeholders)
        counter = 0
        while counter < len(seqs[0]):   ## iterate through columns of aligned sequences
            if seqs[0][counter] == '-' or seqs[1][counter] == '-' or seqs[2][counter] == '-':
                pass       ## remove columns with blanks based on assignment prompt
            else:

                aminos = [seqs[0][counter],seqs[1][counter],seqs[2][counter]]   ## list of 3 AAs in column

    ## so I have a dictionary of the pairs and their respective scores

                try:
                    score1 = blosum[(aminos[0], aminos[1])] ## try to find score for 2 AAs in BLOSUM62 dict
                except KeyError:
                    score1 = blosum[(aminos[1], aminos[0])] ## could be in the other order

                try:
                    score2 = blosum[(aminos[0], aminos[2])] ## repeat for each of three combinations of 2 AAs
                except KeyError:
                    score2 = blosum[(aminos[2], aminos[0])]

                try:
                    score3 = blosum[(aminos[1], aminos[2])]
                except KeyError:
                    score3 = blosum[(aminos[2], aminos[1])]

                total_score += (score1 + score2 + score3)   ## add column score to total score

            counter += 1

    else:
        print("sequences are not the same length")

    return total_score  ## return total sum of pairs score for sequences

## main function definition
def main():
    with open(sys.argv[1], 'r') as sequences:   ## read first command line argument -- with loop as a context manager
        strings = []
        for line in sequences:  ## iterate through lines of input file, add each line as a peptide sequence to "strings"
            line = line.rstrip()
            if line != "":
                strings.append(line)

        print(round(entropy(strings),3))    ## run function to calculate entropy between sequences, print result

        print(sum_of_pairs(strings))    ## run function to calculate sum of pairs between sequences, print result

## run main function
if __name__ == "__main__":
    main()

