import pandas as pd

def discharge_report_extraction(subject_id):
    # EXTRACTING DISCHARGE REPORTS
    df = pd.read_csv("/content/drive/MyDrive/MIMIC/discharge.csv")
    df_ = pd.read_csv("/content/drive/MyDrive/MIMIC/discharge_detail.csv")
    discharge_reports = []

    for index, row in df.loc[df['subject_id'] == subject_id].iterrows():
        hadm_id = row[2]
        note_type = row[4]
        chart_time = row[5]
        text = row[-1]

        for index_, row_ in df_.loc[df_['note_id'] == row[0]].iterrows():
            field_name = row_[2]
            field_value = row_[3]

        discharge_reports.append(
            {"hadm_id": str(hadm_id), "note_type": str(note_type), "chart_time": str(chart_time), "text": str(text),
             "field_name": str(field_name), "field_value": str(field_value)})
    del df
    del df_
    return discharge_reports