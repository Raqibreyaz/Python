import time

max_retries = 5
attempts = 0
wait_time = 1 #in seconds

while(attempts < max_retries):
    print("Attempt ",attempts+1,' waiting time ',wait_time, ' s');
    time.sleep(wait_time)
    
    wait_time *=2
    attempts+=1;