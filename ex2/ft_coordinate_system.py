import math


def calculate_distance(tuple):
    """calculate the distance between 0.0.0 and the"""
    res = math.sqrt((tuple[0] - 0) ** 2 +
                    (tuple[1] - 0) ** 2 + (tuple[2] - 0) ** 2)
    return round(res, 2)


def ft_coordinate_system():
    """principal function for my program"""
    print("=== Game Coordinate System ===\n")
    tuple1 = (10, 20, 5)
    print(f"Position created: {tuple1}")
    print(f"Distance between (0, 0, 0) and {tuple1}: "
          f"{calculate_distance(tuple1)}\n")

    to_parse = "3,4,0"
    print(f'Parsing coordinates: "{to_parse}"')
    parsed = to_parse.split(",")
    tuple2 = tuple(int(x) for x in parsed)
    print(f"Parsed position: {tuple2}")
    print(f"Distance between (0, 0, 0) and {tuple2}: "
          f"{calculate_distance(tuple2)}\n")

    invalid = "abc,def,ghi"
    try:
        print(f'Parsing invalid coordinates: "{invalid}"')
        split = invalid.split(",")
        for x in split:
            x = int(x)

    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f'Error details - Type {type(e).__name__}, Args: ("{e}",)\n')

    print("Unpacking demonstration:")
    x, y, z = tuple2
    print(f"Player at x={x}, y= {y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    ft_coordinate_system()

# unpacking a tuple allows us to directly store the values in a single line
