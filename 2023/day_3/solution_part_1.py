"""
Solution to Advent of Code 2023 day 3 part 1
Solved by doing some magic
"""

import re
import time
import sys
from dataclasses import dataclass

@dataclass
class EnginePartCandidate:
    part_num: int
    row_num: int
    start_pos: int

    def __post_init__(self):
        self.length = len(str(self.part_num))
        self.end_pos = self.start_pos + self.length

    def is_part(self, symbols):
        for s in symbols:
            if self.row_num-1 <= s.row_num <= self.row_num+1:
                # @Cameron, you were adding '1' to the end_pos which extended the evaluation.
                if self.start_pos-1 <= s.start_pos <= self.end_pos:
                    return True
        return False

@dataclass
class EngineSchematicSymbol:
    symbol: str
    row_num: int
    start_pos: int

    def __post_init__(self):
        self.length = len(str(self.symbol))
        self.end_pos = self.start_pos + self.length

class AOCEngineSchematicParser:
    def parse(self, lines):
        candidates = []
        symbols = []
        for i, l in enumerate(lines):

            # Find numbers and create an EnginePartCandidate for each
            numbers_matches = re.finditer(r'(\d+)', l)
            for m in numbers_matches:
                epc = EnginePartCandidate(part_num=int(m.group()), row_num=i, start_pos=m.start())
                candidates.append(epc)

            # Find symbols and create an EngineSchematicSymbol for each
            # symbols_matches = re.finditer(r'([!@#$%^&*/\-\+=])', l)
            symbols_matches = re.finditer(r'(\D)', l)
            for m in symbols_matches:
                if m.group() not in ('\n', '.'):
                    ess = EngineSchematicSymbol(symbol=m.group(), row_num=i, start_pos=m.start())
                    symbols.append(ess)

        return candidates, symbols

def solver(input_file):
    with open(input_file,'r') as file:
        entries = file.read().splitlines()
    candidates, symbols = AOCEngineSchematicParser().parse(entries)
    return sum(c.part_num for c in candidates if c.is_part(symbols))


if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
    start = time.time()
    answer = solver(input_file)
    solution_time = time.time() - start
    print(f"- **Answer**: {answer}")
    print(f"- **Timing**: {solution_time}")
