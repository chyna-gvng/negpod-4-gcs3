#!/usr/bin/bash
# Bash script to the if a file exists:
#   - Print 0 (If file exists & has content)
#   - Print 1 (If file exists but it's empty)
#   - Print 2 (If doesn't exist)

FILE="GCS_3_problems_20221105"
if [ -f "$FILE" ]; then
    if [ -s $FILE ];then
        echo "0"
    else
        echo "1"
    fi
else 
    echo "2"
fi