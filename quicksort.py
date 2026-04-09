#!/usr/bin/env python3
"""QuickSort implementation with a simple command-line interface."""

from __future__ import annotations

from typing import Any, Callable, Iterable, List, Optional, Sequence, TypeVar

T = TypeVar("T")
KeyFunc = Callable[[T], Any]


def quicksort(
    sequence: Sequence[T],
    *,
    key: Optional[KeyFunc] = None,
    reverse: bool = False,
) -> List[T]:
    """Return a new list containing the items from *sequence* in sorted order."""

    seq = list(sequence)
    if len(seq) <= 1:
        return seq

    key_func = key or (lambda item: item)
    pivot_item = seq[len(seq) // 2]
    pivot_value = key_func(pivot_item)

    lesser: List[T] = []
    equal: List[T] = []
    greater: List[T] = []

    for item in seq:
        value = key_func(item)
        if value < pivot_value:
            lesser.append(item)
        elif value > pivot_value:
            greater.append(item)
        else:
            equal.append(item)

    if reverse:
        return (
            quicksort(greater, key=key, reverse=True)
            + equal
            + quicksort(lesser, key=key, reverse=True)
        )

    return (
        quicksort(lesser, key=key, reverse=False)
        + equal
        + quicksort(greater, key=key, reverse=False)
    )


def _parse_cli_values(values: Iterable[str], numeric: bool) -> List[Any]:
    """Convert CLI values to ints/floats when requested."""

    parsed: List[Any] = []
    for raw in values:
        if not numeric:
            parsed.append(raw)
            continue
        try:
            parsed.append(int(raw))
        except ValueError:
            try:
                parsed.append(float(raw))
            except ValueError:
                parsed.append(raw)
    return parsed


def _demo(values: List[Any], reverse: bool) -> None:
    sorted_values = quicksort(values, reverse=reverse)
    direction = "descending" if reverse else "ascending"
    print(f"Input ({direction}):  {values}")
    print(f"Sorted:             {sorted_values}")


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Sort values using QuickSort")
    parser.add_argument("values", nargs="*", help="Values to sort. Default demo if empty.")
    parser.add_argument(
        "--numeric",
        action="store_true",
        help="Attempt to treat each value as an int/float before sorting.",
    )
    parser.add_argument(
        "--reverse",
        action="store_true",
        help="Return the values in descending order.",
    )
    args = parser.parse_args()

    if args.values:
        parsed = _parse_cli_values(args.values, args.numeric)
    else:
        parsed = [34, 7, 23, 32, 5, 62]
        print("No values provided – using built-in sample sequence.")

    _demo(parsed, args.reverse)


if __name__ == "__main__":
    main()
