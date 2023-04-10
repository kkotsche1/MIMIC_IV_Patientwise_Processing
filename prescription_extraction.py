import pandas as pd

def prescription_extraction(subject_id):
  #GETTING PRESCRIPTIONS DATA FOR INDIVIDUAL SUBJECT ID

  df = pd.read_csv("/content/drive/MyDrive/MIMIC/prescriptions.csv", low_memory = False)
  prescriptions = []


  for index, row in df.loc[df['subject_id'] == subject_id].iterrows():
    prescriptions.append({"poe_id":str(row[3]), "hadm_id": str(row[1]), "start_time":str(row[6]), "stop_time":str(row[7]), "drug_type":str(row[8]), "drug":str(row[9]), "prod_strength": str(row[13]), "doses_per_24_hrs": str(row[-2]), "route":str(row[-1]), "form_unit": str(row[-3]), "dose": f"{row[15]}{row[16]}"})

  del df
  return prescriptions