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

sum_lst.remove(sum_lst[-1]) 
conditions = df['Condition'].unique() # will not include all COVID-19
conditions = conditions.tolist()
conditions.remove('COVID-19') # value representing everyone who contracted COVID-19

# value associated with each comorbidity
all_covid = 468643 # number of all COVID-19 deaths according to DataFrame
condition_values = [(round(i / all_covid, 2)) * 100 for i in sum_lst]

# dictionary with comorbidites and values
condition_dict = dict(zip(conditions, condition_values))


def comorbidities(list, dict):
    '''Gives score for comorbidity section for vaccine distribution'''
    
    print(list)
    choice = input('Do you have a condition on this list? (y or n)\n')

    if choice.lower() == 'y':
        comorbidity = input('Which one?\n')
        score = dict[comorbidity]
        return score
    elif choice.lower() == 'n':
        score = 0
        return score
