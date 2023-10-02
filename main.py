from pathlib import Path
from typing import List


SOURCE = Path.home().joinpath("Downloads")
DELIMITER = "-"


def is_delimiter_count_valid(parameter: str, max: int = 1, delimiter: str = DELIMITER) -> bool:
    """
    Verify the delimiter only occurs a maximum number of times in a string.
    """
    return parameter.count(delimiter) == max


def is_delimiter_in_valid_position(parameter: str, delimiter: str = DELIMITER) -> bool:
    """
    Verify the delimiter is not the first or last element of a string.
    """
    return not parameter.startswith(delimiter) and not parameter.endswith(delimiter)


def can_parse(file: Path, delimiter = DELIMITER) -> bool:
    return (is_delimiter_count_valid(parameter = file.name) and
            is_delimiter_in_valid_position(parameter = file.stem))


def main():

    try:

        cannot_parse : List[Path] = []
        
        for invalid_file in (item for item in SOURCE.iterdir() if item.is_file()):

            if can_parse(file = invalid_file):
                folder, file = invalid_file.name.split(DELIMITER)
                parent = SOURCE.joinpath(folder.title())
                parent.mkdir(parents = False, exist_ok = True)
                target = parent.joinpath(file.lower().replace(" ","-"))
                print(f"Renaming {invalid_file} --> {target}")
                invalid_file.rename(target)
            else:
                cannot_parse.append(invalid_file)
        
        if cannot_parse:
            print("\nCannot Parse the Following:")
            for file in cannot_parse:
                print(file.name)

    except(FileExistsError, OSError) as e:
        print(e)

if __name__ == "__main__":
    main()
