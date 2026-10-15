"""Compatibility imports for the renamed :mod:`patience_diff` package."""

import importlib
import sys

import patience_diff as _patience_diff

__path__ = _patience_diff.__path__
__version__ = _patience_diff.__version__
__all__ = [
    name for name in _patience_diff.__all__
    if hasattr(_patience_diff, name)
]

for _name in __all__:
    globals()[_name] = getattr(_patience_diff, _name)

for _module_name in (
    "hunk",
    "hunks",
    "matching_block",
    "move_id",
    "move_kind",
    "patience_diff",
    "patience_diff_lib",
    "plain_diff",
    "range",
):
    sys.modules[f"{__name__}.{_module_name}"] = importlib.import_module(
        f"patience_diff.{_module_name}"
    )
