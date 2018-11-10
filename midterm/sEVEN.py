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


substrings = []

count = 0
span = len(suffixes)

while count < span:
    back = count
    while back >= 0:

        if back == count:
            substrings.append(suffixes[back])

        else:
            substrings.append("".join(suffixes[count].rsplit(suffixes[back])))

        back -= 1


    count += 1


print(substrings)



## sort suffixes by length

## then run your idea where you iterate through suffixes, add each suffix to list of substrings (if not included),
    ## add each suffix minus every shorter suffix to list of substrings (if not included)

    ## this will work to get all unique substrings

    ## will this run in O(n) time?

    ## my concern is that you are searching list of substrings every time a substring is added to check for duplicates
    ## would it be faster to remove these at the end? think about this in terms of runtime


    ## think about runtime in general

    ## for now, write the code, get it to work, then maybe improve upon it for O(n) runtime