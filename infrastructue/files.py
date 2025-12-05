from pathlib import Path


def read_file_to_list(filename):
    # Path relative to project root (2 levels up from this file)
    project_root = Path(__file__).parent.parent
    input_file = project_root / filename
    with open(input_file, "r", encoding="utf-8") as file:
        return [line.strip() for line in file]