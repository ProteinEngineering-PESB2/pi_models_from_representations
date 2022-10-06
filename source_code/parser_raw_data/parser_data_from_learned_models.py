import pandas as pd
import sys
import os

#command line params
df_data = pd.read_csv(sys.argv[1])
path_export = sys.argv[2]
column_seq = sys.argv[3]
column_response = sys.argv[4]
column_id = sys.argv[5]

#create a data frame
df_export = pd.DataFrame()

#create 
for column in [column_id, column_seq, column_response]:
    df_export[column] = df_data[column]
