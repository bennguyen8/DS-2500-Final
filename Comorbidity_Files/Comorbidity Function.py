import pandas as pd

def comorbidities():
     '''Gives score for comorbidity section for vaccine distribution'''
    df = pd.read_csv('Conditions_contributing_to_deaths_involving_coronavirus_disease_2019__COVID-19___by_age_group_and_state__United_States..csv')
    
    df = df[['Group','Condition','COVID-19 Deaths', 'Age Group', 'State']]
    df = df[df['Group'] == 'By Total']
    df = df.dropna()
    condition_lst = df['Condition'].unique()
    sum_lst = []

    for condition in condition_lst:
    
        subset = df[(df['Condition'] == condition) & (df['Age Group'] == 'All Ages') & (df['State'] == 'United States')]
        subset['COVID-19 Deaths'] = list(map(lambda x: int(x.replace(',', '')), subset['COVID-19 Deaths']))
        death_sum = subset['COVID-19 Deaths'].sum()
        
        sum_lst.append(death_sum)
    sum_lst.remove(sum_lst[-1]) # last element = all COVID-19 deaths (not needed)
    
    conditions = df['Condition'].unique() # will not include all COVID-19
    conditions = conditions.tolist()
    conditions.remove('COVID-19') # value representing everyone who contracted COVID-19
    
    # value associated with each comorbidity
    condition_values = [100, 20, 25, 80, 5, 10, 40, 25, 30, 20, 20, 15, 17.5, 10, 12.5, 25, 10, 35, 10, 10, 25, 20] 
    # dictionary with comorbidites and values
    condition_dict = dict(zip(conditions, condition_values))
    
    print(conditions)
    choice = input('Do you have a condition on this list? (y or n)\n')

    if choice.lower() == 'y':
        comorbidity = input('Which one?\n')
        score = condition_dict[comorbidity]
        print(score)
    elif choice.lower() == 'n':
        score = 0
        print(score)
        
comorbidities()