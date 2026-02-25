"""
main.py

Application entry point.
Demonstrates correct module import and naming conventions.
"""

import utils


def main() -> None:
    """
    Main function of the application.

    Args:
        None

    Returns:
        None
    """
    value = utils.example_function(10)
    print(value)


if __name__ == "__main__":
    main()