import time

def calc_time(time1, time2):
  return time2 - time1

def calc_score(scores):
  length = len(scores)
  total = 0

  for s in scores:
    total += s

  total /= length
  # Round it and muliply by 100 so scores are more exact without having a billion decimals
  return round(total * 100)


# No. I will not do this using some other, less retarded method.
def start_message():
  print("\033[91m") # Make this fucker red
  print("---\nThis test will run a lot of (simple, but overkill) math operations and stuff.")
  print("It is in no way intended to be taken as an accurate representation of a computer's processing capabilities. But if you want to, then feel free.\n")
  print("Each task will loop and get a lot harder each time. i.e Multiplier tasks 1-20 will complete in a matter of seconds or less. While later tasks can take minutes on slower machines.")
  print("If anyone bothers to run this on something like a Raspberry Pi, it might even take hours.")
  print("---\n")
  print("\033[0m") # Back to regular text
  time.sleep(5)
