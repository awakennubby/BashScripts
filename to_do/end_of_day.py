#!/usr/bin/env python3
from datetime import datetime
import os
import re
#We wanna run this bad boy at like 11:59pm
def count_items():
    to_do_count = 0
    final_count = 0
    curr_directory = os.getcwd()
    curr_date = datetime.now().date()
    new_file_str = curr_directory+ "/to_do_dates/to_do_"  +str(curr_date)+".txt"
    new_file = open(new_file_str,'r')
    last_line = new_file.readlines()
    #Strip of new chars then we can use this 
    for i,entries in enumerate(last_line):
        last_line[i] = entries.strip()
        if last_line[i] == '':
            last_line.pop(i)
    #Counts to_do list items and completed items
    #print(last_line)
    for i, entries in enumerate(last_line):
        if last_line[i] == "To-Do:\n":
            while last_line[i] != "Completed:\n":
                to_do_count += 1
                i += 1
            i+= 1
            while i <= len(last_line):
                final_count += 1
                i += 1
    #print(to_do_count - 1,final_count -1)
    return (to_do_count-1,final_count-1)
def log_items(incomplete_count,complete_count):
    #Open up log and search through the array for - items
    #Once you reach "Completed: start adding that into the completed array"
    #Log the items complete as well
    pass
def main():
    items_complete = count_items()
    print(items_complete)
    #Go through To-Do and count the - , then go through completed and count the - 
    #Put it into the log, then log activies in log as well

if __name__ == "__main__":
    main()