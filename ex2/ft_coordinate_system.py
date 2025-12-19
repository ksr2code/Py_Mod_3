#!/usr/bin/env python3
"""
Exercise 2: Position Tracker
3D coordinate system using tuples.
"""
import sys
import math


def ft_coordinate_system(coord_strings: list[str]):
    """Demonstrate tuple operations with 3D coordinates."""
    print("=== Game Coordinate System ===\n")
    position0 = (0, 0, 0)
    x1, y1, z1 = position0
    position1 = (10, 20, 5)
    x2, y2, z2 = position1
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    print(
        f"Position created: {position1}\n"
        f"Distance between {position0} and {position1}: "
        f"{distance:.2f}\n"
    )
    if not coord_strings:
        coord_strings = ["3,4,0", "abc,def,ghi"]
    for coord in coord_strings:
        try:
            coords = coord.split(',')
            x2 = int(coords[0])
            y2 = int(coords[1])
            z2 = int(coords[2])
            position2 = (x2, y2, z2)
            distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
            print(
                f'Parsing coordinates: "{coord}"\n'
                f"Parsed position: {position2}\n"
                f"Distance between {position0} and {position2}: "
                f"{distance:.2f}\n"
            )
        except Exception as e:
            print(
                f'Parsing invalid coordinates: "{coord}"\n'
                f"Error parsing coordinates: {e}\n"
                f"Error details - Type: {type(e).__name__}, Args: {e.args}\n"
            )
    position3 = (3, 4, 0)
    x, y, z = position3
    print(
        "Unpacking demonstration:\n"
        f"Player at x={x}, y={y}, z={z}\n"
        f"Coordinates: X={x}, Y={y}, Z={z}"
    )


if __name__ == "__main__":
    ft_coordinate_system(sys.argv[1:])
