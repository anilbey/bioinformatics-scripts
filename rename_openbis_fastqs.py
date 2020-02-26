import os
import argparse

"""
renames the fastqs in format A into format B which is accepted by cellranger-dna.
format A: MERGED_BSSE_QGF_113500_HHVC7BGX9_1_MY5BB_T_scDNA_500c_r1_v1_0_SI-GA-E2_S8_L001_I1_001.fastq.gz
format B: MY5BB_S8_L001_I1_001.fastq.gz
"""

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", required=True, help="fastqs path")
args = parser.parse_args()

fastqs_dir = args.path + "/"


def rename_9(s_name):
    split_name = s_name.split("_")
    new_name = "_".join(split_name[6:7] + split_name[-4:])
    return new_name


for filename in os.listdir(fastqs_dir):
    if filename.startswith("MERGED_BSSE") and filename.endswith(".gz"):
        # print(filename)
        print(rename_9(filename))
        os.rename(fastqs_dir + filename, fastqs_dir + rename_9(filename))
