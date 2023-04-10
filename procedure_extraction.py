import pandas as pd

def procedure_extraction(subject_id):
    # Extracting Procedures for individual subject_IDs

    df = pd.read_csv("MIMIC/procedures_icd.csv")
    df_ = pd.read_csv("MIMIC/d_icd_procedures.csv")
    procedures = []

    for index, row in df.loc[df['subject_id'] == subject_id].iterrows():
        icd_code = row[4]
        icd_version = row[5]
        hadm_id = row[1]
        chart_date = row[3]
        for index_, row_ in df_.loc[df_['icd_code'] == icd_code].iterrows():
            long_title = row_[2]

        procedures.append({"icd_code": str(icd_code), "icd_version": str(icd_version), "hadm_id": str(hadm_id),
                           "chart_date": str(chart_date), "long_title": str(long_title)})

    del df
    del df_
    return procedures