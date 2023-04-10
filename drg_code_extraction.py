import pandas as pd
import os
from tqdm import tqdm
import json

def drg_code_extraction(subject_id):
    # Extracting DRG codes associated with a single patient id
    patient_df = pd.read_csv("Path/To//patients.csv")
    df = pd.read_csv("/content/drive/MyDrive/MIMIC/drgcodes.csv")

    if (not os.path.exists("Path/To/drg_code_patientwise")):
        os.mkdir("Path/To/drg_code_patientwise")

    drg_list = []

    for index, row in df.loc[df['subject_id'] == subject_id].iterrows():
            # extracting all entries that match with the subject_id
            drg_list.append({"drg_type": row[2], "drg_code": row[3], "drg_description": row[4], "hadm_id": row[1]})

    return drg_list
