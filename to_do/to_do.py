#!/usr/bin/env python3
from datetime import datetime,date,time,timezone
def main():
    #1) Read last line from log.txt
    curr_date = datetime.now().date()
    #log_file = open('log.txt','r')
    #last_line = log_file.readlines()[-1].strip()
    #2) Parse CSV into an array
    #3) Create a new file from the Year,Month,Day
    new_file_str = "to_do_"  +str(curr_date)+".txt"
    new_file = open(new_file_str,'w')
    new_file.write("Bet on yourself :)\n\nTo-Do:\n\n-\n-\n-\n\nCompleted:\n\n")
    new_file.close()
    print(new_file_str)
    return new_file_str
    #At the end of the day, run a script to log values into log
if __name__ == "__main__":
    main()