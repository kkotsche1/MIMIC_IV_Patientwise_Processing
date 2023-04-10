import pandas as pd

def radiology_report_extraction(subject_id):
  #EXTRACTING RADIOLOGY REPORTS
  df = pd.read_csv("/content/drive/MyDrive/MIMIC/radiology.csv")
  df_ = pd.read_csv("/content/drive/MyDrive/MIMIC/radiology_detail.csv")
  radiology_reports = []
  for index, row in df.loc[df['subject_id'] == subject_id].iterrows():

    chart_time = row[5]
    text = row[7]
    note_type = row[3]
    note_id = row[0]

    for index_, row_ in df_.loc[df_['note_id'] == note_id].iterrows():
      field_name = row_[2]
      field_value = row_[3]

    radiology_reports.append({"chart_time": str(chart_time), "text": str(text), "note_type": str(note_type), "field_name" : str(field_name), "field_value":str(field_value)})
  del df
  del df_

  return radiology_reports