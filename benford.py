#!/usr/bin/env python3
import random
import math
from matplotlib import pyplot
import numpy as np
import io

VERBOSE = 0

#param: starting_base lowest base to test the distribution on
#param: ending_base greatest base to test the distribution on
def main(starting_base = 2, ending_base = 16):    
    #Generate datapoints
    datapoints = generate_benford_distribution()

    #for each base desired record the frequency
    frequency_for_each_base = [0] * (ending_base - (starting_base - 1))
    for base in range(starting_base, ending_base + 1): #+1 because range() is exlusive on the final value
        data = analyze_benford_distribution(datapoints,base)
        make_pie(data, base)

    print ("done")

#Starting at START_POINT, successively multiply by a random number between 0.99 and 1.01 NUM_SAMPLES times to produce one datapoint, repeat for each datapoint desired.
#param num_datapoints: size of the generated data set
#param num_samples: Make larger to increase bias towards low first digits
#param start_point: Does not affect distribution, must be larger on high sample counts however
def generate_benford_distribution(num_datapoints = 300, num_samples = 50000, start_point = 10000):
    datapoints = [0] * num_datapoints 
   
    for i in range(num_datapoints):
        value = start_point
        for j in range(num_samples):
            sample = random.uniform(0.99, 1.01)
            value = value * sample
            
            if (value < 1):
                print("The start point selected is too low, and is creating anomalies. Raise start_point or lower num_samples.\nExiting.")
                quit()

        datapoints[i] = math.floor(value)

    #print out the entire dataset
    if (VERBOSE >= 2):
        for i in range(len(datapoints)):
            print(datapoints[i])

    return datapoints

#Determine the leading digit on each datapoint, return the frequencies as a numpy vector and print them in a table if verbose.
def analyze_benford_distribution(datapoints, radix):
    #Determine starting digit
    digit_occurances = [0] * (radix)
    for datum in datapoints:
        magnitude = math.floor(math.log(datum, radix)) #ie the highest exponent the base can be raised to while being lower than the datapoint
        starting_digit = math.floor(datum / (radix ** magnitude))
        digit_occurances[starting_digit] += 1

    if (VERBOSE >= 1):
        print("\nBASE {}:".format(radix))
        print("\nDigit\tOccurances")
        for i in range(radix):
            occurances = digit_occurances[i]
            print("{}:\t{}".format(i, occurances))

    return np.array(digit_occurances)

        

#given a vector of frequency data, make a piechart using matplotlib
def make_pie(data, base, show=False, export=True, file_format="png", explode=True):
    pyplot.close() #otherwise several charts are saved overlapping each other

    explode_vals = [0] * base #does not affect graph unless this array is modified in the if(explode) block
    if (explode):
        explode_vals[1] = 0.1 #Seperate the 1s by 10% the circle radius
        
    labels = range(0, base)
    pie = pyplot.pie(data, labels = labels, explode = explode_vals, autopct= '%1.1f%%')
    pyplot.title("Benford's Law in base {}:".format(base))
   
    if (show):
        pyplot.show()
    if (export):
        pyplot.savefig(fname = "Base_{0}.{1}".format(base, file_format), format=file_format)

if (__name__ == "__main__"):
    main()
