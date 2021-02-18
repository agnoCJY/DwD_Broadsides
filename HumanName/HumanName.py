import nltk
from nameparser.parser import HumanName
from nltk.corpus import wordnet
import pandas as pd

def HumanName (text):
    person_list = []
    person_names=person_list
    def get_human_names(text):
        tokens = nltk.tokenize.word_tokenize(text)
        pos = nltk.pos_tag(tokens)
        sentt = nltk.ne_chunk(pos, binary = False)

        person = []
        name = ""
        for subtree in sentt.subtrees(filter=lambda t: t.label() == 'PERSON'):
            for leaf in subtree.leaves():
                person.append(leaf[0])
            if len(person) > 1: #avoid grabbing lone surnames
                for part in person:
                    name += part + ' '
                if name[:-1] not in person_list:
                    person_list.append(name[:-1])
                name = ''
            person = []
    #     print (person_list)

    names = get_human_names(text)
    for person in person_list:
        person_split = person.split(" ")
        for name in person_split:
            if wordnet.synsets(name):
                if(name in person):
                    person_names.remove(person)
                    break

    print(person_names)


    # # TODO 就是这里
    # places.cities = list(set(places.cities))
    # city_list.append(",".join(str(x) for x in places.cities))
    # print(city_list)
    # for i in range(len(city_list)):
    #     city_list[i] = str(city_list[i]).replace(',', ' ')
    # cities = " ".join(str(i) for i in city_list)
    # city_list = cities.split(" ")
    # print(city_list)
    # city_list = (", ".join(str(i) for i in city_list))

    return person_names

new_inventory = pd.read_csv("合并csv/new_inventory.csv", encoding='utf-8', index_col=0, parse_dates=True)
new_inventory['name'] = None
print(new_inventory.head())

full_name = []

for ni_index, ni_row in new_inventory.iterrows():
    if ni_row.name == 0:
        pass
    else:
        file_name = str(ni_row.name)
        file_path = 'nls-text-broadsides/' + file_name + '.txt'
        with open(file_path, 'r') as f:
            text = f.read()
        all_name = HumanName(text)
        ni_row['name'] = all_name
        if len(all_name) > 0:
            for item in all_name:
                full_name.append(item)

print(new_inventory.head())

new_inventory.to_csv("HumanName/inventory_name.csv")


name_time = pd.DataFrame(columns=['name', 'time'])

full_name_set = set(full_name)

for item in full_name_set:
    name_time = name_time.append(pd.DataFrame({'name':[item], 'time':[full_name.count(item)]}),ignore_index=True)

print(name_time.head())

name_time.sort_values(by='time', ascending=False)
name_time.to_csv("Frequency/new_name.csv")

sort_name = pd.read_csv("Frequency/new_name.csv", encoding='utf-8', index_col=0, parse_dates=True)
new_sort = sort_name.sort_values(by='time', ascending=False)
new_sort.to_csv("Frequency/new_sort_name.csv")

