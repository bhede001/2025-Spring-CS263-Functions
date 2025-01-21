import shapes

HEADER_WIDTH: int = 80
DIVIDER: str = "-" * HEADER_WIDTH


def display_menu() -> None:
    """
    Display a stylized program menu
    """

    header_text = "Available Shapes"
    print(DIVIDER)
    print(header_text.center(HEADER_WIDTH))
    print(DIVIDER)

    for idx, shape in enumerate(shapes.get_supported_shapes(), start=1):
        print(f"{idx}. {shape}")


def prompt_for_shape() -> str:
    """
    Prompt for a shape name

    Returns:
        Selected shape name in title case (first letter of each word
        capitalized)
    """

    desired_shape = input("Select a shape: ").title()

    return desired_shape


def prompt_for_precision() -> int:
    """
    Prompt for the desired number of decimal places.

    Raises:
        ValueError if the selected precision is less than zero
    """

    desired_precision = int(input("Enter the number of decimal places: "))
    if desired_precision < 0:
        raise ValueError("Precision must be >=0")

    return desired_precision


def prompt_for_another() -> str:
    """
    Prompt the user for a yes or no value
    """

    selected_option = input("Would you like to generate another problem (yes/no)? ")
    selected_option = selected_option.lower()

    return selected_option
