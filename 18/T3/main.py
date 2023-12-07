import json
import time

import requests

def get_swapi_data(url):
    response = requests.get(url)
    return json.loads(response.text)

def get_pilot_info(pilot_url):
    pilot_data = get_swapi_data(pilot_url)
    return {key: pilot_data[key] for key in ['name', 'height', 'homeworld', 'mass']}

def main():
    start_time = time.time()

    starship_url = 'https://swapi.dev/api/starships/10'
    starship_data = get_swapi_data(starship_url)

    filtered_keys = ['max_atmosphering_speed', 'pilots', 'name', 'starship_class']
    starship_info = {key: starship_data[key] for key in filtered_keys}
    starship_info['ship_name'] = starship_info.pop('name')

    pilots_info = [dict(sorted(get_pilot_info(pilot_url).items())) for pilot_url in starship_info['pilots']]
    for pilot in pilots_info:
        pilot['homeworld_url'] = pilot.pop('homeworld')
        pilot['homeworld'] = get_swapi_data(pilot['homeworld_url'])['name']

    starship_info['pilots'] = pilots_info

    with open('data.json', 'w') as file:
        json.dump(starship_info, file, indent=4)

    print(starship_info)
    print(time.time() - start_time)

if __name__ == "__main__":
    main()
