"""
Script to create directories to get gud at advent of code.
"""
from pathlib import Path
import datetime
import os
import shutil
import calendar
import re
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Create directory for advent of code")
    parser.add_argument('--all', action='store_true', help='Create a directory for every day in month')
    parser.add_argument('--overwrite', action='store_true', help='Will overwrite the current day folder.')

    dir_path = os.path.dirname(os.path.realpath(__file__))
    today_date = datetime.datetime.now()
    current_year = today_date.year
    day = today_date.day
    days_to_make = [day]

    args = parser.parse_args()
    if args.all:
        days_to_make = [day + 1 for day in range(calendar.monthrange(today_date.year, today_date.month + 1)[1])]

    for day in days_to_make:
        if day > 25:
            break
        new_path = f"{dir_path}/{current_year}/day_{day}"

        if os.path.isdir(new_path) and not args.overwrite:
            continue

        Path(new_path).mkdir(parents=True, exist_ok=True)

        # create base input file and solution
        try:
            open(os.path.join(new_path, 'input.txt'), "x")
        except FileExistsError:
            pass

        for part in range(2):
            part += 1
            solution_file_path = os.path.join(new_path, f"solution_part_{part}.py")
            shutil.copyfile(f"{dir_path}/solution_template.py", solution_file_path)
            with open(solution_file_path, "r+") as f:
                content = f.read()
                replacements = re.findall(r'{{(.*?)}}(?!})', content)
                for variable in replacements:
                    variable = variable.strip()
                    if variable == "year":
                        content = content.replace("{{" + variable + "}}", str(current_year))
                    elif variable == "day":
                        content = content.replace("{{" + variable + "}}", str(day))
                    else:
                        content = content.replace("{{" + variable + "}}", str(part))
                f.seek(0)
                f.truncate()
                f.write(content)
