import pandas as pd

def pharmacy_event_extraction(subject_id):
  #EXTRACTING PHARMACY ENTRIES

  df = pd.read_csv("MIMIC/pharmacy.csv", low_memory=False)
  pharmacy_entries = []


  for index, row in df.loc[df['subject_id'] == subject_id].iterrows():
    pharmacy_entries.append({"starttime": str(row[4]), "hadm_id":str(row[1]), "stoptime": str(row[5]), "medication": str(row[6]), "disp_schedule" : str(row[13]), "doses_per_24_hrs":str(row[19]), "status": str(row[8]), "route": str(row[11]), "frequency" : str(row[13])})

  del df
  return pharmacy_entries
