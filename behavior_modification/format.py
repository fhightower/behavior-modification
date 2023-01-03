def _split_and_clean(s: str, split_char: str = "\n") -> list[str]:
    return [line.strip() for line in s.split(split_char) if line]


def _longest(a: str, b: str) -> str:
    if len(a) > len(b):
        return a
    return b


def _gen_string(top: str, bottom: str) -> tuple[str, str]:
    new_top = new_bottom = "| "
    longest = _longest(top, bottom)

    if longest == top:
        new_top += top + " "
        padding = len(top) - len(bottom)
        new_bottom += bottom + padding * " " + " "
    elif longest == bottom:
        new_bottom += bottom + " "
        padding = len(bottom) - len(top)
        new_top += top + padding * " " + " "

    return new_top, new_bottom


def format_string(s: str) -> str:
    # todo: handle cases where there are more tables in one row than the other
    # todo: catch error w/ unpacking here...
    first_row, second_row = _split_and_clean(s)
    first_row = _split_and_clean(first_row, "|")
    second_row = _split_and_clean(second_row, "|")

    new_first_row = new_second_row = ""

    for top, bottom in zip(first_row, second_row):
        new_top, new_bottom = _gen_string(top, bottom)
        new_first_row += new_top
        new_second_row += new_bottom

    new_first_row += "|"
    new_second_row += "|"
    return "\n".join([new_first_row, new_second_row])

