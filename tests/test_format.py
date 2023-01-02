import pytest

from behavior_modification.format import format_string

EXAMPLES = [
    (
        """
| a       |     b             |
| c| d     |
""",
        """| a | b |
| c | d |""",
    ),
    (
        """
| aa|     bb          |
| c     | d|
""",
        """| aa | bb |
| c  | d  |""",
    ),
    (
        """
| aaa|     bb          | c          |
| d     | eee | ff|
""",
        """| aaa | bb  | c  |
| d   | eee | ff |""",
    ),
]


@pytest.mark.parametrize("in_, out", EXAMPLES)
def test_examples(in_, out):
    assert format_string(in_) == out
