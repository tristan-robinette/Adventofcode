import os
import pathlib
from subprocess import check_output
import re

X_MAS_EMOJIES = [
    "👼", "⛄", "🎁", "🦌", "🎄", "🤶", "🎅", "❄️", "🌟", "🍪", "⛸️", "🔔", "✨", "🥛", "🍷",
    "🥞", "🕯", "🎶", "🧦", "🤍", "🥂", "🌿", "🍾", "🏂", "🧣", "🛷", "☕", "🍫", "👪"
]

ROOT_PATH = pathlib.Path(__file__).parent.parent

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
    year_index = 0
    year = path.split("/")[-2]
    day = path.split("/")[-1]
    for line in readme.splitlines():
        if year_match := re.findall(r'## Year (\d+)', line):
            year_index = readme.index(line)
            if str(year_match[0]) == str(year):
                year_exists = True
                break
    if year_exists:
        for line in readme[year_index:].splitlines():
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


def build_day(year, day) -> list:
    path_to_dir = os.path.join(ROOT_PATH, str(year), str(day))
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

def build_toc_link(day, days_in_toc:list, toc_config:dict, year_to_build):
    badge_name = f"{year_to_build} Day {day} Badge"
    endpoint = f"{year_to_build}%20Day%20{day}-none"
    qs = "".join(f"{name}={value}&" for name, value in toc_config.items())
    link_to_sol = f"#-day-{day}"
    if day in days_in_toc:
        # append '-' and the number when multiple headings with same name.
        link_to_sol += f"-{len([d for d in days_in_toc if d == day])}"
    return f"[![{badge_name}](https://img.shields.io/badge/{endpoint}?{qs})]({link_to_sol})"


def add_day_plugins(readme_lines:list, code_as_dropdown=True) -> list:
    if code_as_dropdown:
        readme_lines = add_dropdown_to_day(readme_lines)
    return readme_lines


def main(readme_template_name=None, code_as_dropdown=True, build_toc=True, toc_config=None):
    current_readme = get_readme_text()
    output_readme = []
    toc_config = toc_config or DEFAULT_TOC_CONFIG
    days_in_toc = []
    toc = ["#### Jump to solution", ''] if build_toc else []

    for year_to_build in get_years_to_build():
        days_available = get_available_days_to_process(year_to_build)
        for i, day in enumerate(days_available):
            emoji = X_MAS_EMOJIES[int(day) % len(X_MAS_EMOJIES)]
            base_log = f"{emoji} YEAR: {year_to_build} | DAY: {day}"
            # if first solve for year add in year header
            if i == 0:
                output_readme += [f'### Year {year_to_build}', '']
            path_to_dir = os.path.join(ROOT_PATH, str(year_to_build), str(day))
            if does_day_already_exists_for_year(current_readme, path_to_dir):
                print(f"{base_log} =>  EXISTS")
                readme_lines = get_day_existing_text(current_readme, path_to_dir)
            else:
                print(f"{base_log} =>  BUILDING")
                readme_lines = build_day(year_to_build, day)
            readme_lines = add_day_plugins(readme_lines, code_as_dropdown)
            output_readme += readme_lines
            if build_toc:
                result = build_toc_link(day, days_in_toc, toc_config, year_to_build)
                days_in_toc.append(day)
                toc.append(result)
        toc.append("")

    if build_toc:
        toc.extend(["<hr>", ''])

    readme_template = ''
    if readme_template_name:
        readme_template = pathlib.Path(
            os.path.join(ROOT_PATH, f"{pathlib.Path(__file__).parent}/templates/{readme_template_name}")
        ).read_text()
    readme_file = os.path.join(ROOT_PATH, 'readme.md')
    with open(readme_file, 'w') as f:
        f.write(readme_template + '\n'.join(toc + output_readme))


if __name__ == '__main__':
    DEFAULT_TOC_CONFIG = {
        # 'r' would be for R, 'javascript' for JS see more: https://simpleicons.org/
        "logo": "python",
        "logoColor": "f43f5e",
        # The background and text color of the button (don't include hashtag for hex)
        "color": "065f46",
        "labelColor": "white",
    }
    main(readme_template_name='readmetemplate.md', toc_config=DEFAULT_TOC_CONFIG)
