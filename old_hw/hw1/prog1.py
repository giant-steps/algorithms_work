"""
This docstring will provide information about the following code.


$ python prog1.py fasta_practice.txt codon_table.txt seq_output.txt 1
"""

## import statements
import sys

## function definitions
def translate(seq,codon_table,frame):
    protein_dict = {}   ## empty dictionary, will hold fasta IDs and sequences

    for key in seq:     ## loops through sequences in dictionary, which are seq[key]
        count = -1 + int(frame)
        protein = ''

        while count < len(seq[key]):

            if len(seq[key][count:(count + 3)]) == 3:
                protein += codon_table[seq[key][count:(count + 3)]]

            count += 3

        protein_dict[key] = protein

    return protein_dict

def cleave(arg1):   ## will find putative cleavage sites, dict from translate() as input
    new_keys = {}
    for key in arg1:
        #print(key)         ############
        #print(arg1[key])   ###########

        text = arg1[key]
        count = 0
        sites = []
        while count < len(text):
            if text[count:(count+2)] == 'KK' or text[count:(count+2)] == 'KH' or text[count:(count+2)] == 'KR' or text[count:(count+2)] == 'HK' or text[count:(count+2)] == 'HH' or text[count:(count+2)] == 'HR' or text[count:(count+2)] == 'RK' or text[count:(count+2)] == 'RH' or text[count:(count+2)] == 'RR':
                sites.append(count)
            count += 1

        #print(sites)   ########

        new_keys[key] = key + ' ' + str(sites)

    return new_keys



    ## one way to do it is to create a new dict (key:value == old descriptor:new descriptor)
    ## then return this dict
        ## main function will use a combo of input & output dicts to write to file
    ## for key in old_dict:
        ## write new_dict[old descriptor / key]
        ## write old_dict[old descriptor / key]

    ## I want to take dictionary, and for each value (sequence), use a sliding window to look for hits (PCSs)
    ## store indices of hits in a list, then append this to key (may need to create a new dict?)
    ## output is dict -- same dict except keys are original descriptors with list of indices appended to end

## main function definition
def main():
    fasta_dict = {}
    cod_tab = {}
    with open(sys.argv[1],'r') as infile, open(sys.argv[2],'r') as codons, open(sys.argv[3],'a') as outfile:
        for line in infile:
            line = line.rstrip()


            ####    OLD CODE -- LOOK IT OVER
            if line == '':
                idstore = 'empty'
                continue
            elif line.startswith('>'):
                idstore = line
                continue
            elif idstore.startswith('>'):           #this 'try, except' setup helps if there are returns interpreted in a multi-line DNA sequence
                try:
                    if fasta_dict[str(idstore[1:])] == 1:
                        pass
                    fasta_dict[str(idstore[1:])] += line
                except KeyError:
                    fasta_dict[str(idstore[1:])] = line

        for line in codons:
            line = line.rstrip()
            line = line.split('\t')
            cod_tab[line[0]] = line[2]

            ####    OLD CODE -- LOOK IT OVER

        dict_proteins = translate(fasta_dict,cod_tab,sys.argv[4])
    ### YOU NEED TO RUN FUNCTION 3 TIMES & APPEND ALL TO DICT
        ## possibly add reading frame to descriptor?


    #print(dict_proteins)    #############

        cleaver = cleave(dict_proteins)
        ## output of this is a dict

        #print(cleaver)      #############


        for key in dict_proteins:
            outfile.write(cleaver[key] + '\n')
            outfile.write(dict_proteins[key] + '\n')

    ## write new dict to the output file




    ## now use another function on this to search for putative cleavage sites & modify keys
    ## may have to create a new dict? not sure if you can modify keys
    ## add cleavage sites to keys
    ## then write that dict to a file here in the main function



## run main function
if __name__ == "__main__":
    main()

