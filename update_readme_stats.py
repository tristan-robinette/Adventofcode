import os
import pathlib
from subprocess import check_output
import re

X_MAS_EMOJIES = [
    "👼", "⛄", "🎁", "🦌", "🎄", "🤶", "🎅", "❄️", "🌟", "🍪", "⛸️", "🔔", "✨", "🥛", "🍷",
    "🥞", "🕯", "🎶", "🧦", "🤍", "🥂", "🌿", "🍾", "🏂", "🧣", "🛷", "☕", "🍫", "👪"
]


ROOT_PATH = os.path.dirname(os.path.realpath(__file__))


def get_years_to_build():
    return [d for d in os.listdir(os.path.join(ROOT_PATH)) if d.startswith("20")]


def get_available_days_to_process(year) -> set:
    return {
        int(d.split('_')[-1])
        for d in os.listdir(os.path.join(ROOT_PATH, str(year)))
        if d.startswith('day_')
    }

def get_readme_text(filename='readme.md'):
    readme_file = os.path.join(ROOT_PATH, filename)
    with open(readme_file, 'r') as f:
        return f.read()

def does_day_already_exists_for_year(readme, path) -> bool:
    year_exists = False
    day_exists = False
    year = path.split("/")[-2]
    day = path.split("/")[-1]
    for line in readme.splitlines():
        if year_match := re.findall(r'## Year (\d+)', line):
            if str(year_match[0]) == str(year):
                year_exists = True
        if day_match := re.findall(r'## Day (\d+)', line):
            if str(day_match[0]) == str(day):
                day_exists = True
    return year_exists is True and day_exists is True

def get_day_existing_text(readme, path):  # sourcery skip: use-named-expression
    year = path.split("/")[-2]
    day = path.split("/")[-1]
    year_index = 0
    start_day_index = 0
    existing_day_text = []
    # find year boundary
    for line in readme.splitlines():
        year_match = re.findall(r'## Year (\d+)', line)
        if year_match and str(year_match[0]) == str(year):
            year_index = readme.index(line)
            break
    # Find first day within year boundary
    for line in readme[year_index:].splitlines():
        day_match = re.findall(r'Day (\d+)', line)
        if day_match and str(day_match[0]) == str(day) and "###" in line:
            start_day_index = readme[year_index: ].index(line)
            break
    # get text for that day
    for line in readme[year_index:][start_day_index: ].splitlines():
        if line.strip() == "<hr>":
            existing_day_text.extend((line, ''))
            break
        existing_day_text.append(line)
    return existing_day_text

def get_text_for_new_day(path):
    year = path.split("/")[-2]
    day = path.split("/")[-1]
    print(f"Updating day {day} {year}")
    # get day's name
    emoji = X_MAS_EMOJIES[int(day) % len(X_MAS_EMOJIES)]
    result = ['', f"### {emoji} Day {day}\n"]
    # Get each part
    for part in range(1, 2 + 1):
        result.append(f"#### Day {day} Solution Part {part}\n")
        day_path = os.path.join(ROOT_PATH, str(year), f"day_{day}")
        solution_file = os.path.join(day_path, f"solution_part_{part}.py")
        input_file = os.path.join(day_path, "input.txt")
        # Perform the run
        run_output = check_output(["python3", solution_file, input_file])
        run_output = run_output.decode('utf-8').strip()
        result += run_output.splitlines()[-2:]
        # Add the approach
        with open(solution_file, 'r') as f:
            code_text = f.read()
        code_text = code_text[:code_text.find('if __name__ == "__main__":')].strip()
        result.append("")
        result.append("")
        result.append("```python")
        result += code_text.splitlines()
        result.append("```")
        result.append('')
    result.append('<hr>')
    return result


def build_day(readme, year, day) -> list:
    path_to_dir = os.path.join(ROOT_PATH, str(year), str(day))
    if does_day_already_exists_for_year(readme, path_to_dir):
        return get_day_existing_text(readme, path_to_dir)
    return get_text_for_new_day(path_to_dir)

def add_dropdown_to_day(day_lines:list) -> list:
    # check if details already exists
    if any(line.startswith("<details>") for line in day_lines):
        return day_lines
    # track open/close of code tag
    found_open_tag = False

    out = []
    for line in day_lines:
        if line.startswith("```"):
            if not found_open_tag:
                out += ['<details>', '<summary>View code</summary>', '']
                found_open_tag = True
            else:
                out += ['```', '', '</details>', '']
                found_open_tag = False
                continue
        out.append(line)
    return out

def add_toc_to_day(day_lines:list) -> list:
    # todo implement
    return day_lines

def add_day_plugins(readme_lines:list, code_as_dropdown=True, build_toc=True) -> list:
    if code_as_dropdown:
        readme_lines = add_dropdown_to_day(readme_lines)
    if build_toc:
        readme_lines = add_toc_to_day(readme_lines)
    return readme_lines

def main(readme_template_name=None, code_as_dropdown=True, build_toc=True):
    current_readme = get_readme_text()
    output_readme = []

    for year_to_build in get_years_to_build():
        days_available = get_available_days_to_process(year_to_build)
        for day in days_available:
            if int(day) == 1:
                output_readme += [f'### Year {year_to_build}', '']
            readme_lines = build_day(current_readme, year_to_build, day)
            readme_lines = add_day_plugins(readme_lines, code_as_dropdown, build_toc)
            output_readme += readme_lines

    readme_template = ''
    if readme_template_name:
        readme_template = pathlib.Path(
            os.path.join(ROOT_PATH, readme_template_name)
        ).read_text()
    readme_file = os.path.join(ROOT_PATH, 'readme.md')
    with open(readme_file, 'w') as f:
        f.write(readme_template + '\n'.join(output_readme))


if __name__ == '__main__':
    main(readme_template_name='readmetemplate.md')
