"""

6. Bacterial genomes are often circular. To transform to a linear form, some genome assembly programs will pick a
random location in the genome to break the circle. Thus, it is possible that running the same program multiple times
 we would get different answers, corresponding to different circular rotations of the same string. Provide the
  psuedo-code that will determine if two DNA strings are circular rotations of each other. For example TTGATC is a
  circular rotation of ATCTTG. You must state all assumptions.


    one assumption is that the strings are identical in length

"""

string1 = 'TTGATC'
string2 = 'ATCTTG'


#string1 = 'ATCGACTGACGTATTATTATCGGGCGCGGCCCATGCTACGTATGCGACGTATCGATGCGTACGAGTCTGACTGATCGATCTGACGTA'
#string2 = 'CTGACTGATCGATCTGACGTAATCGACTGACGTATTATTATCGGGCGCGGCCCATGCTACGTATGCGACGTATCGATGCGTACGAGT'



double = string1 * 2

count1 = 0
count2 = 0

while count1 < len(double) and count2 < len(string2):
    if string2[count2] == double[count1]:
        count1 += 1
        count2 += 1

    else:
        if count2 == 0:
            count1 += 1
        else:
            count2 = 0

index = count1 - len(string2)

rev = double[index:(index + len(string2))]

if rev == string2:
    #print(rev)
    print('These two strings ARE circular rotations of each other.')
else:
    print('These two strings ARE NOT circular rotations of each other.')