

import random

# Generate a random heart rate value between 60 and 100 bpm

heart_rate = random.randint(60, 100)



# Print the generated heart rate value

print("Heart rate: {} bpm".format(heart_rate))


import random

import matplotlib.pyplot as plt

import time



# Initialize an empty list to store heart rate values

heart_rates = []

# Generate and store a random heart rate value every second for 30 seconds

for i in range(30):

  heart_rate = random.randint(60, 100)

  heart_rates.append(heart_rate)

  time.sleep(1)



# Plot the heart rate values as a line graph

plt.plot(heart_rates)

plt.xlabel('Time (seconds)')

plt.ylabel('Heart rate (bpm)')

plt.title('Heart rate over time')

plt.show()



