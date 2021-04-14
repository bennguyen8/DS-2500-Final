import pandas as pd
import matplotlib.pyplot as plt
from state_functions import *
from sklearn.preprocessing import MinMaxScaler


count = 100

def main():

    state_df = pd.read_csv('state_info.csv')
    state_df['submission_date'] = pd.to_datetime(state_df['submission_date'])
    state_df = state_df.sort_values(by=['state', 'submission_date'],
                          ignore_index=True)
    state_df.fillna(value=0, inplace=True)

    pop_df = pd.read_csv('Population_data.csv', usecols=['state', 'July'])

    score_lst = []
    pop_df['state'] = list(map(lambda x:  us_states[x], pop_df['state']))

    cases = []
    deaths = []
    
    # Fix the consent cases and deaths
    for i in range(len(state_df)):
         score = 0
        
         if state_df['consent_cases'].iloc[i] == 'Agree':
             cases.append(fix_consent('cases', state_df.iloc[i]))
         else:
             cases.append(state_df['tot_cases'].iloc[i])
             
        
         if state_df['consent_deaths'].iloc[i] == 'Agree':
             deaths.append(fix_consent('death', state_df.iloc[i]))
         else:
             deaths.append(state_df['tot_death'].iloc[i])


    state_df['cases'] = cases
    state_df['deaths'] = deaths

    # Drops rows that are not gound in the Population DF
    drop_lst = []
    valid_states = pop_df['state'].unique()
    for i in range(len(state_df)):
        row = state_df.iloc[i]

        if row['state'] not in valid_states:
            drop_lst.append(i)

    state_df.drop(axis=0, inplace=True, labels=drop_lst)
    state_df.reset_index(inplace=True)


    # Gets the cases and Deaths for each place
    state_lst = state_df['state'].unique()
    state_scores = {}
    
    for value in state_lst:

        state_subset = state_df.loc[state_df['state'] == value]
        pop = pop_df.loc[pop_df['state'] == value]['July'].iloc[0]
        
        
        death_count = sum(state_subset['new_death'])
        death_count = round(death_count/len(state_subset), 2)

        percent_death = death_count/pop
        state_scores[value] = percent_death

    sorted_keys = sorted(state_scores, key=state_scores.get)
    states = []
    values = []
    for key in sorted_keys:
        states.append(key)
        values.append(state_scores[key])

    values = list(map(lambda x: [x], values))
    scaler = MinMaxScaler(feature_range=(0,100))
    scaler.fit(values)
    values = scaler.transform(values)

    final_scores = list(zip(states, values))

    for number,value in enumerate(states, 1):
        print(f'{number}:{value}')


    state_idx = int(input('Enter the number that corresponds'
                          'to your home state using the list above.\n'))
    
    while state_idx not in range(1, len(states)+1):
        state_idx = int(input('Please enter a valid number'
                              ' from the list above.\n'))

    
    personal_info = final_scores[state_idx-1]
    state = personal_info[0]
    score = personal_info[1]

    print(state, score)
    


    
    
                          
    













if __name__ == '__main__':
    main()





