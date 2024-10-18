# Devon Taylor
# U2 Final
# DS
# 10/9/24

from ecosystem import *
from time import sleep

DAYS_SIMULATED = 15
RIVER_SIZE = 15
START_BEARS = 10
START_FISH = 10

def BearFishRiver():

  r = River(RIVER_SIZE, START_BEARS, START_FISH)
  day = 0
  done = False
  full = False
  for day in range(DAYS_SIMULATED):
    print(f"\n\nDay: {day+1}")
    print(r)
    print(f"\nStarting Poplation: {r.population} animals")
    done = r.new_day()
    print(f"Ending Poplation: {r.population} animals")
    print(r)
    day += 1
    sleep(5)
    if r.population >= RIVER_SIZE**2:
      full = True
      break
  if full == True:
    print("River is full")
  else:
    pass

if __name__ == "__main__":
  BearFishRiver()