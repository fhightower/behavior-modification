# todo: make sure `Iterator` is correct
# todo: update `file_path` arg to also take a Path object
def _get_file_content(file_path: str) -> Iterator[str]:
    file_lines = None
    with open(file_path, "r") as f:
        yield from f.readlines()


# todo: test and clean this function...
def _get_tables(lines: Iterator[str]) -> Iterator[str]:
    in_table = False
    current_table = []
    for line in lines:
        if in_table:
            table_complete = not line.strip().startswith("|")
            if table_complete:
                in_table = False
                yield current_table
            else:
                current_table.append(line)
            continue

        if line.strip().startswith("|"):
            in_table = True
            current_table.append(line)


def find_tables(file_path: str) -> Iterator[str]:
    """Find all tables in the given file_path."""
    lines = _get_file_content(file_path)
    tables = _get_tables(lines)
    print(tables)


