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

def main():
    one()

if __name__ == "__main__":
    main()