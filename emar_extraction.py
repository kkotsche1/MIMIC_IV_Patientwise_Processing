import pandas as pd
import os
from tqdm import tqdm
import json


def emar_extraction(subject_id):
    # Extracting EMARs for individual patients

    df = pd.read_csv("path/to/emar.csv")
    emar_list = []

    patient_df = pd.read_csv("path/to/patients.csv")
    if (not os.path.exists("path/to/emar_patientwise")):
        os.mkdir("path/to/emar_patientwise")



    for index, row in df.loc[df['subject_id'] == subject_id].iterrows():
            emar_list.append({"charttime": row[7], "medication": row[8], "event_txt": row[9], "scheduletime": row[10],
                              "emar_id": row[2], "hadm_id": row[1]})

        # Extracting EMAR Details for individual patients and appending it to the original emar list

        #EMAR FILE HAS BEEN SPLIT INTO 5 INDIVIDUAL CSVs PRIOR TO RUNNING THIS CODE FOR RAM REASONS
    for index_ in [0, 1, 2, 3, 4, 5]:
            df_detail = pd.read_csv(f"path/to/emar_detail{index_}.csv")
            for list_index, item in enumerate(emar_list):
                for index, row in df_detail.loc[df_detail['emar_id'] == item["emar_id"]].iterrows():
                    emar_list[list_index]["administration_type"] = row[4]
                    emar_list[list_index]["product_description"] = row[17]
                    emar_list[list_index]["dose_given"] = row[11] + row[12]
                    emar_list[list_index]["route"] = row[24]

            del df_detail
    return emar_list