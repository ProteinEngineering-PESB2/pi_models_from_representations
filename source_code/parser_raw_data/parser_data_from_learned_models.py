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

#create a dictionary 
dict_columns = {"sequence":column_seq, "id_seq": column_id, "response": column_response}
#create a data frame
print("Reading dataframe")
df_export = pd.DataFrame()

#create dataframe
print("Creating dataframe")
for column in dict_columns:
    df_export[column] = df_data[dict_columns[column]]

#create dir
command = "mkdir {}{}".format(path_export, name_path_to_create)
print(command)
os.system(command)

#export dataframe
print("Export dataframe")
df_export.to_csv("{}{}\\parsed_dataframe.csv".format(path_export, name_path_to_create), index=False)
