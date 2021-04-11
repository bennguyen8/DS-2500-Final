import pandas as pd




def main():
    
    columns = ['state', 'August', 'July', 'Num', 'Per', 'Rank', 'drop',
               'change', 'ds', 'None']
    pop_data = pd.read_csv('state_pops.csv', names=columns)

    pop_data.drop(axis=0, columns=['August', 'Num', 'Per', 'Rank', 'drop',
                                   'change', 'ds', 'None'],
                  inplace=True)
    pop_data.dropna(inplace=True)
    pop_data.reset_index(drop=True, inplace=True)
    

    pop_data = pop_data.iloc[5:]
    pop_data['state'] = list(map(lambda x: x[1:] if x[0]=='.' else x,
                                 pop_data['state']))


    pop_data.to_csv('Population_data.csv')
    



if __name__ == '__main__':
    main()
