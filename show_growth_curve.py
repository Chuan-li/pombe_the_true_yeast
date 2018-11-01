def show_growth_curve(strain_a, strain_b, media, number_of_replicate):

    import matplotlib.pyplot as plt
    import pandas as pd

    turbi_run = 'y' + str(strain_a) + '_' + 'y' + str(strain_b) + '_' + media + '_' + str(number_of_replicate)
    print(turbi_run)
    # import csv file
    file_name = '/Users/kikawaryoku/OneDrive - Imperial College London' \
                '/Fitness&size/Estradiol_week1_turbis/' + turbi_run + '/data.csv'
    data = pd.read_csv(file_name)
    # subtract time
    epoch_time = data.abs_time_s
    # convert epoch time to human time
    human_time = (epoch_time - data.abs_time_s[0]) / 3600
    # subtract OD
    od = data['OD']
    # plot
    plt.plot(human_time, od)
    plt.ylabel('OD')
    plt.xlabel('Time (h)')
    plt.title(turbi_run)
    plt.show()
