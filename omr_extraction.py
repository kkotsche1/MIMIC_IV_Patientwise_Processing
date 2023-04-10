import pandas as pd

def omr_extraction(subject_id):
  #EXTRACTING OMR ENTRIES - IE WEIGHT, HEIGHT, BMI

  df = pd.read_csv("MIMIC/omr.csv")
  omr_entries = []

  for index, row in df.loc[df['subject_id'] == subject_id].iterrows():
    omr_entries.append({"chart_date": str(row[1]), "result_name":str(row[3]), "result_value":str(row[4])})

  del df
  return omr_entries
