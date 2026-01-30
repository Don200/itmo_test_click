from __future__ import annotations

import collections.abc as cabc
import enum
import errno
import inspect
import os
import sys
import typing as t
from collections import abc
from collections import Counter
from contextlib import AbstractContextManager
from contextlib import contextmanager
from contextlib import ExitStack
from functools import update_wrapper
from gettext import gettext as _
from gettext import ngettext
from itertools import repeat
from types import TracebackType

from . import types
from ._utils import FLAG_NEEDS_VALUE
from ._utils import UNSET
from .exceptions import Abort
from .exceptions import BadParameter
from .exceptions import ClickException
from .exceptions import Exit
from .exceptions import MissingParameter
from .exceptions import NoArgsIsHelpError
from .exceptions import UsageError
from .formatting import HelpFormatter
from .formatting import join_options
from .globals import pop_context
from .globals import push_context
from .parser import _OptionParser
from .parser import _split_opt
from .termui import confirm
from .termui import prompt
from .termui import style
from .utils import _detect_program_name
from .utils import _expand_args
from .utils import echo
from .utils import make_default_short_help
from .utils import make_str
from .utils import PacifyFlushWrapper

if t.TYPE_CHECKING:
    from .shell_completion import CompletionItem

F = t.TypeVar("F", bound="t.Callable[..., t.Any]")
V = t.TypeVar("V")


def parse_due_date(due: str) -> t.Optional[datetime]:
    today = datetime.today()
    if due == "tomorrow":
        return today + timedelta(days=1)
    elif due.startswith("+") and due.endswith("d"):
        days = int(due[1:-1])
        return today + timedelta(days=days)
    else:
        try:
            return datetime.strptime(due, "%Y-%m-%d")
        except ValueError:
            raise BadParameter(f"Invalid due date format: {due}")


class Context:
    # ... existing code ...

    def list_tasks(self) -> list[Task]:
        tasks = self.get_tasks()
        tasks.sort(key=lambda task: (task.due or datetime.max))
        return tasks

    # ... existing code ...

class Task:
    def __init__(self, due: str):
        self.due = parse_due_date(due)

    # ... existing code ...

# Add tests for new due date formats
@pytest.mark.parametrize(
    "due, expected",
    [
        ("tomorrow", datetime.today() + timedelta(days=1)),
        ("+3d", datetime.today() + timedelta(days=3)),
        ("2023-10-10", datetime(2023, 10, 10)),
    ],
)
def test_parse_due_date(due, expected):
    assert parse_due_date(due) == expected

# Test sorting tasks
def test_sorting_tasks():
    task1 = Task("2023-10-10")
    task2 = Task("2023-10-11")
    task3 = Task(None)
    tasks = [task1, task2, task3]
    sorted_tasks = sorted(tasks, key=lambda task: (task.due or datetime.max))
    assert sorted_tasks == [task1, task2, task3]
