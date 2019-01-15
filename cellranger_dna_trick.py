
# coding: utf-8

# ### Tricking CellrangerDNA with Less base pairs than supported
# This trick allows you to sequence Genome or Exome libraries with fewer cycles than the recommended 2x150 or 2x100.


import pandas as pd
import numpy as np
# from tqdm import tqdm
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

# define file paths

# fastqs path
fastq_path = "/cluster/work/bewi/ngs/projects/tumorProfiler/analysis/sc_dna/CCGL1ANXX_2/fastqs_pe_26_58/"
# R2 fastq file
r2_fastq = "CCGL1ANXX_2_S1_L002_R2_001.fastq"
# R1 fastq file
r1_fastq = "CCGL1ANXX_2_S1_L002_R1_001.fastq"
# new fastq path
new_fastq_path = fastq_path+"tricked/unzipped/"


print(new_fastq_path+r1_fastq)
with open(new_fastq_path+r1_fastq,"a") as new_r1_fastq:

    with open(fastq_path+r1_fastq) as r1, open(fastq_path+r2_fastq) as r2: 
        i = 0
        read1 = ''
        read2 = ''
        for x, y in zip(r1, r2):

            read1 = x.strip()
            read2 = y.strip()
            #import ipdb; ipdb.set_trace() # debugging starts here
            if i%2 == 1: # trim read1 by 16
                read1 = read1[0:16]
                if i%4 == 1: # the sequence
                    read2_seq = Seq(read2)
                    read1 += str(read2_seq.reverse_complement())[0:42]
                if i%4 == 3:
                    read1 += read2[::-1][0:42]
            new_r1_fastq.write(read1)
            new_r1_fastq.write('\n')
            i += 1


