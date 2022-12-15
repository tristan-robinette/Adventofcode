import time
from typing import Callable, List, Any, Union
import datetime
import os
import pandas as pd

X_MAS_EMOJIES = [
    "👼", "⛄", "🎁", "🦌", "🎄", "🤶", "🎅", "❄️", "🌟", "🍪", "⛸️", "🔔", "✨", "🥛", "🍷",
    "🥞", "🕯", "🎶", "🧦", "🤍", "🥂", "🌿", "🍾", "🏂", "🧣", "🛷", "☕", "🍫", "👪"
]

README_TEMPLATE_FILE_NAME = "readmetemplate"


def run_func(func: Callable, input_file: str) -> List[Union[float, Any]]:
    """
    Runs a solution function with its daily input and times it.
    Returns the solution time and output of the solution in an array.
    :param func:
    :param input_file:
    :return:
    """
    start = time.time()
    sol = func(input_file)
    solution_time = time.time() - start
    return [solution_time, sol]


def get_new_lines(num_lines:int):
    """
    returns a string of new lines to easily create long string document.
    :param num_lines:
    :return:
    """
    out = ""
    for _ in range(num_lines):
        out += "\n"
    return out


def gen_mkd(dataframe: pd.DataFrame):
    """
    Takes a df and returns markdown to insert into the readme
    :param dataframe:
    :return:
    """
    text_out = f"# Solutions {get_new_lines(2)}"
    emojies = list(set(X_MAS_EMOJIES))
    for year_num in dataframe["year"].unique():
        text_out += f"### Year {year}{get_new_lines(2)}"
        df = dataframe.loc[dataframe["year"] == year_num]
        group = df.groupby("day")
        for day_name, group in group:
            text_out += f"### {emojies[0]} Day {day_name} {get_new_lines(2)}"
            emojies.remove(emojies[0])
            for i, row in group.iterrows():
                text_out += f"##### {' '.join(row['solution_name'].split('_')).title()} {get_new_lines(2)}"
                text_out += f"- Answer: {row['result']} {get_new_lines(1)}"
                text_out += f"- Timing: {row['timing']} {get_new_lines(1)}"
                text_out += get_new_lines(2)
                text_out += f"```python{get_new_lines(1)}{row['code_text']}{get_new_lines(1)}```{get_new_lines(1)}"
            text_out += f"<hr>{get_new_lines(2)}"
    text_out += f"{get_new_lines(2)}"
    return text_out


if __name__ == '__main__':
    results = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    new_path = f"{dir_path}/{datetime.datetime.now().year}"

    if os.path.isdir(new_path):
        dirs = sorted([x[0] for x in os.walk(new_path, topdown=True)])[1:]
        for idx, day in enumerate(dirs, 1):
            year = day.split("/")[-2]
            print(day)
            if day == "/Users/tristanrobinette/PycharmProjects/advent/2022/day_12":
                break
            for path, arr, files in os.walk(day):
                day_num = path.split("/")[-1]
                for file in files:
                    if ".py" in file:
                        sol_name = f"{day_num}_{file.split('.')[0]}"
                        code_text = open(os.path.join(path, file), "r").read()
                        input_file_path = os.path.join(path, 'input.txt')
                        code_text = code_text[:code_text.find('if __name__ == "__main__":')]
                        code = compile(code_text, '', 'exec')
                        exec(code)
                        results.append(
                            [idx] + [year] + [sol_name] + run_func(solution, input_file_path) + [code_text]
                        )
                        del solution  # is this needed?
                        del code  # is this needed?

    result = pd.DataFrame(results, columns=["day", "year", "solution_name", "timing", "result", "code_text"])

    base_template = open(f"{README_TEMPLATE_FILE_NAME}.md").read()
    with open("readme.md", "r+") as f:
        f.seek(0)
        f.truncate()
        f.write(f"{base_template}{get_new_lines(2)}{gen_mkd(result)}")
