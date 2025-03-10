#! /usr/bin/env python3

import sys

if len(sys.argv) <= 1:
    print('usage: python pdb2fasta.py file.pdb > file.fasta')
    exit()

input_file = open(sys.argv[1])

letters = {'ALA':'A','ARG':'R','ASN':'N','ASP':'D','CYS':'C','CYX':'C','GLU':'E',\
'GLN':'Q','GLY':'G','HIS':'H','HIE':'H','HIP':'H','HSD':'H', 'HSE':'H', 'ILE':'I','LEU':'L',\
'LYS':'K','MET':'M','MSE':'M','PHE':'F','PRO':'P','SER':'S','THR':'T',\
'TRP':'W','TYR':'Y','VAL':'V',\
'ADE':'A', 'GUA':'G', 'THY':'T', 'CYT':'C', 'URI':'U',\
'RA':'A', 'RG':'G',  'RC':'C', 'RU':'U',\
'DT':'T', 'DA':'A', 'DG':'G',  'DC':'C',\
}
for i in ['A', 'T', 'C', 'G', 'U']:
    letters.update(dict.fromkeys(i, i))
    for a in ['D', 'R']:
        letters.update(dict.fromkeys(a+i, i))
        for b in ['5', '3']:
            letters.update(dict.fromkeys([a+i+b, i+b],i))

print('>',sys.argv[1])
for line in input_file:
    toks = line.split()
    if toks[0] == "TER":
        sys.stdout.write("%s\n"%"/")
    if len(toks)<1 or toks[0] != 'ATOM' or line[16]=="B":
        continue
    if toks[2] == "CA" or toks[2] == "O3'":
        sys.stdout.write('%c' % letters[toks[3][-3:]])

sys.stdout.write('\n')
input_file.close()
