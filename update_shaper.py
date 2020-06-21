# import modules to: manage timing, aid with processing JSON and
# help us make HTTP requests
    
import time
import json
import requests
    
# paste the base URL and API key in the empty quotes ("")
base_url = ""
header = {"X-Api-Key":""}
attempts = 1
   
# function to retrieve current bandwidth (part 2)

def get_values():
    
    while True:
    
        # we'll use the requests.get() method to retrieve current
        # values for the bandwidth and network shaper
        
        # add the correct endpoint in the empty quotes
        
        r = requests.get(url=base_url+"", headers=header)
        
        # parse the results of this request into the variables below
        
        current_shaper = 
        current_bandwidth = 
        
        # to check if your function is working, uncomment the line below 
        # and run the program in your terminal, it should print both values every 5s
        
        # print(f'Reading values\nShaper: {current_shaper}\nBandwidth: {current_bandwidth}\n')

        # when you are ready to start part 3, uncomment the line below and 
        # follow the instructions in the course 
      
        # monitor_shaper(current_shaper, current_bandwidth)
        
        time.sleep(5)

# part 3 - complete the remaining functions

def monitor_shaper():
    return

def adjust_shaper():
    return

# start the program
if __name__ == "__main__":
    get_values()

