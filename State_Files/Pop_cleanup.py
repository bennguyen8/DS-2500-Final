import pandas as pd


NYC_POP = 8_740_000

def main():

    # Creates a list of names for the population dataset then reads data
    columns = ['state', 'drop1', 'Population', 'drop2', 'drop3',
               'drop4', 'drop5', 'drop6', 'drop7', 'drop8']
    pop_data = pd.read_csv('state_pops.csv', names=columns)

    # Drops the useless columns from the dataset
    pop_data.drop(axis=0, columns=['drop1', 'drop2', 'drop3'
                                   , 'drop4', 'drop5', 'drop6',
                                   'drop7', 'drop8'], inplace=True)
    # Drops any columns with NA values
    pop_data.dropna(inplace=True)
    pop_data.reset_index(drop=True, inplace=True)

    # Removes the periods from the state names
    pop_data = pop_data.iloc[5:]
    pop_data['state'] = list(map(lambda x: x[1:] if x[0]=='.' else x,
                                 pop_data['state']))

    # Removes the commas from the populations
    pop_data['Population'] = list(map(lambda x: int(x.replace(',', '')),
                                 pop_data['Population']))

    # Fixes the NY score so that it doesnt count NYC
    pop_data['Population'] = [value if pop_data['state'].iloc[index]
                              != 'New York' else value - NYC_POP for index,value
                              in enumerate(pop_data['Population'])]

    # Adds NYC to the dataset and then returns it as CSV  
    nyc = ['New York City',  NYC_POP]
    pop_data.loc[len(pop_data.index)] = nyc
    pop_data.reset_index(inplace=True, drop=True)
    pop_data.to_csv('Population_data.csv')

if __name__ == '__main__':
    main()
