def show_growth_rate(strain_a, strain_b, media, number_of_replicate):

    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np

    turbi_run = 'y' + str(strain_a) + '_' + 'y' + str(strain_b) + '_' + media + '_' + str(number_of_replicate)
    file_name = '/Users/kikawaryoku/OneDrive - Imperial College London' \
                '/Fitness&size/Estradiol_week1_turbis/' + turbi_run + '/data.csv'
    # import csv file
    data = pd.read_csv(file_name)
    # subtract useful information
    info = data[['abs_time_s', 'OD', 'has_opened']]
    # find and store time points after valve open
    open_time = []
    for i, row in info.iterrows():
        if row.has_opened == 1:
            open_time.append(i + 1)

    parameters = []
    for i in range(len(open_time) - 1):
        # iterate segment
        segment = info.iloc[open_time[i]:open_time[i + 1]]
        # calculate growth rate from each segment that has more than one time point
        if len(segment) > 1:
            t0 = segment.abs_time_s.iloc[0]
            parameter = np.polyfit((segment.abs_time_s - t0) / 3600, np.log(segment.OD), 1)
            parameters.append(parameter[0])
            # iterative plotting
            plt.plot(i, parameter[0], marker=".")
    # calculate average growth rate
    average_growth_rate = sum(parameters) / len(parameters)
    print(average_growth_rate)
    # plotting
    plt.ylabel('Growth rate')
    plt.title(turbi_run)
    plt.show()
