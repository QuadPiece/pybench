##
#  This entire application is a huge mess of code.
#  But I am not sorry at all.
#
#  *trollface*
##

import time
from multiprocessing import Process
from QuadBench import math,base

# Output the message thing before we begin
base.start_message()

start = time.time()
# Save for later
absolute_start = start

##
# Multiplier test
##
for i in range(0,25):
  if i == 1:
    print("Multiplier task 1", end="")
  else:
    print("\r" + "Multiplier task " + str(i), end="")
  math.multiplier(i,i)

finish = time.time()

time_multiplier = base.calc_time(start, finish)

print("\n\033[92mMultiplier took " + str(round(time_multiplier, 2)) + " seconds\033[0m\n")

##
# Square number calculation test
##

start = time.time()

for i in range(0,901):
  if i == 1:
    print("Squares task 1", end="")
  else:
    print("\r" + "Squares task " + str(i), end="")
  math.squares(math.multiplier(i,2))

finish = time.time()

time_squares = base.calc_time(start, finish)

print("\n\033[92m" + "Squares took " + str(round(time_squares, 2)) + " seconds\033[0m\n")

