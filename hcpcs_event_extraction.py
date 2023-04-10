import pandas as pd
import os
from tqdm import tqdm
import json


def hcpcs_event_extraction(subject_id):
    # EXCTRACTING HCPCS EVENTS
    df = pd.read_csv("MIMIC/hcpcsevents.csv")
    df_ = pd.read_csv("MIMIC/d_hcpcs.csv")
    hcpcs_events = []

    for index, row in df.loc[df['subject_id'] == subject_id].iterrows():
            chart_date = row[2]
            description = row[5]
            hadm_id = row[1]

            for index, row in df_.loc[df_['code'] == row[3]].iterrows():
                long_description = row[2]

            hcpcs_events.append(
                {"chart_date": chart_date, "description": description, "long_description": long_description,
                 "hadm_id": hadm_id})

    return hcpcs_events


