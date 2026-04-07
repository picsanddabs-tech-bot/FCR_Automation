"""Bubble sort implementation with a small CLI helper.

Usage examples:
    python bubble_sort.py 5 3 1 4 2
    python bubble_sort.py 10 7 9 --order desc
"""
from __future__ import annotations

import argparse
from typing import List


def bubble_sort(items: List[int], descending: bool = False) -> List[int]:
    """Return a new list containing the sorted values from *items*.

    Args:
        items: Sequence of integers to be sorted.
        descending: Sort order flag; False sorts ascending.
    """

    arr = list(items)
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

    if descending:
        arr.reverse()
    return arr


def _parse_cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Bubble sort integers from the CLI.")
    parser.add_argument(
        "values",
        nargs="+",
        type=int,
        help="Integers to sort",
    )
    parser.add_argument(
        "--order",
        choices=("asc", "desc"),
        default="asc",
        help="Sort order (default: asc)",
    )
    return parser.parse_args()


def main() -> None:
    args = _parse_cli()
    descending = args.order == "desc"
    result = bubble_sort(args.values, descending=descending)
    print("Sorted:", " ".join(str(v) for v in result))


if __name__ == "__main__":
    main()
