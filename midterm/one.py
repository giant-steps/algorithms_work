"""
1. Provide the pseudo-code for an algorithm that will determine the length of the shortest substring that occurs exactly once in a genomic sequence of length N. You must provide all assumptions made for your algorithm.

how to go about this?

easiest to start with smallest substrings first, I think -- you know that there will be single character substrings

first search for 2-mers. if there are none found, return a particular message

add all 2-mers to a list, & any time one is already in the list, remove from list (doesn't occur exactly once)

then go to 3-mers...no, you shouldn't be searching through all 2-mers if there is a 3-mer that exists

maybe I should start from longest...

how would that work?

the entire string occurs exactly one time. start with that. you will have a current shortest substring occurring exactly once that will be discarded when a shorter one is found

there are 2 substrings with (length - 1) length. see if these are unique.
	if not, keep whole string as current winner and keep looking
	if so, try (l - 2)
		search all of these -- if any are unique, these are the current winners
		go another level down...etc.

NOPE -- I was right the first time
	the point is to write your code in a way that if you find the answer early on, you don't have to keep looking. and also you want it to be likely that you find your answer early on

it could be 1-mer -- if a character is used only once -- then you would end there

look for unique 2-mer -- if so, done ; if not, go to 3-mers

once you find a unique k-mer at a given k-level, return all unique k-mers for that k and you are finished


This algorithm will look for the shortest unique k-mer, starting with k = 1 and increasing k by increments of 1 until a unique value is found. For example, if there is a character used only once, a unique value would be found at k = 1, all unique 1-mers would be returned, and the algorithm would stop. If no unique 1-mers are found, k increases to 2. And so on.


"""

string = 'AAATTTCCCGGGAAATTTCCCGGGAAATTTCCCGGGAAATTTCCCGGGAAATTTCCCGGGGAAATTTCCCGGGAAATTTCCCGGGAAATTTCCCGGG'
        ## ^string we are searching
k = 1      ## k as in k-mer (e.g. 1-mer is a substring with length of one, etc.)
unique = [] ## list of unique substrings (items removed when found not to be unique) -- will be returned at end
check = []  ## list of substrings that have already been checked

count = 0   ## used to cycle through string with second while loop

while len(unique) == 0: ## run as long as unique is empty (haven't found answer) at the end of a cycle

    while count < len(string):  ## search entire string

        x = string[count:(count + k)]   ## sliding window along string

        if x not in check:  ## if substring hasn't been looked at:
            check.append(x)     ## add to substrings that have been considered
            unique.append(x)    ## this is unique (for now -- removed when disproved)
        else:
            if x in unique:     ## if a second copy of substring is found:
                unique = [y for y in unique if y != x]  ## substring removed from unique

        count += 1  ## shift window along string

    k += 1  ## keep increasing k until unique substrings are found (start small, increase as needed)
                ## ^ this is computationally faster because we don't have to search all of the really
                ## long substrings unnecessarily -- if we find small unique substring, search is over

    count = 0   ## re-set to beginning of string when searching a new k-value

print(unique)