import requests
import json




#basic fish search - you can enter the fish name and it will return the fish's location and times available
#ends with a function to make sure you've finished
# PROBLEM - if the fish is available all day, the function 'finished()' will not run

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
    elif fish['availability']['isAllDay'] == False:
        print('Times available:', fish['availability']['time-array'])


#function with loop to check if user wants to search again
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
