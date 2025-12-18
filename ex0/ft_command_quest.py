#!/usr/bin/env python3
"""
Exercise 0: Command Quest
A command-line argument demonstration program.
"""
import sys


def ft_command_quest():
    """Display program name and command-line arguments."""
    print("=== Command Quest ===")
    if len(sys.argv) < 2:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
        print(f"Total arguments: {len(sys.argv)}")
    else:
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments received: {len(sys.argv[1:])}")
        i = 1
        for arg in sys.argv[1:]:
            print(f"Argument {i}: {arg}")
            i += 1
        print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    ft_command_quest()
