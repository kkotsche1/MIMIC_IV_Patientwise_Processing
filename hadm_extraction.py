import pandas as pd

def hadm_extraction(patient_id):
    df = pd.read_csv("MIMIC/admissions.csv")
    matches = df[df['subject_id'] == patient_id]

    final_dict_list = []
    for index, row in matches.iterrows():
        individual_dict = {
            'subject_id': row['subject_id'],
            'hadm_id': row['hadm_id'],
            'admittime': row['admittime'],
            'dischtime': row['dischtime'],
            'deathtime': row['deathtime'],
            'admission_type': row['admission_type'],
            'admission_location': row['admission_location'],
            'discharge_location': row['discharge_location']
        }
        final_dict_list.append(individual_dict)
    return final_dict_list


hadm_extraction(10000032)