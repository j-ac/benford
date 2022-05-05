#!/usr/bin/env python3
import random
import math

VERBOSE = False

#param: starting_base lowest base to test the distribution on
#param: ending_base greatest base to test the distribution on
def main(starting_base = 2, ending_base = 16):    
    #Generate datapoints
    datapoints = generate_benford_distribution()

    #for each base desired print out a digit frequency table
    for base in range(starting_base, ending_base + 1): #+1 because range() is exlusive on the final value
        analyze_benford_distribution(datapoints, base)

#Starting at START_POINT, successively multiply by a random number between 0.99 and 1.01 NUM_SAMPLES times to produce one datapoint, repeat for each datapoint desired.
#param num_datapoints: size of the generated data set
#param num_samples: Make larger to increase bias towards low first digits
#param start_point: Does not affect distribution, must be larger on high sample counts however
def generate_benford_distribution(num_datapoints = 100, num_samples = 100000, start_point = 10000):
    datapoints = [0] * num_datapoints 
   
    for i in range(num_datapoints):
        value = start_point
        for j in range(num_samples):
            sample = random.uniform(0.99, 1.01)
            value = value * sample
            
            if (value < 1):
                print("The start point selected is too low, and is creating anomalies. Raise START_POINT or lower NUM_SAMPLES.\nExiting.")
                quit()

        datapoints[i] = math.floor(value)

    #print out the entire dataset
    if (VERBOSE) :
        for i in range(len(datapoints)):
            print(datapoints[i])

    return datapoints

#Determine the leading digit on each datapoint, and print the frequencies in a table.
def analyze_benford_distribution(datapoints, radix):
    #Determine starting digit
    digit_occurances = [0] * (radix)
    for datum in datapoints:
        magnitude = math.floor(math.log(datum, radix)) #ie the highest exponent the base can be raised to while being lower than the datapoint
        starting_digit = math.floor(datum / (radix ** magnitude))
        digit_occurances[starting_digit] += 1


    print("\nBASE {}:".format(radix))
    print("\nDigit\tOccurances")
    for i in range(radix):
        occurances = digit_occurances[i]
        print("{}:\t{}".format(i, occurances))
        

if (__name__ == "__main__"):
    main()
