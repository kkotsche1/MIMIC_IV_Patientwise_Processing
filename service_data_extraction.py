import pandas as pd

def service_data_extraction(subject_id):
  #EXTRACTING TRANSFER DATA FOR INDIVIDUAL SUBJECT ID, KEY AT THE FOLLOWING WEBSITE
  #https://github.com/MIT-LCP/mimic-iv-website/blob/master/content/hosp/services.md

  df = pd.read_csv("MIMIC/services.csv")
  services = []


  for index, row in df.loc[df['subject_id'] == subject_id].iterrows():
    services.append({"hadm_id": str(row[1]), "transfer_time": str(row[2]), "prev_service" : str(row[3]), "curr_service": str(row[4])})
  del df
  return services
