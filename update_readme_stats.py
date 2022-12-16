import os
import sys
import datetime
from subprocess import check_output
import re
import requests
import random

X_MAS_EMOJIES = [
    "👼", "⛄", "🎁", "🦌", "🎄", "🤶", "🎅", "❄️", "🌟", "🍪", "⛸️", "🔔", "✨", "🥛", "🍷",
    "🥞", "🕯", "🎶", "🧦", "🤍", "🥂", "🌿", "🍾", "🏂", "🧣", "🛷", "☕", "🍫", "👪"
]
#random.shuffle(X_MAS_EMOJIES)


if __name__ == '__main__':
    # Get date
    today_date = datetime.datetime.now()
    if today_date.month != 12:
        print("It's not December you silly goose!")
        sys.exit()
    current_year = today_date.year
    current_day = today_date.day
    
    root_path = os.path.dirname(os.path.realpath(__file__))

    # Read the README
    readme_file = os.path.join(root_path, 'readme.md')
    with open(readme_file, 'r') as f:
        readme = f.read()
        readme = readme.splitlines()
    
    # Read available days
    days_available = set()
    for d in os.listdir(os.path.join(root_path, str(current_year))):
        if d.startswith('day_'):
            days_available.add(int(d.split('_')[-1]))
    print(f"all days_available:", days_available)
    
    # READ known days
    days_known = set()
    readme_year = False
    for line in readme:
        # find year
        match = re.findall(r'## Year (\d+)', line)
        if match:
            readme_year = current_year == int(match[0])
        # create/find day
        match = re.findall(r'### . Day (\d+)', line)
        if match and readme_year:
            days_known.add(int(match[0]))
    print(f"days_known:", days_known)
    last_day_known = max(days_known, default=0)
    print(f"last_day_known:", last_day_known)
    days_available -= days_known
    print(f"unknown days_available:", days_available)
    if len(days_available) == 0:
        print(f"No new solutions found")
        sys.exit()
    
    # Fill in the README
    result = []
    readme_year = False
    readme_day = 0
    for line in readme:
        result.append(line)
        # find year
        match = re.findall(r'## Year (\d+)', line)
        #print(match, line)
        if match:
            year = int(match[0])
            random.Random(year).shuffle(X_MAS_EMOJIES)
            readme_year = current_year == year
            print(f"Year {year}")
        # create/find day
        match = re.findall(r'### . Day (\d+)', line)
        if match:
            readme_day = int(match[0])
        # add new timing
        #print(readme_year, readme_day)
        if (line == '<hr>' or last_day_known == 0) and readme_year and readme_day == last_day_known:
            result.append('')
            for day in sorted(days_available):
                print(f"Updating day {day} {current_year}")
                # get day's name
                emoji = X_MAS_EMOJIES[day % len(X_MAS_EMOJIES)]
                result.append(f"### {emoji} Day {day}\n")
                # Get each part
                for part in range(1,2+1):
                    result.append(f"#### Day {day} Solution Part {part}\n")
                    day_path = os.path.join(root_path, str(current_year), f"day_{day}")
                    solution_file = os.path.join(day_path, f"solution_part_{part}.py")
                    input_file = os.path.join(day_path, f"input.txt")
                    # Perform the run
                    run_output = check_output(["python3", solution_file, input_file])
                    run_output = run_output.decode('utf-8').strip()
                    result += run_output.splitlines()
                    # Add the approach
                    with open(solution_file, 'r') as f:
                        code_text = f.read()
                    code_text = code_text[:code_text.find('if __name__ == "__main__":')].strip()
                    result.append("\n\n```python")
                    result += code_text.splitlines()
                    result.append("```")
                result.append('<hr>')
    result.append('')
    
    with open(readme_file, 'w') as f:
        f.write('\n'.join(result))
