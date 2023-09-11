#!/usr/bin/env python
import re

def remove_string(file_name, string):
  with open(file_name, "r") as f:
    lines = f.readlines()

  new_lines = []
  for line in lines:
    if not re.search(re.escape(string), line):
      new_lines.append(line)

  with open(file_name, "w") as f:
    f.writelines(new_lines)


if __name__ == "__main__":
  file_name = "test.txt"
  string = "43 4f 52 52 55 50 54 45 44"

  remove_string(file_name, string)
