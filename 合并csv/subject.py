import pandas as pd
from tqdm import trange
from time import sleep

print("\n")

inventory = pd.read_csv("/Users/jingyichu/Documents/DwD/合并csv/broadsides_inventory.csv", encoding='utf-8', index_col=0, parse_dates=True, header=None)
inventory.columns = ["title"]
inventory["selfmark"] = None
inventory["PlainTitle"] = None
for inven_index, inven_row in inventory.iterrows():
    inven_row[1] = inven_row[0].split(' - ')[-1]
    inven_row[2] = inven_row[0].split(' - ')[0]
    # print(inven_row[2])

inventory["subject"] = None
inventory["year"] = None
print(inventory.head())

subject = pd.read_csv("/Users/jingyichu/Documents/DwD/合并csv/subject.csv", encoding='utf-8', index_col=0, parse_dates=True)
subject["PlainTitle"] = None
for subj_index, subj_row in subject.iterrows():
    try:
        subj_row[5] = subj_row[3].split("'")[1]
    except IndexError:
        pass

subject_dict_sm = dict(zip(list(subject.selfmark), list(subject.key)))
# print(subject_dict_sm)
year_dict_sm = dict(zip(list(subject.selfmark), list(subject.year)))


subject_dict_pt = dict(zip(list(subject.PlainTitle), list(subject.key)))
# print(len(subject_dict_pt))
year_dict_pt = dict(zip(list(subject.PlainTitle), list(subject.year)))


for inven_index, inven_row in inventory.iterrows():
    inven_row[3] = subject_dict_sm.get(inven_row[1])
    inven_row[4] = year_dict_sm.get(inven_row[1])
    # print(subject_dict_sm.get(inven_row[1]))
    if inven_row[3] == None:
        inven_row[3] = subject_dict_pt.get(inven_row[2])
        inven_row[4] = year_dict_pt.get(inven_row[2])



inventory.to_csv("new_inventory.csv")
# print(inventory.head())

print("\n")

