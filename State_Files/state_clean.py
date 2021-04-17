from state_functions import *



def main():

    # Reads in the State dataset and does basic clean up and sorting
    state_df = pd.read_csv('state_info.csv')
    state_df['submission_date'] = pd.to_datetime(state_df['submission_date'])
    state_df = state_df.sort_values(by=['state', 'submission_date'],
                          ignore_index=True)
    state_df.fillna(value=0, inplace=True)
    state_df.rename(columns={'consent_deaths':'consent_death'},
                    inplace=True)

    # Reads in the population dataset
    pop_df = pd.read_csv('Population_data.csv', usecols=['state', 'Population'])

    # Uses the state dict to reassign state names to abbreviations
    score_lst = []
    pop_df['state'] = list(map(lambda x:  us_states[x], pop_df['state']))

    cases = []
    deaths = []
    
    # Fix the consent cases and deaths
    for i in range(len(state_df)):
        row = state_df.iloc[i]

        cases.append(fix_consent('cases', row))
        deaths.append(fix_consent('death', row))

    state_df['cases'] = cases
    state_df['deaths'] = deaths

    # Finds rows that are not found in the Population DF
    drop_lst = []
    valid_states = pop_df['state'].unique()
    drop_lst = [index for index,state in enumerate(state_df['state'])
                if state not in valid_states]

    # Drops the rows that were found above
    state_df.drop(axis=0, inplace=True, labels=drop_lst)
    state_df.reset_index(inplace=True)

    # Gets the cases and Deaths for each place
    state_scores = {}
    for value in valid_states:

        state_subset = state_df.loc[state_df['state'] == value]
        pop = pop_df.loc[pop_df['state'] == value]['Population'].iloc[0]

        death_score = count_stats(state_subset, 'tot_death')
        case_score = count_stats(state_subset, 'tot_cases')

        final_score = death_score + (case_score * .01)

        # Finds the percent of population affected in each state
        percent_death = final_score/pop
        state_scores[value] = percent_death

    # Sorts the keys based on the score found above
    sorted_keys = sorted(state_scores, key=state_scores.get)
    states = [state for state in sorted_keys]
    values = [state_scores[key] for key in sorted_keys]

    # Scales the values into a new range and saves them in a list
    values = scale_values(values)
    final_scores = list(zip(states, values))

    # Generates the shuffled list of states based on actual populations
    total_pop = sum(pop_df['Population'])
    pop_percents = {state:
                    pop_percent(total_pop, pop_df.iloc[index])
                    for index,state in enumerate(pop_df['state'])}
    random_lst = generate_states(pop_percents, COUNT)

    # Questionnaire for the User to fill out
    personal_info = menu(final_scores, SHOW)

    # Creates a bar chart of the data found above
    xlabel = 'States'
    ylabel = 'Risk Score'
    title = 'Covid Risk of Each State'

    if SHOW:
        draw_bar(title, ylabel, xlabel, final_scores)

    


if __name__ == '__main__':
    main()





