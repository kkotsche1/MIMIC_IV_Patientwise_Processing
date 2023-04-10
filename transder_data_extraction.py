import pandas as pd


def transfer_data_extraction(subject_id):
  #EXTRACTING TRANSFER DATA 2
  df = pd.read_csv("/content/drive/MyDrive/MIMIC/transfers.csv")
  transfers = []

  for index, row in df.loc[df['subject_id'] == subject_id].iterrows():
    transfers.append({"event_type": str(row[3]), "care_unit": str(row[4]), "in_time": str(row[5]), "out_time": str(row[6])})

  del df
  return transfers