import pandas as pd
from sklearn.preprocessing import MinMaxScaler





count = 100

def main():

    state_df = pd.read_csv(r'/Users/bongo/Documents/Ds 2500/'
                    r'2500_project/state_info.csv')
    state_df['submission_date'] = pd.to_datetime(state_df['submission_date'])
    state_df = state_df.sort_values(by=['state', 'submission_date'],
                          ignore_index=True)
    state_df.fillna(value=0, inplace=True)

    score_lst = []

    # Fix the consent cases and deaths
    for i in range(len(state_df)):
        score = 0

        if state_df['consent_cases'].iloc[i] == 'Agree':
            state_df['tot_cases'].iloc[i] -= state_df['prob_cases'].iloc[i]

        if state_df['consent_deaths'].iloc[i] == 'Agree':
            state_df['tot_death'].iloc[i] -= state_df['prob_death'].iloc[i]


        score += state_df['tot_cases'].iloc[i] * 1.5
        score += state_df['prob_cases'].iloc[i] * 0.5

        score += state_df['tot_death'].iloc[i] * 2.0
        score += state_df['prob_death'].iloc[i] * 1.0

        score_lst.append([score])


    scalar = MinMaxScaler(feature_range=(0, 1))
    scalar.fit(score_lst)
    scaled_data = scalar.transform(score_lst)
    state_df['scaled_data'] = scaled_data

    state_lst = state_df['state'].unique()
    state_scores = {}

    for value in state_lst:

        subset = state_df.loc[state_df['state'] == value].head(count)
        avg_score = subset['scaled_data'].mean()
        state_scores[value] = avg_score


















if __name__ == '__main__':
    main()





