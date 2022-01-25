"""
Indigo Dockery
lab2.py
Solving for RMS, Harmonic Mean, and Geometric Mean
"""


def means():
    num_values = eval(input("Enter the number of values to be input: "))
    rms_accum = 0
    harm_accum = 0
    geo_counter = 1
    for i in range(num_values):
        val = eval(input("Enter Value: "))
        rms_accum = rms_accum + (val ** 2)
        harm_accum = harm_accum + 1 / val
        geo_counter = geo_counter * val
    rms = (rms_accum / num_values) ** (1/2)
    harm_mean = num_values / harm_accum
    geo_mean = geo_counter ** (1 / num_values)
    print("The RMS Average is:", rms)
    print("The Harmonic Mean is:", harm_mean)
    print("The Geometric Mean is:", geo_mean)

means()