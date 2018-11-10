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

suffixes = []

count = 0

while count < len(string):
    if count == 0:
        suffixes.append(string)
        count += 1
    else:
        suffixes.append(string[(count * -1):])
        count += 1

suffixes.sort(key = lambda s: len(s))
#print(suffixes[0])

#print("".join(suffixes[2].rsplit(suffixes[0])))

substrings = []

for suffix in suffixes:
    if suffix not in substrings:
        substrings.append(suffix)

    ## better way here -- don't check length on every element -- use counter so you never get to longer suffixes
        ## will improve runtime

    for other in suffixes:
        if len(other) < len(suffix) and "".join(suffix.rsplit(other)) not in substrings:
            substrings.append("".join(suffix.rsplit(other)))

print(substrings)


## https://stackoverflow.com/questions/18454570/how-can-i-subtract-two-strings-in-python    credit this
    ## with idea for how to subtract two strings


## sort suffixes by length

## then run your idea where you iterate through suffixes, add each suffix to list of substrings (if not included),
    ## add each suffix minus every shorter suffix to list of substrings (if not included)

    ## this will work to get all unique substrings

    ## will this run in O(n) time?

    ## my concern is that you are searching list of substrings every time a substring is added to check for duplicates
    ## would it be faster to remove these at the end? think about this in terms of runtime


    ## think about runtime in general

    ## for now, write the code, get it to work, then maybe improve upon it for O(n) runtime