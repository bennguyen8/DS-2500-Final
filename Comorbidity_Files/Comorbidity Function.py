comor_df = pd.read_csv('Conditions_contributing_to_deaths_involving_coronavirus_disease_2019__COVID-19___by_age_group_and_state__United_States..csv')
    
comor_df = comor_df[['Group','Condition','COVID-19 Deaths', 'Age Group', 'State']]
comor_df = comor_df[comor_df['Group'] == 'By Total']
comor_df = comor_df.dropna()
condition_lst = comor_df['Condition'].unique()
sum_lst = []

for condition in condition_lst:
    
    subset = comor_df[(comor_df['Condition'] == condition) & (comor_df['Age Group'] == 'All Ages') & (comor_df['State'] == 'United States')]
    subset['COVID-19 Deaths'] = list(map(lambda x: int(x.replace(',', '')), subset['COVID-19 Deaths']))
    death_sum = subset['COVID-19 Deaths'].sum()
        
    sum_lst.append(death_sum)

conditions = comor_df['Condition'].unique() # will be different from condition_lst
conditions = conditions.tolist()
conditions.remove('COVID-19')

all_covid = sum_lst[-1]
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
