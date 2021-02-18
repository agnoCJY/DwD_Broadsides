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

    #TODO 就是这里
    places.cities = list(set(places.cities))
    city_list.append(",".join(str(x) for x in places.cities))
    print(city_list)
    for i in range(len(city_list)):
        city_list[i] = str(city_list[i]).replace(',', ' ')
    cities = " ".join(str(i) for i in city_list)
    city_list = cities.split(" ")
    print(city_list)
    city_list = (", ".join(str(i) for i in city_list))

    return person_names

new_inventory = pd.read_csv("合并csv/new_inventory.csv", encoding='utf-8', index_col=0, parse_dates=True)
new_inventory['name'] = None
print(new_inventory.head())


for ni_index, ni_row in new_inventory.iterrows():
    if ni_row.name == 0:
        pass
    else:
        file_name = str(ni_row.name)
        file_path = 'nls-text-broadsides/' + file_name + '.txt'
        with open(file_path, 'r') as f:
            text = f.read()
        ni_row['name'] = HumanName(text)

print(new_inventory.head())

new_inventory.to_csv("HumanName/inventory_name.csv")
