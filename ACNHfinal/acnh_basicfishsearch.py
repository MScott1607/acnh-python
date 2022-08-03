import requests
import json

def fish_search(fish_name):
    url_fish = 'https://acnhapi.com/v1/fish/{}'.format(fish_name)
    response_fish = requests.get(url_fish)
    fish = response_fish.json()
    return fish


def run():
    fish_name = input('name')
    fish=fish_search(fish_name)
    print(fish['name']['name-EUen'], 'Availability:', fish['availability']['location'])
    #less messy if fish is available all day
    if fish['availability']['isAllDay'] == True:
        print('Time: All Day')
    else:
        print('Times available:', fish['availability']['time-array'])

#function with for loop to check if user wants to search again
        def finished():
            are_you_finished=input('Are you done? yes/no')
            if are_you_finished=='no':
                run()
            elif are_you_finished=='yes':
                print('thanks! Happy fishing!')
            else:
                print('That made no sense, try again')
                finished()
        finished()
run()