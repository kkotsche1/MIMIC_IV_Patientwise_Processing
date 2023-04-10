import pandas as pd
import os
import json
from tqdm import tqdm_notebook
from individual_master_list import individual_master_list



### Depending on Ram capabilities, code might need to be adjusted to split larger CSV files for easier loading ###

# for i,chunk in enumerate(pd.read_csv("/content/drive/MyDrive/MIMIC/labevents.csv", chunksize=10000000)):
#     chunk.to_csv('/content/drive/MyDrive/MIMIC/labevents{}.csv'.format(i), index=False)
#     print(i)

#######################################################################################################################

#Selecting a user ID for which to compile information

df = pd.read_csv("MIMIC/patients.csv")

for index, row in df.iterrows():
  subject_id = row[0]
  final_dictionary = individual_master_list(subject_id)
  final_dictionary["gender"] = row[1]
  final_dictionary["anchor_age"] = row[2]
  final_dictionary["date_of_death"] = row[-1]

  with open (f"individual_subject_files/{subject_id}.json", "w") as f:
    json.dump(final_dictionary, f)
