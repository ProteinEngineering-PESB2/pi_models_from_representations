import pandas as pd
import sys
import os

#command line params
df_data = pd.read_csv(sys.argv[1])
path_export = sys.argv[2]
column_seq = sys.argv[3]
column_response = sys.argv[4]
column_id = sys.argv[5]
name_path_to_create = sys.argv[6]

#create a data frame
print("Reading dataframe")
df_export = pd.DataFrame()

#create dataframe
print("Creating dataframe")
for column in [column_id, column_seq, column_response]:
    df_export[column] = df_data[column]

#create dir
command = "mkdir {}{}".format(path_export, name_path_to_create)
print(command)
os.system(command)

#export dataframe
print("Export dataframe")
df_export.to_csv("{}{}\\parsed_dataframe.csv".format(path_export, name_path_to_create), index=False)
