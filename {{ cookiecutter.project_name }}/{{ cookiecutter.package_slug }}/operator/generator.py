import numpy as np


def generate(iterations, size):
    """Convert a dataframe column to lowercase

        Args:
            iterations (int): Number of times the text will be repeated
            size (int): Substring size

        Returns:
            dataframe: Updated dataframe
    """

    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, " \
           "sed do eiusmod tempor incididunt ut labore et dolore  aliqua. " \
           "Ut enim ad minim veniam, quis nostrud exercitation  laboris " \
           "nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor " \
           "in reprehenderit in voluptate velit esse cillum  eu fugiat " \
           "nulla pariatur. Excepteur sint occaecat cupidatat  proident, " \
           "sunt in culpa qui officia deserunt mollit anim id est laborum."

    return list(np.repeat(text[0:int(size)], iterations))
