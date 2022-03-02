# The algorithm
# The program will be very simple:
#    1 - Ask user what it wants to be reminded about
#       2 - Ask when (in what amount of time, in minutes)
#           3 - Calculate timeout (minutes multiply by seconds)
#               4 - Wait for the specified time
#                   5 - Remind of what I requested in step 1
# * Although the algorithm is simple, the implementation of each step can make this app very useful. For example, in steps 1 and 2, I can communicate through different channels: keyboard, voice, or messaging apps.


import time
print("What shall I remind you about?")
text = str(input())

print("In how many minutes?")
local_time = float(input())

local_time = local_time * 60

time.sleep(local_time)

print(text)
