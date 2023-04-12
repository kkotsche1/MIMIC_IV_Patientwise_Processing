import pandas as pd
from tqdm import tqdm
import os

def microbiology_extraction(subject_id):
  #EXTRACTING MICROBIOLOGY EVENTS
  df = pd.read_csv("MIMIC/microbiologyevents.csv", low_memory=False)
  microbiology_events = []

  for index, row in df.loc[df['subject_id'] == subject_id].iterrows():
    microbiology_events.append({"organism_name": str(row[15]), "hadm_id": str(row[2]), "chart_date": str(row[5]), "comments": str(row[-1]).strip(), "test_name": str(row[13]), "ab_name" :str(row[19]), "ab_dilution": str(row[22]), "ab_interpretation": str(row[-2])})
  del df
  return microbiology_events