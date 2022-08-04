import json
import requests
#this will allow you to input which hemisphere you are in, the time and date (month only, days do not matter), 
#whether you are searching for fish or bugs or sea life, and then which creature you want. It will return the availability and times.
#This code is not finished
def fish_search(fish_name):
    url_fish = 'https://acnhapi.com/v1/fish/{}'.format(fish_name)
    response_fish = requests.get(url_fish)
    fish = response_fish.json()
    return fish

def bug_search(bug_name):
    url_bug = 'https://acnhapi.com/v1/bugs/{}'.format(bug_name)
    response_bug = requests.get(url_bug)
    bugs = response_bug.json()
    return bugs



def north_fish():
    fish_name = input('fish name')
    choice_month = input('month')
    choice_time = input('time')
    all_fish_data = fish_search(fish_name)
    fish_location = all_fish_data['availability']['location']
    fish_northern_month = all_fish_data['availability']['month-northern']
    fish_northern_time = all_fish_data['availability']['time-array']

    if choice_month in fish_northern_month and all_fish_data['availability']['isAllDay'] == True:
        print('can has today, available now in', fish_location, '\n', 'Shadow size:', all_fish_data['shadow'])
    elif choice_month in fish_northern_month and all_fish_data['availability']['isAllDay'] == False:
        print('fish available today at the following hours:', fish_northern_time, '\n', fish_location, 'Shadow size:', all_fish_data['shadow'])
    elif choice_month not in fish_northern_month:
        print('you cannot fish him now! This fishie is available during the following months:', fish_northern_month)


    # function with for loop to check if user wants to search again
    def finished():
        are_you_finished = input('Are you done? yes/no')
        if are_you_finished == 'no':
            run()
        elif are_you_finished == 'yes':
            print('thanks! Happy fishing!')
        else:
            print('That made no sense, try again')
            finished()

    finished()

def south_fish():
    fish_name = input('fish name')
    choice_month = input('month')
    choice_time = input('time')
    all_fish_data = fish_search(fish_name)
    fish_location = all_fish_data['availability']['location']
    fish_southern_month = all_fish_data['availability']['month-southern']
    fish_southern_time = all_fish_data['availability']['time-array']

    if choice_month in fish_southern_month and all_fish_data['availability']['isAllDay'] == True:
        print('can has today, available now in', fish_location, '\n', 'Shadow size:', all_fish_data['shadow'])
    elif choice_month in fish_southern_month and all_fish_data['availability']['isAllDay'] == False:
        print('fish available today at the following hours:', fish_southern_time, '\n', fish_location, 'Shadow size:', all_fish_data['shadow'])
    elif choice_month not in fish_southern_month:
        print('you cannot fish him now! This fishie is available during the following months:', fish_southern_month)
    else:
        print('oops I did not factor in for this outcome')

    # function with for loop to check if user wants to search again
    def finished():
        are_you_finished = input('Are you done? yes/no')
        if are_you_finished == 'no':
            run()
        elif are_you_finished == 'yes':
            print('thanks! Happy fishing!')
        else:
            print('That made no sense, try again')
            finished()

    finished()

def north_bugs():
    bug_name = input('bug name')
    choice_month = input('month')
    choice_time = input('time')
    all_bug_data = bug_search(bug_name)
    bug_location = all_bug_data['availability']['location']
    bug_northern_month = all_bug_data['availability']['month-northern']
    bug_northern_time = all_bug_data['availability']['time-array']

    if choice_month in bug_northern_month and all_bug_data['availability']['isAllDay'] == True:
        print('can has today, available now in', bug_location, '\n')
    elif choice_month in bug_northern_month and all_bug_data['availability']['isAllDay'] == False:
        print('fish available today at the following hours:', bug_northern_time, '\n')
    elif choice_month not in bug_northern_month:
        print('you cannot fish him now! This fishie is available during the following months:', bug_northern_month)


    # function with for loop to check if user wants to search again
    def finished():
        are_you_finished = input('Are you done? yes/no')
        if are_you_finished == 'no':
            run()
        elif are_you_finished == 'yes':
            print('thanks! Happy fishing!')
        else:
            print('That made no sense, try again')
            finished()

    finished()

# def north_bugs()
#     bug_name = input('bug name')
#     choice_month = input('month')
#     choice_time = input('time')
#     all_bug_data = bug_search(bug_name)
#     bug_location = all_bug_data['availability']['location']


def run():
    choice_hemisphere = input('Which hemisphere please enter as north/south')
    choice_creatures = input('which creatures type[please enter as: fish/bugs/sea]')
    if choice_hemisphere == "north" and choice_creatures == 'fish':
        north_fish()
    if choice_hemisphere == 'north' and choice_creatures == 'sea':
        print("north sea")
    if choice_hemisphere == 'north' and choice_creatures == 'bugs':
        north_bugs()

        #southern hemisphere
    if choice_hemisphere == "south" and choice_creatures == 'fish':
        south_fish()
    if choice_hemisphere == 'north' and choice_creatures == 'sea':
        print("north sea")
    if choice_hemisphere == 'north' and choice_creatures == 'bugs':
        print("north bugs")


run()




    #print(response_fish.status_code)
    #function for northern hemisphere search - if user hemisphere is north, nhem(), then inside that
    #you need a function to search for the fish data
    #fish_name = input('fish')
    #user_month = input('month')
    #user_time = input('time')
    #fish_location = all_fish_data['availability']['location']
    #fish_northern_month = all_fish_data['availability']['month-northern']
    #fish_northern_time = all_fish_data['availability']['time-array']
    #if user_month in fish_northern_month and all_fish_data['availability']['isAllDay'] == True:
        #print('can has today, available now in', fish_location, 'Shadow size:', all_fish_data['shadow'])
    #elif user_month in fish_northern_month and user_time in fish_northern_time:
        #print('can has today, available now in', fish_location, 'Shadow size:', all_fish_data['shadow'])
    #else:
        #print(fish_northern_month, fish_location, fish_northern_time, 'Shadow size:', all_fish_data['shadow'])
