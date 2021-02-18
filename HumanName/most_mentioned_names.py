import heapq
import os
import pandas as pd
import pycountry, pycountry_convert as pc

# path = r'/Users/wanfangdu/Desktop/DS4D/projectgit/extracted/edition'
path = r"F:\Edin\1_2\Design with Data\Data\inventory_name_place.csv"
output_dir = r'F:\Edin\1_2\Design with Data\Project'


def find_most_mentioned_countries(file):

    data = pd.read_csv(file)
    city_list = data['name'].tolist()
    for i in range(len(city_list)):
        city_list[i] = str(city_list[i]).replace(',', ' ')
    cities = " ".join(str(i) for i in city_list)
    city_list = cities.split(" ")
    print(city_list)

    different_country_dictionary_list = []
    different_country = []


    if (len(city_list)>1):
        for k in range(len(city_list)):
            if city_list[k] not in different_country:
                different_country.append(city_list[k])
                country_dictionary = {'Name': city_list[k], 'Frequency': 1}
                different_country_dictionary_list.append(country_dictionary)
            else:
                for j in range(len(different_country)):
                    if different_country_dictionary_list[j]['Name'] == city_list[k]:
                        different_country_dictionary_list[j]['Frequency'] = different_country_dictionary_list[j]['Frequency'] + 1

    for i in range(len(different_country_dictionary_list)):
        country_code = different_country_dictionary_list[i]['Name']
        try:
            different_country_dictionary_list[i]['Name'] = pycountry.countries.get(alpha_2=country_code).name
        except:
            continue

    name = ['Name', 'Frequency']
    df = pd.DataFrame(columns=name, data=different_country_dictionary_list)  # 数据有三列，列名分别为one,two,three
    df = df.sort_values(by='Frequency', ascending=False)
    dirName = output_dir + "\\" + "Frequency"
    if not os.path.exists(dirName):
        os.makedirs(dirName)
    dirName = dirName + "\\" + "names.csv"
    df.to_csv(dirName,index=False)


f = open(path, encoding='utf-8')
a = f.read()
f.close()
find_most_mentioned_countries(path)