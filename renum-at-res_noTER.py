#!/usr/bin/python2.7
import sys, os, string

pdb = open(sys.argv[1],'r').readlines()
resdeb = 1
atdeb = 1
if len(sys.argv)>2: resdeb = int(sys.argv[2])
if len(sys.argv)>3: atdeb = int(sys.argv[3])
chain = False

#print >> sys.stderr, sys.argv[1], resdeb, atdeb

def check_letter(p,resnum,res,previous,previousletter):
    num=int(resnum[:-1])
    letter=resnum[-1]
    if p[2]=='P' or p[2]=='N' or letter!=previousletter:
        res+=1
    return(int(res),int(num),letter)

def check_noletter(p,resnum,res,previous):
    if p[2]=='P' or p[2]=='N' or resnum!=previous:
        res+=1
    return(int(res),int(resnum))

p=pdb[3].split()
previousletter="z"
previous=10000

at=atdeb-1
res=resdeb-1
deb=True
#print chain

for line in pdb:
    p=line.split()
    if p[0]=='ENDMDL' or p[0]=='END' or p[0]=='MODEL':
        print line[:-1]
        at=atdeb
        res=resdeb
        deb=True
        continue
    if p[0]=='TER':
        print line[:-1]
        previous=-100
        continue
    if p[0]!='ATOM':
        raise ValueError("non recognised line %s" %p)
    at+=1
    resnum=p[4]
    if p[4].isalpha():resnum=p[5]
    if resnum.strip()[-1].isalpha(): res,num,previousletter=check_letter(p,resnum,res,previous,previousletter)
    else: res,previous=check_noletter(p,int(resnum),int(res),previous)
    deb=False
    print "%s%4d%s%4d%s" % (line[:7], at, line[11:22], res, line[26:-1])

#os.system('rm '+PDB+'.pdb','r')
