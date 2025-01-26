import math


def get_supported_shapes() -> list[str]:
    """
    Generate a hardcoded list of known (supported) shapes
    """

    return [
        "Circle",
        "Square",
        "Rectangle",
        "Right Triangle",
    ]


def circle_perimeter(radius: float) -> float:
    """
    TBW
    """

    return 2 * math.pi * radius


def circle_area(radius: float) -> float:
    """
    TBW
    """

    return math.pi * (radius ** 2)


def square_perimeter(side: float) -> float:
    """
    TBW
    """

    return 4 * side


def square_area(side: float) -> float:
    """
    TBW
    """

    return side ** 2


def rectangle_perimeter(length: float, height: float) -> float:
    """
    TBW
    """

    return (2 * length) + (2 * height)


def rectangle_area(length: float, height: float) -> float:
    """
    TBW
    """

    return length * height


def right_triangle_perimeter(base: float, height: float) -> float:
    """
    TBW
    """

    hypotenuse = math.sqrt((base**2) + (height**2))

    return base + height + hypotenuse


def right_triangle_area(base: float, height: float) -> float:
    """
    TBW
    """

    return 0.5 * base * height
