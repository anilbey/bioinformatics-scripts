# coding: utf-8

# ### Tricking CellrangerDNA with Less base pairs than supported
# This trick allows you to sequence Genome or Exome libraries with fewer cycles than the recommended 2x150 or 2x100.


import pandas as pd
import numpy as np
from tqdm import tqdm
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
import argparse
import gzip

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", required=True, help="fastqs path")
parser.add_argument("-r1", "--read1", required=True, help="read 1 fastq")
parser.add_argument("-r2", "--read2", required=True, help="read 2 fastq")
parser.add_argument("-o", "--output", required=True, help="output fastqs path")

args = parser.parse_args()


# define file paths

# fastqs path
fastq_path = args.path + "/"
# R2 fastq file
r2_fastq = args.read2
# R1 fastq file
r1_fastq = args.read1
# new fastq path
new_fastq_path = args.output + "/"


with gzip.open(new_fastq_path + r1_fastq, "wb") as new_r1_fastq:

    with gzip.open(fastq_path + r1_fastq, "rt") as r1, gzip.open(
        fastq_path + r2_fastq, "rt"
    ) as r2:
        i = 0
        read1 = ""
        read2 = ""
        for x, y in tqdm(zip(r1, r2)):

            read1 = x.strip()
            read2 = y.strip()
            # import ipdb; ipdb.set_trace() # debugging starts here
            if i % 2 == 1:  # trim read1 by 16
                read1 = read1[0:16]
                if i % 4 == 1:  # the sequence
                    read2_seq = Seq(read2)
                    read1 += str(read2_seq.reverse_complement())[0:42]
                if i % 4 == 3:
                    read1 += read2[::-1][0:42]
            new_r1_fastq.write(read1.encode())
            new_r1_fastq.write("\n".encode())
            i += 1
