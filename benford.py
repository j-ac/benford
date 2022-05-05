import random
import math
import pdb

NUM_DATAPOINTS = 50
NUM_SAMPLES = 100000
START_POINT = 10000
STARTING_BASE = 2
ENDING_BASE = 16
IS_PRINTNG_DATAPOINTS = False

def generate_benford_distribution(num_datapoints, num_samples):
    datapoints = [0] * num_datapoints 
    
    for i in range(num_datapoints):
        value = START_POINT
        for j in range(num_samples):
            sample = random.uniform(0.99, 1.01)
            value = value * sample
            
        datapoints[i] = math.floor(value)

    if (IS_PRINTNG_DATAPOINTS) :
        for i in range(len(datapoints)):
            print(datapoints[i])

    return datapoints

def analyze_benford_distribution(datapoints, radix):
    #Determine starting digit
    digit_occurances = [0] * (radix)
    for datum in datapoints:
        magnitude = math.floor(math.log(datum, radix)) #ie the highest exponent the base can be raised to while being lower than the datapoint
        starting_digit = math.floor(datum / (radix ** magnitude))
        if (starting_digit >= radix):
            pdb.set_trace()
        digit_occurances[starting_digit] += 1


    print("\nBASE {}:".format(radix))
    print("\nDigit\tOccurances")
    for i in range(radix):
        occurances = digit_occurances[i]
        print("{}:\t{}".format(i, occurances))
        
    

datapoints = generate_benford_distribution(NUM_DATAPOINTS, NUM_SAMPLES)
for base in range(STARTING_BASE, ENDING_BASE + 1): #range() is exlusive on the final value
    analyze_benford_distribution(datapoints, base)

