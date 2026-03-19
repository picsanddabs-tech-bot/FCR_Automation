#!/usr/bin/env python3
"""Simple greeter script for Shravan."""

import sys

def build_message(name: str) -> str:
    return f"Hello, {name}! Keep exploring, learning, and having fun with tech."

def main() -> None:
    name = sys.argv[1] if len(sys.argv) > 1 else "Shravan"
    print(build_message(name))

if __name__ == "__main__":
    main()
