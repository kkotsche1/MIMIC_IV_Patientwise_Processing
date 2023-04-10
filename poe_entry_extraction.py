import pandas as pd

def poe_entry_extraction(subject_id):
    # EXTRACTING POE ENTRIES FOR INDIVIDUAL SUBJECT IDS
    df = pd.read_csv("path/to/poe.csv", low_memory=False)
    df_ = pd.read_csv("path/to/poe_detail.csv")
    poe_entries = []

    for index, row in df.loc[df['subject_id'] == subject_id].iterrows():
        poe_id = row[0]
        hadm_id = row[3]
        field_name = "nan"
        field_value = "nan"

        for index_, row_ in df_.loc[df_['poe_id'] == poe_id].iterrows():
            field_name = row_[3]
            field_value = row_[4]

        poe_entries.append({"order_type": str(row[5]), "hadm_id": str(hadm_id), "order_time": str(row[4]),
                            "order_subtype": str(row[6]), "transaction_type": str(row[7]),
                            "discontinue_of_poe_id": row[8], "discontinued_by_poe_id": row[9],
                            "field_name": str(field_name), "field_value": str(field_value)})

    del df
    del df_
    return poe_entries