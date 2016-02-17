import time
from multiprocessing import Process
from QuadBench import math,base

start = time.time()
# Save for later
absolute_start = start

# Output the message thing before we start
base.start_message()

##
# Multiplier test
##
for i in range(0,23):
  if i == 1:
    print("Multiplier task 1", end="")
  else:
    print("\r" + "Multiplier task " + str(i), end="")
  math.multiplier(i,i)

finish = time.time()

time_multiplier = base.calc_time(start, finish)

print("\n\033[92mMultiplier took " + str(time_multiplier) + " seconds\033[0m\n")

##
# Square number calculation test
##

start = time.time()

for i in range(0,800):
  if i == 1:
    print("Squares task 1", end="")
  else:
    print("\r" + "Squares task " + str(i), end="")
  math.squares(math.multiplier(i,2))

finish = time.time()

time_squares = base.calc_time(start, finish)

print("\n\033[92m" + "Squares took " + str(time_squares) + " seconds\033[0m\n")

