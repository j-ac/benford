import random
import math

NUM_DATAPOINTS = 100    #Size of the generated data set
NUM_SAMPLES = 100000    #Make larger to increase bias towards low first digits.
START_POINT = 10000     #Does not affect distribution, must be larger on high sample counts 
STARTING_BASE = 2       #First base to test the distribution on
ENDING_BASE = 16        #Last base to test the distribution on
VERBOSE = False

#Starting at START_POINT, successively multiply by a random number between 0.99 and 1.01 NUM_SAMPLES times to produce one datapoint, repeat for each datapoint desired.
def generate_benford_distribution(num_datapoints, num_samples):
    datapoints = [0] * num_datapoints 
   
    for i in range(num_datapoints):
        value = START_POINT
        for j in range(num_samples):
            sample = random.uniform(0.99, 1.01)
            value = value * sample
            
            if (value < 1):
                print("The start point selected is too low, and is creating anomalies. Raise START_POINT or lower NUM_SAMPLES.\nExiting.")
                quit()

        datapoints[i] = math.floor(value)

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
        
    
#Generate datapoints
datapoints = generate_benford_distribution(NUM_DATAPOINTS, NUM_SAMPLES)

#for each base desired print out a digit frequency table
for base in range(STARTING_BASE, ENDING_BASE + 1): #+1 because range() is exlusive on the final value
    analyze_benford_distribution(datapoints, base)

