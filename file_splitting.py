import pandas as pd

# for i,chunk in enumerate(pd.read_csv("MIMIC/labevents.csv", chunksize=10000000)):
#     print(i)
#     chunk.to_csv('MIMIC/labevents{}.csv'.format(i), index=False)
#
# print("LABEVENTS SPLIT")

for i,chunk in enumerate(pd.read_csv("MIMIC/emar_detail.csv", chunksize=10000000, low_memory=False)):
    print(i)
    chunk.to_csv('MIMIC/emar_detail{}.csv'.format(i), index=False)

print("EMAR DETAIL SPLIT")
#
# for i,chunk in enumerate(pd.read_csv("MIMIC/labevents.csv", chunksize=10000000)):
#     print(i)
#     chunk.to_csv('MIMIC/labevents{}.csv'.format(i), index=False)
#
# print("LABEVENTS SPLIT")