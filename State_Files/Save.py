# SAVE FOR LATER #



    x_lab = 'Location Abbreviation'
    y_lab = 'Number of Deaths'
    title = 'Average Confirmed Deaths Per Location Per Day'


    plt.bar(states, values, color='coral')
    plt.xticks(rotation=270)
    plt.xlabel(x_lab)
    plt.ylabel(y_lab)
    plt.title(title)
    plt.show()



        # print(state_df.iloc['state'])
        # score += state_df['tot_cases'].iloc[i] * 1.5
        # score += state_df['prob_cases'].iloc[i] * 0.5
        #
        # score += state_df['tot_death'].iloc[i] * 2.0
        # score += state_df['prob_death'].iloc[i] * 1.0

        # score_lst.append([score])

    # print(score_lst)
    # scalar = MinMaxScaler(feature_range=(0, 1))
    # scalar.fit(score_lst)
    # scaled_data = scalar.transform(score_lst)
    # state_df['scaled_data'] = scaled_data
    #
