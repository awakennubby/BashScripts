#!/bin/bash

date
FILE_NAME=`python3 to_do.py`
echo "$FILE_NAME"
mv $FILE_NAME to_do_dates
cd to_do_dates
subl $FILE_NAME