from geotext import GeoText
import pandas as pd
import pycountry
import pycountry_convert as pc


def find_cities_countries_continent(text):
    city_list = []
    country_list = []
    continent_list = []
    places = GeoText(text)
    places.cities = list(set(places.cities))
    city_list.append(",".join(str(x) for x in places.cities))
    print(city_list)
    for i in range(len(city_list)):
        city_list[i] = str(city_list[i]).replace(',', ' ')
    cities = " ".join(str(i) for i in city_list)
    city_list = cities.split(" ")
    print(city_list)
    city_list = (", ".join(str(i) for i in city_list))
    print(city_list)
    if len(places.cities) != 0:
        # print(places.cities)
        for key in places.country_mentions.keys():
            country = pycountry.countries.get(alpha_2=key)
            try:
                continent = country_to_continent(country.alpha_2)
            except:
                continue
            country_list.append(country.name)
            continent_list.append(continent)
    continent_list = list(set(continent_list))
    return city_list, country_list, continent_list


def country_to_continent(country_alpha2):
    country_continent_code = pc.country_alpha2_to_continent_code(country_alpha2)
    country_continent_nam = pc.convert_continent_code_to_continent_name(country_continent_code)
    return country_continent_nam

new_inventory = pd.read_csv(r"F:\Edin\1_2\Design with Data\Project\HumanName\inventory_name.csv", encoding='utf-8', index_col=0, parse_dates=True)
new_inventory['cities'] = None
new_inventory['countries'] = None
new_inventory['continent'] = None


for ni_index, ni_row in new_inventory.iterrows():
    if ni_row.cities == 0:
        pass
    else:
        file_name = str(ni_row.name)
        file_path = r"F:\Edin\1_2\Design with Data\Data\nls-text-broadsides\nls-text-broadsides" + "\\" +  file_name + ".txt"
        with open(file_path, 'r', encoding='UTF-8') as f:
            text = f.read()
        ni_row['cities'], ni_row['countries'], ni_row['continent'] = find_cities_countries_continent(text)


new_inventory.to_csv(r"F:\Edin\1_2\Design with Data\Project\geographical_location\inventory_name_place.csv")