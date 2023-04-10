import os
import pandas as pd
from tqdm import tqdm
import json


def lab_item_extraction(subject_id):

  #EXTRACTING LAB EVENTS USING PATIENT DATA AND LABCODE DATA
  lab_events = []

  #LABCODE DATA
  df_ = pd.read_csv("path/to/d_labitems.csv")

  for index in range(0,12):
    #PATIENT DATA
    df = pd.read_csv(f"path/to/labevents{index}.csv")
    #MATCHING LAB ROWS FOR SPECIFIC SUBJECT_ID
    for index, row in df.loc[df['subject_id'] == subject_id].iterrows():
      #MATCHING LAB ITEMID TO MASTER SHEET TO GET THE RELEVANT LABITEM NAME
      for index_, row_ in df_.loc[df_['itemid'] == row[4]].iterrows():
        labitem = row_[1]

      if f"{row[9]}" == "nan":
        continue
      if f"{row[10]}" != "nan":
        lab_events.append({"chart_time" : row[6], "hadm_id": row[2], "value": f"{row[9]}{row[10]}", "ref_lower_upper": [row[11], row[12]], "labitem": labitem})
      else:
        lab_events.append({"chart_time" : row[6], "hadm_id": row[2], "value": f"{row[9]}", "ref_lower_upper": [row[11], row[12]], "labitem": labitem})

    del df
  del df_
  return lab_events
