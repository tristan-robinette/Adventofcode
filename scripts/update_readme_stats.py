import collections
import contextlib
import dataclasses
import json
import os
import pathlib
from subprocess import check_output
from typing import Literal

X_MAS_EMOJIES = [
    "👼", "⛄", "🎁", "🦌", "🎄", "🤶", "🎅", "❄️", "🌟", "🍪", "⛸️", "🔔", "✨", "🥛", "🍷",
    "🥞", "🕯", "🎶", "🧦", "🤍", "🥂", "🌿", "🍾", "🏂", "🧣", "🛷", "☕", "🍫", "👪"
]

ROOT_PATH = pathlib.Path(__file__).parent.parent
CACHE_FILE = ROOT_PATH / "results_cache.json"


def load_cache():
    if CACHE_FILE.exists():
        return json.loads(CACHE_FILE.read_text())
    return {}


def save_cache(cache):
    CACHE_FILE.write_text(json.dumps(cache, indent=2))


@dataclasses.dataclass(kw_only=True)
class Submission:
    year: int
    day: int

    @property
    def emoji(self):
        return X_MAS_EMOJIES[int(self.day) % len(X_MAS_EMOJIES)]

    @property
    def path(self):
        return ROOT_PATH / str(self.year) / f"day_{self.day}"

    @property
    def input_file(self):
        return self.path / "input.txt"

    @property
    def p1(self):
        return self.path / "solution_part_1.py"

    @property
    def p2(self):
        return self.path / "solution_part_2.py"

    def _cache_key(self):
        import hashlib, pathlib

        h = hashlib.sha256()
        for file in (self.p1, self.p2, self.input_file):
            h.update(pathlib.Path(file).read_bytes())
        return h.hexdigest()

    def part_code(self, part: Literal['p1', 'p2']):
        with open(getattr(self, part), 'r') as f:
            code_text = f.read()
            return code_text[:code_text.find('if __name__ == "__main__":')].strip()

    def part_results(self, part: Literal['p1', 'p2']) -> dict:
        identifier = f"{self.year}-{self.day}"
        cache = load_cache()
        key = self._cache_key()

        if identifier in cache and cache[identifier].get("_cache_key") == key:
            return cache[identifier][part]

        results_for_day = {}
        for p in ("p1", "p2"):
            run_output = check_output(["python3", getattr(self, p), self.input_file]).decode()
            lines = run_output.splitlines()
            part_dict = {}

            for line in lines:
                with contextlib.suppress(Exception):
                    field = line.split('- **')[1].split('*')[0].strip()
                    value = line.split('**:')[-1].strip()
                    part_dict[field] = value

            results_for_day[p] = part_dict

        # Save both parts + cache key
        cache[identifier] = results_for_day
        cache[identifier]["_cache_key"] = key
        save_cache(cache)

        return results_for_day[part]


def get_years_to_build():
    return [d for d in os.listdir(os.path.join(ROOT_PATH)) if d.startswith("20")]


def get_available_days_to_process(year) -> set:
    return {
        int(d.split('_')[-1])
        for d in os.listdir(os.path.join(ROOT_PATH, str(year)))
        if d.startswith('day_')
    }


def build_markdown_heading(text: str, level: int = 3) -> str:
    return f"{'#' * level} {text}"


def build_markdown_list(*items):
    return "\n".join(f"- {item}" for item in items)


def build_markdown_code_block(code: str):
    return "\n".join(["<details>", "<summary>View code</summary>", "\n```python", code.strip(), "```", "</details>"])


def build_markdown_badge(submission: Submission, num_days: int):
    options = {
        # 'r' would be for R, 'javascript' for JS see more: https://simpleicons.org/
        "logo": "python",
        "logoColor": "f43f5e",
        # The background and text color of the button (don't include hashtag for hex)
        "color": "065f46",
        "labelColor": "white",
    }
    badge_name = f"{submission.year} Day {submission.day} Badge"
    endpoint = f"{submission.year}%20Day%20{submission.day}-none"
    qs = "".join(f"{name}={value}&" for name, value in options.items())
    link_to_sol = f"#-day-{submission.day}"
    if num_days > 1:
        # append '-' and the number when multiple headings with same name.
        link_to_sol += f"-{num_days - 1}"
    return f"[![{badge_name}](https://img.shields.io/badge/{endpoint}?{qs})]({link_to_sol})"


def get_badges_markdown(submissions: list[Submission]):
    years = set()
    day_counter = collections.Counter()
    markdown = [build_markdown_heading("Jump to solution", 4)]
    for submission in submissions:
        if submission.year not in years:
            years.add(submission.year)
            markdown.append("\n\n")
        day_counter[submission.day] += 1
        markdown.append(build_markdown_badge(submission, day_counter[submission.day] - 1))
        markdown.append("\n")
    return markdown


def get_code_submissions():
    submissions = []
    for year in get_years_to_build():
        days = get_available_days_to_process(year)
        for day in days:
            submissions.append(Submission(year=int(year), day=day))
    return submissions


def get_template_content(readme_template_name: str):
    return pathlib.Path(
        os.path.join(ROOT_PATH, f"{pathlib.Path(__file__).parent}/templates/{readme_template_name}")
    ).read_text()


def build_readme(readme_file_name: str = "readme", template_name='readmetemplate.md'):
    submissions = get_code_submissions()
    submissions.sort(key=lambda s: (s.year, s.day), reverse=True)
    years_processed = set()
    readme_parts = []
    badges = get_badges_markdown(submissions)

    for submission in submissions:
        print(f"building: {submission.year=} {submission.day=}")
        if submission.year not in years_processed:
            readme_parts.append(build_markdown_heading(f"Year {submission.year}"))
            years_processed.add(submission.year)
        readme_parts.append(build_markdown_heading(f"{submission.emoji} Day {submission.day}"))
        for part in ["1", "2"]:
            current_p = f'p{part}'
            readme_parts.append(build_markdown_heading(f"Day {submission.day} Solution part {part}", 4))
            p = submission.part_results(current_p)
            readme_parts.append(build_markdown_list(*[f"**{field}**: {val}" for field, val in p.items()]))
            readme_parts.append(build_markdown_code_block(submission.part_code(current_p)))
        readme_parts.append("<hr>")
    with open(f'{readme_file_name}.md', 'w') as f:
        readme_parts = [get_template_content(template_name), ' '.join(badges), '\n\n'.join(readme_parts)]
        f.write("\n\n".join(readme_parts))
    return


if __name__ == '__main__':
    build_readme()
