import project_template
import numpy as np


def main():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    result = project_template.adder(a, b)
    print(
        f"The result of adding {a} and {b} is {result}.\n"
        f'This is computed using project_template.adder from version "{project_template.__version__}"'
    )


if __name__ == "__main__":
    main()
