def fish_search(fish_name):
    url_fish = 'https://acnhapi.com/v1/fish/{}'.format(fish_name)
    response_fish = requests.get(url_fish)
    fish = response_fish.json()
    return fish

print(fish['name'])
