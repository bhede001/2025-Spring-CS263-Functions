from __future__ import annotations

import random

import shapes
import user_prompt


def generate_problem(shape_name: str, precision: int) -> str:
    """
    Generate a problem for a specified shape.

    Raises:
        ValueError if shape_name is not supported
    """

    match shape_name:
        case "Circle":
            radius = random.randint(1, 10)

            question = f"A *{shape_name}* with radius *{radius}*"

            perimeter = shapes.circle_perimeter(radius)
            area = shapes.circle_area(radius)

        case "Square":
            side = random.randint(1, 10)

            question = f"A *{shape_name}* with side length *{side}*"

            perimeter = shapes.square_perimeter(side)
            area = shapes.square_area(side)

        case "Rectangle":
            dims = [random.randint(1, 10) for _ in range(0, 2)]

            question = f"A *{shape_name}* with base *{dims[0]}* and length *{dims[1]}*"

            perimeter = shapes.rectangle_perimeter(*dims)
            area = shapes.rectangle_area(*dims)

        case "Right Triangle":
            dims = [random.randint(1, 10) for _ in range(0, 2)]

            question = f"A *{shape_name}* with base *{dims[0]}* and height *{dims[1]}*"

            perimeter = shapes.right_triangle_perimeter(*dims)
            area = shapes.right_triangle_area(*dims)

        case _:
            raise ValueError(f"{shape_name} is not supported.")

    problem = [
        f"{question} has what perimeter and area?",
        f"  - {perimeter = :.{precision}f}",
        f"  - {area = :.{precision}f}",
    ]

    return "\n".join(problem)


def main():
    known_shapes = shapes.get_supported_shapes()

    continue_generation = "yes"

    while continue_generation == "yes":
        user_prompt.display_menu()
        print()

        desired_shape = user_prompt.prompt_for_shape()
        if desired_shape not in known_shapes:
            print(f'[Error] - "{desired_shape}" is not supported.')
            print()
            continue

        print()
        desired_precision = user_prompt.prompt_for_precision()

        print()
        problem = generate_problem(desired_shape, desired_precision)
        print(problem)

        print()
        continue_generation = user_prompt.prompt_for_another()
        print()


if __name__ == "__main__":
    main()
