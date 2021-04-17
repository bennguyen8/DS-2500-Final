from sklearn.preprocessing import MinMaxScaler
import random
import pandas as pd
import matplotlib.pyplot as plt
from statistics import mode
COUNT = 1000
SHOW = False

# Dictionary to map states to their abbreviations
us_states = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'American Samoa': 'AS',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Guam': 'GU',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'New York City': 'NYC',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}

def fix_consent(column, row):
    '''
    param: column(string), row(series)
    return: float
    Does: Corrents records that improperly store the total deaths and cases
    '''

    # Generates the proper column names to use for conditional
    consent = f'consent_{column}'
    total = f'tot_{column}'
    prob = f'prob_{column}'

    # Checks to see if row is stored improperly and then corrects it
    if row[consent] == 'Agree':
        return row[total] - row[prob]

    else:
        return row[total]

    
def count_stats(subset, stat):
    '''
    param: subset(dataframe), stat(string)
    return: stat_count(float)
    Does: Gets the proper stat measurment from the df subset 
    '''

    # Finds last entry in subset and then calculates relevant stat
    stat_count = subset[stat].iloc[-1]
    stat_count = round(stat_count/len(subset), 2)

    return stat_count


def scale_values(values, scaler=MinMaxScaler):
    '''
    param: values(list), scaler(function)
    return: list
    Does: Scales the values according to the scaling function passed
    '''

    # Prepares the scaler passed along with data
    values = list(map(lambda x: [x], values))
    scaler = scaler(feature_range=(0,100))

    # Scales the data and then returns it
    scaler.fit(values)
    values = scaler.transform(values)
    return [value[0] for value in values]


def pop_percent(total, state_pop):
    '''
    param: total(int), state_pop(int)
    return: percent
    Does: Finds the percentage of the country that a state accounts for and
    then returns it
    '''

    # Finds the percent of population for state that was passed
    state_population = state_pop['Population']
    percent = state_population/total

    return percent


def generate_states(percents, count):
    '''
    param: percents(dict), count(int)
    return: random_lst(list)
    Does: Creates a shuffled list of US states based on actual population
    distribution
    '''

    # Iterates through the list of percents generated before
    random_lst = []
    for key, value in percents.items():
        iterate = int(round(count * value))

    # Adds states to list relative to its total percent
        for num in range(iterate):
            random_lst.append(key)

    # Adjusts list size for rounding errors
    most_common = mode(random_lst)
    while len(random_lst) < count:
        random_lst.append(most_common)

    # Shuffles the list and then returns it
    random.shuffle(random_lst)
    return random_lst


def menu(final_scores, show):
    '''
    param: final_scores(list), show(Bool)
    return: personal_info(tuple)
    Does: Prompts user for info and then returns it in a tuple
    '''
   
    if show:

        # Prints out the possible inputs
        states = [state for state,score in final_scores]
        for number,value in enumerate(states, 1):
            print(f'{number}:{value}')

        # Prompts user for their howe state
        state_idx = int(input('Enter the number that corresponds'
                              'to your home state using the list above.\n'))

        # Checks to make sure the input is valid and then loops until True
        while state_idx not in range(1, len(states)+1):
            state_idx = int(input('Please enter a valid number'
                                  ' from the list above.\n'))

        # Returns the response to the question above 
        personal_info = final_scores[state_idx-1]
        return personal_info
            

def draw_bar(title, xlabel, ylabel, data):
    '''
    param: title(string), xlabel(string), y_label(string), data(list)
    return: N/A
    Does: Uses the data passed to draw a bar chart
    '''

    # Creates data for the bar chart
    x = [tup[0] for tup in data]
    y = [tup[1] for tup in data]

    # Creates bar chart        
    plt.bar(x=x, height=y, color='coral')

    # Adds proper labels to the bar chart and then shows it
    plt.xticks(label=xlabel, rotation=270)
    plt.ylabel(ylabel=ylabel)
    plt.title(title)
    plt.show()









