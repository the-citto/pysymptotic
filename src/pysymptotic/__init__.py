"""Init."""

import importlib.metadata
import os
import re

import rich_click as click


os.environ["MYPY_FORCE_COLOR"] = "1"
os.environ["CLICOLOR_FORCE"] = "1"


class _Version(str):

    __slots__ = ()

    @property
    def as_tuple(self) -> tuple[int, ...]:
        version_re = re.match(r"(\d+).(\d+).(\d+)", self)
        if version_re is None:
            raise ValueError
        return tuple(map(int, version_re.groups()))

    @property
    def major(self) -> int:
        return self.as_tuple[0]

    @property
    def minor(self) -> int:
        return self.as_tuple[1]

    @property
    def patch(self) -> int:
        return self.as_tuple[2]


__version__: str = _Version(importlib.metadata.version(__name__))



click.rich_click.COMMAND_GROUPS = {
    # "leetcode": [
    #     {
    #         "name": "Level",
    #         "commands": [
    #             "easy",
    #             "medium",
    #             "hard",
    #         ],
    #     },
    # ],
    # "leetcode easy": [
    #     {
    #         "name": "Problems",
    #         "commands": [
    #             "two-sum",
    #             "add-two-numbers",
    #         ],
    #     },
    # ],
    # "leetcode medium": [
    #     {
    #         "name": "Problems",
    #         "commands": [
    #             "longest-substring-withouut-characters",
    #             "longest-palindromic-substring",
    #         ],
    #     },
    # ],
    # "leetcode hard": [
    #     {
    #         "name": "Problems",
    #         "commands": [
    #             "median-of-two-sorted-arrays",
    #         ],
    #     },
    # ],
}




