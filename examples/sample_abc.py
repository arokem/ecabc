'''
Simple sample script to demonstrate how to use the artificial bee colony, this script is a simple example, which is just
used to demonstrate how the program works.

If an ideal day is 70 degrees, with 37.5% humidity. The fitness functions takes four values and tests how 'ideal' they are.
The first two values input will be added to see how hot the day is, and the second two values will be multiplied to see how much
humidity there is. The resulting values will be compared to 70 degrees, and 37.5% humidity to determine how ideal the day those 
values produce is. 

The goal is to have the first two values added up to as close to 70 as possible, while the second two values multiply out to as 
close to 37.5 as possible.
'''

from ecabc.abc import *
import os
import time

def idealDayTest(values, args=None):  # Fitness function that will be passed to the abc
    temperature = values[0] + values[1]       # Calcuate the day's temperature
    humidity = values[2] * values[3]          # Calculate the day's humidity
    
    cost_temperature = abs(70 - temperature)  # Check how close the daily temperature to 70
    cost_humidity = abs(37.5 - humidity)      # Check how close the humidity is to 37.5

    return cost_temperature + cost_humidity   # This will be the cost of your fitness function generated by the values

         # First value      # Second Value     # Third Value      # Fourth Value

if __name__ == '__main__':
    values = [('int', (0,100)), ('int', (0,100)), ('float',(0,100)), ('float', (0, 100))]

    start = time.time()
    abc = ABC(fitness_fxn=idealDayTest, 
            value_ranges=values
            )
    abc.create_employers()
    while True:
        abc.save_settings('{}/settings.json'.format(os.getcwd()))
        abc.calc_average()
        if (getattr(abc, 'best_performer')[0] < 2):
            break
        abc.calc_new_positions()
        abc.check_positions()
    print("execution time = {}".format(time.time() - start))
