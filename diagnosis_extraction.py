import os
import pandas as pd
from tqdm import tqdm
import json

def diagnosis_extraction(subject_id):
    # Creating a for loop to iterate over each patients whos records we want to extract

    patient_df = pd.read_csv("Filepath/to/patients.csv")

    df = pd.read_csv("Filepath/to/diagnoses_icd.csv")
    diagnosis_df = pd.read_csv("Filepath/to/d_icd_diagnoses.csv")

    if (not os.path.exists("Filepath/to/diagnosis_patientwise")):
        os.mkdir("Filepath/to/diagnosis_patientwise")



    diagnosis_list = []

    for index, row in df.loc[df['subject_id'] == subject_id].iterrows():

            # extracting all entries that match with the subject_id
            icd_code = row[3]
            icd_version = row[4]
            hadm_id = row[1]
            diagnosis_text = ""
            for _index, _row in diagnosis_df.loc[diagnosis_df['icd_code'] == icd_code].iterrows():
                diagnosis_text = _row[2]
                diagnosis_list.append(
                    {"icd_code": icd_code, "icd_version": icd_version, "diagnosis_text": diagnosis_text,
                     "hadm_id": hadm_id})

    return diagnosis_list