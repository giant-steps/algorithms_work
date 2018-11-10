"""

Christopher Klocke
Algorithms midterm
Submitted: November 9th, 2018

This program will answer questions 1, 6, and 7 on the midterm.
"""

"""
1. Provide the pseudo-code for an algorithm that will determine the length of the shortest substring that
occurs exactly once in a genomic sequence of length N. You must provide all assumptions made for your
algorithm.
"""
def one():  ## answers midterm question 1
    ## string to search
    string = 'AAATTTCCCGGGAAATTTCCCGGGAAATTTCCCGGGAAATTTCCCGGGAAATTTCCCGGGGAAATTTCCCGGGAAATTTCCCGGGAAATTTCCCGGG'

    k = 1      ## k as in k-mer (e.g. 1-mer is a substring with length of one, etc.)
    unique = [] ## list of unique substrings (items removed when found not to be unique) -- will be returned at end
    check = []  ## list of substrings that have already been checked

    count = 0   ## used to cycle through string with second 'while' loop

    while len(unique) == 0: ## run as long as unique is empty (haven't found answer) at the end of a cycle

        while count < len(string):  ## search entire string

            x = string[count:(count + k)]   ## sliding window of length 'k' along string

            if x not in check:  ## if substring hasn't been looked at:
                check.append(x)     ## add to substrings that have been considered
                unique.append(x)    ## this is unique (for now -- removed when disproved)
            else:
                if x in unique:     ## if a second copy of substring is found:
                    unique = [y for y in unique if y != x]  ## substring removed from unique

            count += 1  ## shift window along string

        k += 1  ## keep increasing k until unique substrings are found (start small, increase as needed)
                    ## ^ this may be computationally faster because program doesn't have to search all of the
                    ## long substrings unnecessarily -- if a small unique substring is found, search is over

        count = 0   ## re-set reading window to beginning of string when searching for a new k-value

    for string in unique:
        print(len(string))  ## could have multiple values in unique (same length, all unique)-- print the length of each

"""
6. Bacterial genomes are often circular. To transform to a linear form, some genome assembly programs
will pick a random location in the genome to break the circle. Thus, it is possible that running the same
program multiple times we would get different answers, corresponding to different circular rotations of
the same string. Provide the psuedo-code that will determine if two DNA strings are circular rotations of
each other. For example TTGATC is a circular rotation of ATCTTG. You must state all assumptions.

ASSUMPTIONS: 
-The two strings are the same length
-The two strings are from the same DNA strand, running in the same direction
-Apart from being circular rotations of each other, the strings are identical

"""
def six():
    string1 = 'TTGATC'
    string2 = 'ATCTTG'

    double = string1 * 2

    count1 = 0
    count2 = 0

    while count1 < len(double) and count2 < len(string2):   ## slide windows along doubled first string and second string
        if string2[count2] == double[count1]:   ## if these windows match:
            count1 += 1                         ## slide both windows by one base (matching a substring)
            count2 += 1

        else:                   ## if they don't match, keep looking for start of string2 in doubled string1
            if count2 == 0:
                count1 += 1
            else:
                count2 = 0      ## if string2 has been partially matched in doubled string1, need to start over (find exact match)

    index = count1 - len(string2)   ## starting location of string2 in doubled string1

    rev = double[index:(index + len(string2))]  ## supposed match of rotated string2 with string1

    if rev == string2:
        print('These two strings ARE circular rotations of each other.')
    else:
        print('These two strings ARE NOT circular rotations of each other.')

"""
7. We can define a set of distinct substrings of a string S that includes all substrings. However, each
repeat is only represented once.

You are given a suffix tree of S. Provide the pseudo-code for an algorithm that counts the number of
distinct substrings of S. For full credit, this should run in O(n) time. 

First, take the suffix tree and trace back each end node to the beginning node, and reverse the string to get all possible
suffixes. For the sake of this code, I generated the suffixes of 'AATATT'. Then subtract all shorter suffixes from each 
suffix to obtain all possible substrings. 

This code is not completely functional but the comments / underlying structure should stand in for the pseudocode. 

"""
def seven():
    ## create suffix array
    string = 'AATATT'   ## string

    suffixes = []   ## list of suffixes

    count = 0

    while count < len(string):
        if count == 0:
            suffixes.append(string) ## add the entire string as one suffix
            count += 1
        else:
            suffixes.append(string[(count * -1):])  ## 
            count += 1

    suffixes.sort(key=lambda s: len(s)) ## sort suffixes by length



    ## find distinct substrings from suffixes
    substrings = []

    count = 0
    span = len(suffixes)

    while count < span:
        back = count
        while back >= 0:

            if back == count:
                if suffixes[back] not in substrings:  ## find better way to do this
                    substrings.append(suffixes[back])

            else:
                if "".join(suffixes[count].rsplit(suffixes[back])) not in substrings:
                    substrings.append("".join(suffixes[count].rsplit(suffixes[back])))

            back -= 1

        count += 1

    print(substrings)

def main():
    one()
    six()
    seven()

if __name__ == "__main__":
    main()