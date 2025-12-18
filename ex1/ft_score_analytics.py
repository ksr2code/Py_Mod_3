#!/usr/bin/env python3
"""
Exercise 1: Score Cruncher
Process and analyze player scores from command-line arguments.
"""
import sys


def ft_score_analytics():
    """Analyze player scores and display statistics."""
    print("=== Player Score Analytics ===")
    if len(sys.argv) < 2:
        print("No score provided. Usage: python3 "
              "ft_score_analytics.py <score1> <score2> ...")
    else:
        try:
            scores = []
            for arg in sys.argv[1:]:
                scores += [int(arg)]
            print(
                f"Scores processed: {scores}\n"
                f"Total players: {len(scores)}\n"
                f"Total score: {sum(scores)}\n"
                f"Average score: {sum(scores) / len(scores)}\n"
                f"High score: {max(scores)}\n"
                f"Low score: {min(scores)}\n"
                f"Score range: {max(scores) - min(scores)}"
            )
        except ValueError:
            print("Error: All arguments must be integers")


if __name__ == "__main__":
    ft_score_analytics()
