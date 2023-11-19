import requests
from decorator1 import logger


url = 'https://akabab.github.io/superhero-api/api/all.json'
# names_of_characters = [{'name': 'Hulk'}, {'name': 'Captain America'}, {'name': 'Thanos'}]
response = requests.get(url)


@logger
def smart_hero(smart_hero_list, top_amt=1):
    hero_list = []
    counter = 0
    for hero_dict in response.json():
        name = hero_dict.get('name')
        if name == smart_hero_list[counter] and counter < len(smart_hero_list):
            powerstats = hero_dict.get('powerstats')
            intelligence = powerstats.get('intelligence')
            hero_list.append([name, intelligence])
            counter += 1
        else:
            continue
        
    hero_list.sort(key=lambda x:x[1], reverse=True)
    top_amt = hero_list[0:top_amt]
    str_top_amt = []
    for i in top_amt:
        str_top_amt.append(i[0])
    
    return f'Самый умный супергерой: {str_top_amt[0]}'
    # return hero_list

if __name__ == '__main__':
    print(smart_hero(['Hulk', 'Captain America', 'Thanos']))
