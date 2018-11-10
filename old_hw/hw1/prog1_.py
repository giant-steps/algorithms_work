"""
This docstring will provide information about the following code.


$python prog1_.py fasta_practice.txt codon_table.txt seq_output.txt

    where "fasta_practice.txt" is your input fasta file, "codon
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
        text = arg1[key]
        count = 0
        sites = []
        while count < len(text):
            if text[count:(count+2)] == 'KK' or text[count:(count+2)] == 'KH' or text[count:(count+2)] == 'KR' or text[count:(count+2)] == 'HK' or text[count:(count+2)] == 'HH' or text[count:(count+2)] == 'HR' or text[count:(count+2)] == 'RK' or text[count:(count+2)] == 'RH' or text[count:(count+2)] == 'RR':
                sites.append(count)
            count += 1

        new_keys[key] = key + ' ' + str(sites)

    return new_keys

## main function definition
def main():
    fasta_dict = {}
    cod_tab = {}
    with open(sys.argv[1],'r') as infile, open(sys.argv[2],'r') as codons, open(sys.argv[3],'a') as outfile:
        for line in infile:
            line = line.rstrip()

            if line == '':
                idstore = 'empty'
                continue
            elif line.startswith('>'):
                idstore = line
                continue
            elif idstore.startswith('>'):
                try:
                    fasta_dict[str(idstore[1:])] += line
                except KeyError:
                    fasta_dict[str(idstore[1:])] = line

        for line in codons:
            line = line.rstrip()
            line = line.split('\t')
            cod_tab[line[0]] = line[2]

        dict_proteins1 = translate(fasta_dict,cod_tab,1)
        dict_proteins2 = translate(fasta_dict, cod_tab,2)
        dict_proteins3 = translate(fasta_dict, cod_tab,3)

        cleaver1 = cleave(dict_proteins1)
        cleaver2 = cleave(dict_proteins2)
        cleaver3 = cleave(dict_proteins3)

        for key in dict_proteins1:

            outfile.write(cleaver1[key] + ' ' + 'reading_frame_1'+ '\n')
            outfile.write(dict_proteins1[key] + '\n')

            outfile.write(cleaver2[key] + ' ' + 'reading_frame_2' + '\n')
            outfile.write(dict_proteins2[key] + '\n')

            outfile.write(cleaver3[key] + ' ' + 'reading_frame_3' + '\n')
            outfile.write(dict_proteins3[key] + '\n')

## run main function
if __name__ == "__main__":
    main()

