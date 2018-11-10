"""

7. We can define a set of distinct substrings of a string S that includes all substrings. However, each repeat is
only represented once. For example, for the string S = AATATT, this set is:

{A, T, AA, AT, TA, TT, AAT, ATA, TAT, ATT, AATA, ATAT, TATT, AATAT, ATATT, AATATT}

You are given a suffix tree of S. Provide the pseudo-code for an algorithm that counts the number of distinct substrings of S. For full credit, this should run in O(n) time.


input: suffix tree
    it would be useful to have an example here


count distinct substrings


AATATT

make the suffix tree

AATATT$
ATATT$
ATT$
T$
TATT$
TT$






"""

string = 'AATATT'

string1 = string + '$'

suffixes = []

count = 0

while count < len(string1):
    if count == 0:
        suffixes.append(string1)
        count += 1
    else:
        suffixes.append(string1[(count * -1):])
        count += 1

print(suffixes)