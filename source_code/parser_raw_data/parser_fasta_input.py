import pandas as pd
import sys
import os
from Bio import SeqIO

fasta_doc = sys.argv[1]
path_export = sys.argv[2]
name_path_to_create = sys.argv[3]
character_split = sys.argv[4]

matrix_data = []

with open(fasta_doc) as handle:
    for record in SeqIO.parse(handle, "fasta"):
        
        id_seq = str(record.id).split(character_split)[0]
        response= float(str(record.id).split(character_split)[-1])
        sequence =str(record.seq)

        row = [id_seq, sequence, response]
        matrix_data.append(row)

df_data = pd.DataFrame(matrix_data, columns=['id_seq', 'sequence', 'response'])

command = "mkdir {}{}".format(path_export, name_path_to_create)
os.system(command)

df_data.to_csv("{}{}\\parsed_dataframe.csv".format(path_export, name_path_to_create), index=False)