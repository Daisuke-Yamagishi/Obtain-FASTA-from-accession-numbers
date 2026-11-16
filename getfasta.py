import sys
args = sys.argv
#Import modules from biopython.
from Bio import Entrez, SeqIO
#Needs to write your email address to use Entrez API. DO NOT use someone else's email address and fake email adress.
Entrez.email = "Please write your email adress here"
from Bio.SeqFeature import SeqFeature, FeatureLocation
from Bio.SeqRecord import SeqRecord
from pathlib import Path
import pathlib

handle = Entrez.einfo()
result = handle.read()

#Input file name here.
data_name = args[1]
#Open the list file.
f = open(data_name, 'r')
#Read accession number list from the file and make a list of accession numbers.
name_list = f.readlines()
for i in name_list :
    i = i.replace('\n','')
    #get fasta sequence from NCBI using Entrez API.
    handle = Entrez.efetch(db = 'nucleotide', id = i , rettype = 'fasta', retmode = 'text')
    print(handle.read())
f.close()
