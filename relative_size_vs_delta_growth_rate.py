import pandas as pd
import matplotlib.pyplot as plt
all_growth_rate = pd.read_csv('/Users/kikawaryoku/Desktop/pairwise-competition-turbi-master 2/output-data/all-delta-growth-rates.csv')
all_cell_size = pd.read_csv('/Users/kikawaryoku/Desktop/pairwise-competition-turbi-master 2/output-data/all-division-sizes.csv')

all_cell_size["mean_difference"] = all_cell_size.mean_sept_vol_um3_strain_B / all_cell_size.mean_sept_vol_um3_strain_A
all_cell_size["unique_column"] = all_cell_size.strain_A.astype(str) + all_cell_size.strain_B.astype(str)


strain_B_min = 242
strain_B_max = 256

target_strain_B = range(strain_B_min + 1, strain_B_max + 1)
target_selector = all_cell_size.strain_B.isin(target_strain_B)
restriction = all_cell_size.mean_sept_width_um_strain_B > 0

selector = target_selector & restriction
selection = all_cell_size[selector]
relative_sizes = selection.mean_difference
delta_growth_rates = all_growth_rate.iloc[selection.index].delta_growth_rate_per_hr_A_minus_B * -1


for unique_col in selection['unique_column'].unique():
    sub_rel = selection[selection.unique_column == unique_col].mean_difference
    sub_del = all_growth_rate[selector][selection.unique_column == unique_col].delta_growth_rate_per_hr_A_minus_B * -1
    print(unique_col, len(sub_rel))
    plt.plot(sub_rel, sub_del, "o")

plt.show()

