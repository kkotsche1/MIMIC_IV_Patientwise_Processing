import pandas as pd

for i,chunk in enumerate(pd.read_csv("MIMIC/labevents.csv", chunksize=10000000)):
    chunk.to_csv('MIMIC/labevents{}.csv'.format(i), index=False)

for i,chunk in enumerate(pd.read_csv("MIMIC/emar_detail.csv", chunksize=10000000)):
    chunk.to_csv('MIMIC/emar_detail{}.csv'.format(i), index=False)

for i,chunk in enumerate(pd.read_csv("MIMIC/labevents.csv", chunksize=10000000)):
    chunk.to_csv('MIMIC/labevents{}.csv'.format(i), index=False)