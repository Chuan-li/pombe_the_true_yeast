def c1_volume_calculator(growth_rate, c2_growth_time_hr, c2_volume_ml, c2_objective_od, c1_od):
    import math
    c2_initial_od = c2_objective_od / (math.exp(growth_rate * c2_growth_time_hr) / 2)
    volume_from_c1 = c2_initial_od * c2_volume_ml / c1_od
    print('\nYou need to add ' + str(round(volume_from_c1, 5) * 1000) + ' ul from C1 at OD ' + str(c1_od) + '.')
    print('\nYour ' + str(c2_volume_ml) + ' ml C2 will grow from OD ' + str(round(c2_initial_od, 2)) + ' to OD ' + str(c2_objective_od) + ' in ' + str(c2_growth_time_hr) + 'h.')

c1_volume_calculator(0.26, 17, 10, 0.5, 6.93)


