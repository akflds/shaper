# import modules to: manage timing, aid with processing JSON and
# help us make HTTP requests
    
import time
import json
import requests
    
# start by setting some global variables
# TODO: paste the base URL and API key in the empty quotes ("")

base_url = ""
header = {"X-Api-Key":""}
attempts = 1
   
# function to retrieve current bandwidth (part 2)

def get_values():

    # this function will use the requests.get() method to retrieve current
    # values for the bandwidth and network shaper
    
    while True:
    
        # start by making a request 
        # TODO: add the correct endpoint in the empty quotes
        
        r = requests.get(url=base_url+"", headers=header)
        
        # TODO: parse the results of this request into the variables below
        
        current_shaper = 
        current_bandwidth = 
        
        # to check if your function is working, uncomment the line below 
        # and run the program in your terminal
        # if you are successful it should print the values every 5s
        
        # print(f'Reading values\nShaper: {current_shaper}\nBandwidth: {current_bandwidth}\n')
        
        ## uncomment the line below when you start Part 3
        # adjust_shaper(current_shaper, current_bandwidth)
        
        time.sleep(5)
    
# starter code for part 3  

# function to calculate shaper value  
def adjust_shaper(current_shaper, current_bandwidth):
    new_shaper = -1 

    # TODO: calculate the min and max bandwidth and assign these to the
    # variables below
    # the minimum bandwidth should be 80% of the current bandwidth
    # the maximum bandwidth should be 90% of the current shaper value

    min_bandwidth =       
    max_bandwidth = 

    # TODO: check the current bandwidth against the min and max values
    
    # if the current bandwidth is greater than the max bandwidth, 
    # increase the shaper value by 10% and save this as `new_shaper`
   
    # if the current bandwidth is less than the minimum bandwidth, 
    # decrease the shaper value by 20% and save this as `new_shaper`
    
    # if the shaper has any other value, ignore this

   

    # TODO: finally, call the write_new_values() function, with 
    # the new_shaper and current_bandwidth variables

    
# function to send new values to the API and print the response
def write_new_values(new_shaper, current_bandwidth):
    global attempts
        
    # TODO: complete the data to accompany the rests, including your name 
    # and the appropriate variables
    
    payload = {"studentId":"",
            "currentBandwidth":,
            "newShaper":,
            "attemptNumber": attempts
            }

    # TOOD: add the appropriate endpoint in the empty quotes
    r = requests.post(url=base_url+"", headers=header, data=json.dumps(payload))

    # increment the number of attempts and print the response
    attempts += 1 
    print(f'Response:\n{r.json()\n'}

if __name__ == "__main__":
    every()
