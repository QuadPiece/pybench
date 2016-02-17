from multiprocessing import Process

def multiplier(base, end):
  counter = 1
  while True:
    base *= base
    counter += 1
    if counter >= end:
      break
  return base

def squares(end):
  counter = 1
  number = 2
  while True:
    square = number * number
    counter += 1
    number += 1
    if counter >= end:
      break