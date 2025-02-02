# © 2025 SuRec Contributors. All Rights Reserved.
# Distributed under the terms of the Apache License 2.0.
# For more details, visit: https://www.apache.org/licenses/LICENSE-2.0

import sys

with open("copyright.txt", "r", encoding="utf-8") as f:
    HEADER = f.read().strip()


def add_header(file_path):
    with open(file_path, "r+", encoding="utf-8") as f:
        content = f.read()
        if not content.startswith(HEADER):
            content = (HEADER + "\n"*2) + content
            f.seek(0)
            f.write(content)


def check_header(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        if content.count(HEADER) > 1:
            print(f"Header already exists in {file_path}")
            sys.exit(1)


if __name__ == "__main__":
    for file_path in sys.argv[1:]:
        add_header(file_path)
        check_header(file_path)
