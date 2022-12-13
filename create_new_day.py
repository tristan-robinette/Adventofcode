"""
Script to create directories to get gud at advent of code.
"""
import datetime
import os
import sys
import shutil
import calendar
import re
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Create directory for advent of code")
    parser.add_argument('--all', action='store_true', help='Create a directory for every day in month')
    parser.add_argument('--anticipation', action='store_true', help='Will treat the current day as tomorrow in anticipation')
    parser.add_argument('--overwrite', action='store_true', help='Will overwrite the current day folder.')
    args = parser.parse_args()

    today_date = datetime.datetime.now()
    if today_date.month != 12:
        print("It's not December you silly goose!")
        sys.exit()
    current_year = today_date.year
    current_day = today_date.day + args.anticipation
    last_day = 25 if args.all else current_day
    
    dir_path = os.path.dirname(os.path.realpath(__file__))
    
    for day in range(current_day, last_day+1):
        day_path = os.path.join(dir_path, current_year, f"day_{day}")

        if os.path.isdir(day_path) and not args.overwrite:
            continue

        print(f"creating day {day}")
        os.makedirs(day_path, exist_ok=True)

        # create blank input files
        for input_file in ['input.txt', 'input1.txt']:
            input_path = os.path.join(day_path, input_file)
            with open(input_path, 'w') as f:
                f.write('')
        
        # create the solutions
        for part in range(1,2+1):
            solution_file_path = os.path.join(day_path, f"solution_part_{part}.py")
            template_path = os.path.join(dir_path, "solution_template.py")
            shutil.copyfile(template_path, solution_file_path)
            
            with open(solution_file_path, 'r') as f:
                content = f.read()
            replacements = {'year': current_year, 'day': day, 'part': part}
            for var, val in replacements.items():
                content = content.replace('{{' + var + '}}', str(val))
            with open(solution_file_path, 'w') as f:
                f.write(content)
                
