import pandas as pd
import os
import json
from tqdm import tqdm_notebook
from individual_master_list import individual_master_list


#Selecting a user ID for which to compile information

df = pd.read_csv("MIMIC/patients.csv")

#OG_Length included to continue off where previous runs may have been cut short.
og_length = len(os.listdir("C:/Users/Admin/PycharmProjects/MIMIC_IV_Patientwise_Processing/individual_subject_files"))

for index, row in df.iterrows():
  if index > og_length:
    print(index)
    subject_id = row[0]
    final_dictionary = individual_master_list(subject_id)
    final_dictionary["gender"] = row[1]
    final_dictionary["anchor_age"] = row[2]
    final_dictionary["date_of_death"] = row[-1]

    with open (f"individual_subject_files/{subject_id}.json", "w") as f:
      json.dump(final_dictionary, f)
